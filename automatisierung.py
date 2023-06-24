"""
Author: Taha Al-Bukhaiti
"""
import os
import shutil
import subprocess
import sys

from PyQt5.QtCore import QDateTime, Qt, pyqtSignal
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class AutomatisierungApp(QMainWindow):
    """
    Eine Anwendung zur Automatisierung von Dateiverschiebungen und Überwachung von Ordnern.

    Die Anwendung überwacht den Downloads-Ordner auf neue Fotos und verschiebt sie in den Zielordner.
    Sie zeigt eine Tabelle mit den verschobenen Dateien und ermöglicht das Öffnen der Dateien.
    """

    closed = pyqtSignal()  # Signal `closed` in der AutomatisierungApp-Klasse definieren

    def __init__(self):
        """
        Initialisiert die AutomatisierungApp.

        Erstellt und konfiguriert das Hauptfenster, erstellt das Table Widget für die Anzeige der verschobenen Dateien,
        lädt die zuvor verschobenen Dateien und überwacht den Downloads-Ordner für neue Fotos.
        """
        super().__init__()
        self.setWindowTitle("Automatisierung")
        self.setGeometry(100, 100, 500, 500)

        self.table_widget = QTableWidget(self)  # Table Widget zur Anzeige der verschobenen Dateien
        self.table_widget.setGeometry(10, 10, 480, 480)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["Dateiname", "Verschiebungszeitpunkt"])
        self.table_widget.itemDoubleClicked.connect(self.open_file)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.show()

        self.load_moved_files()  # Lade die zuvor verschobenen Dateien beim Start der App
        self.watch_downloads_fotos()

    def watch_downloads_fotos(self):
        """
        Überwacht den Downloads-Ordner auf neue Fotos und verschiebt sie in den Zielordner.

        Aktualisiert die Tabelle der verschobenen Dateien in der GUI.
        """
        downloads_dir = os.path.expanduser("~/Downloads")
        target_dir = os.path.expanduser("~/Documents/Bilder")

        for filename in os.listdir(downloads_dir):
            if filename.lower().endswith(".jpg") or filename.lower().endswith(".heic") \
                    or filename.lower().endswith(".jpeg") or filename.lower().endswith(".png"):
                file_path = os.path.join(downloads_dir, filename)
                target_path = os.path.join(target_dir, filename)
                shutil.move(file_path, target_path)

                # Aktualisiere die Tabelle der verschobenen Dateien in der GUI
                timestamp = QDateTime.currentDateTime().toString(Qt.DefaultLocaleLongDate)
                row_count = self.table_widget.rowCount()
                self.table_widget.insertRow(row_count)
                self.table_widget.setItem(row_count, 0, QTableWidgetItem(filename))
                self.table_widget.setItem(row_count, 1, QTableWidgetItem(timestamp))
                self.save_moved_file(filename, timestamp)  # Speichere den Dateinamen und den Zeitstempel

        self.adjust_table_columns()

    def save_moved_file(self, filename, timestamp):
        """
        Speichert den Dateinamen und den Zeitstempel einer verschobenen Datei in einer Textdatei.

        Args:
            filename (str): Der Name der verschobenen Datei.
            timestamp (str): Der Zeitstempel der Verschiebung.
        """
        with open("moved_files.txt", "a") as file:
            file.write(f"{filename},{timestamp}\n")

    def load_moved_files(self):
        """
        Lädt die zuvor verschobenen Dateien aus der Textdatei und aktualisiert die Tabelle in der GUI.
        """
        if os.path.exists("moved_files.txt"):
            with open("moved_files.txt", "r") as file:
                moved_files = file.readlines()
                for moved_file in moved_files:
                    filename, timestamp = moved_file.strip().split(",")
                    row_count = self.table_widget.rowCount()
                    self.table_widget.insertRow(row_count)
                    self.table_widget.setItem(row_count, 0, QTableWidgetItem(filename))
                    self.table_widget.setItem(row_count, 1, QTableWidgetItem(timestamp))

        self.adjust_table_columns()

    def resizeEvent(self, event):
        """
        Behandelt das Resize-Event des Hauptfensters und passt die Spaltenbreite der Tabelle an.

        Args:
            event (QResizeEvent): Das Resize-Event.
        """
        super().resizeEvent(event)
        self.adjust_table_columns()

    def adjust_table_columns(self):
        """
        Passt die Spaltenbreite der Tabelle basierend auf der Breite des Table Widgets an.
        """
        table_width = self.table_widget.viewport().width()
        self.table_widget.setColumnWidth(0, int(table_width * 0.7))
        self.table_widget.setColumnWidth(1, int(table_width * 0.3))

    def open_file(self, item):
        """
        Öffnet die ausgewählte Datei.

        Args:
            item (QTableWidgetItem): Das ausgewählte Element in der Tabelle.
        """
        filename_item = self.table_widget.item(item.row(), 0)
        if filename_item:
            filename = filename_item.text()
            target_dir = os.path.expanduser("~/Documents/Bilder")
            file_path = os.path.join(target_dir, filename)
            if os.path.exists(file_path):
                if sys.platform == 'win32':
                    os.startfile(file_path)  # Öffnet die Datei unter Windows
                elif sys.platform == 'darwin':
                    subprocess.call(['open', file_path])  # Öffnet die Datei auf macOS
                else:
                    subprocess.call(['xdg-open', file_path])  # Öffnet die Datei auf Linux
            else:
                QMessageBox.warning(self, "Datei nicht gefunden", "Die Datei konnte nicht gefunden werden.")


"""
Die verwendeten Bibliotheken, APIs und Module sind:

- os: Eine Python-Bibliothek, die Funktionen für die Interaktion mit dem Betriebssystem bereitstellt, z. B. Datei- und Ordneroperationen.

- shutil: Eine Python-Bibliothek, die Funktionen zum Kopieren, Verschieben und Löschen von Dateien und Ordnern bereitstellt.

- subprocess: Eine Python-Bibliothek, mit der externe Prozesse gestartet und gesteuert werden können, z. B. das Öffnen von Dateien mit dem Standardprogramm.

- sys: Ein Modul, das Funktionen und Variablen zur Interaktion mit dem Python-Interpreter bereitstellt, z. B. System-spezifische Parameter und Funktionen.

- PyQt5.QtCore: Ein Modul von PyQt5, das die Kernfunktionalität von Qt enthält, einschließlich Datentypen, Signalen und Slots sowie Ereignisverarbeitung.

- PyQt5.QtWidgets: Ein Modul von PyQt5, das die Widgets und Funktionen für die Erstellung von GUI-Anwendungen bereitstellt, z. B. Fenster, Layouts und Steuerelemente.

Die verwendeten APIs sind:

PyQt5 API: Eine API für die Entwicklung von GUI-Anwendungen unter Verwendung von PyQt5, einer Python-Bindung für das Qt-Framework.
Zusammen bieten diese Bibliotheken, APIs und Module die erforderlichen Funktionen zum Erstellen des Hauptfensters, 
des Table Widgets, zum Überwachen von Ordnern, zum Verschieben von Dateien, zum Anzeigen von Dateien in der Tabelle 
und zum Öffnen von Dateien mit dem Standardprogramm des Betriebssystems.

"""
