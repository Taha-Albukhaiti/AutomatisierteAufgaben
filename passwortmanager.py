"""
Author: Taha Al-Bukhaiti
"""
import json
import os
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QDialog, \
    QGridLayout, QTableWidget, QTableWidgetItem, QWidget


class PasswordManager:
    """
    Eine Klasse zum Verwalten von Passwörtern.

    Parameter:
        filename (str): Der Dateiname der Datei, in der die Passwörter gespeichert werden.

    Methoden:
        save_password(username, password):
            Speichert ein Passwort für einen Benutzernamen.

        load_passwords_from_file():
            Lädt die gespeicherten Passwörter aus der Datei.

        get_password(username):
            Ruft das Passwort für einen Benutzernamen ab.

        get_all_passwords():
            Ruft alle gespeicherten Passwörter ab.

        save_passwords_to_file():
            Speichert die Passwörter in der Datei.
    """

    def __init__(self, filename):
        self.filename = filename
        self.passwords = {}

    def save_password(self, username, password):
        """
        Speichert ein Passwort für einen Benutzernamen.

        Args:
            username (str): Der Benutzername.
            password (str): Das Passwort.
        """
        self.passwords[username] = password
        self.save_passwords_to_file()

    def load_passwords_from_file(self):
        """
        Lädt die gespeicherten Passwörter aus der Datei.
        """
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                file_content = file.read()
                if file_content:
                    self.passwords = json.loads(file_content)

    def get_password(self, username):
        """
        Ruft das Passwort für einen Benutzernamen ab.

        Args:
            username (str): Der Benutzername.

        Returns:
            str: Das Passwort für den angegebenen Benutzernamen.
        """
        return self.passwords.get(username)

    def get_all_passwords(self):
        """
        Ruft alle gespeicherten Passwörter ab.

        Returns:
            dict: Ein Dictionary mit allen gespeicherten Benutzernamen und Passwörtern.
        """
        return self.passwords

    def save_passwords_to_file(self):
        """
        Speichert die Passwörter in der Datei.
        """
        with open(self.filename, "w") as file:
            json.dump(self.passwords, file)


class PasswordManagerApp(QMainWindow):
    """
    Eine GUI-Anwendung zum Verwalten von Passwörtern.

    Signale:
        closed: Signal, das ausgelöst wird, wenn die Anwendung geschlossen wird.

    Methoden:
        save_password():
            Speichert das eingegebene Passwort für den angegebenen Benutzernamen.

        retrieve_password():
            Ruft das Passwort für den angegebenen Benutzernamen ab.

        show_all_passwords():
            Zeigt alle gespeicherten Benutzernamen und Passwörter in einer Tabelle an.

        closeEvent(event):
            Behandelt das Ereignis des Schließens des Fensters.
    """

    closed = pyqtSignal()

    def __init__(self, password_manager):
        """
        Initialisiert die PasswordManagerApp.

        Args:
            password_manager (PasswordManager): Die Instanz des PasswordManager, der die Passwörter verwaltet.
        """
        super().__init__()
        self.setWindowTitle("Passwortmanager")
        self.setGeometry(100, 100, 300, 200)

        self.password_manager = password_manager

        self.username_label = QLabel("Benutzername:", self)
        self.username_input = QLineEdit(self)

        self.password_label = QLabel("Passwort:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.save_button = QPushButton("Passwort speichern", self)
        self.save_button.clicked.connect(self.save_password)

        self.retrieve_button = QPushButton("Passwort abrufen", self)
        self.retrieve_button.clicked.connect(self.retrieve_password)

        self.show_all_button = QPushButton("Alle Passwörter anzeigen", self)
        self.show_all_button.clicked.connect(self.show_all_passwords)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.save_button)
        layout.addWidget(self.retrieve_button)
        layout.addWidget(self.show_all_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def save_password(self):
        """
        Speichert das eingegebene Passwort für den angegebenen Benutzernamen.
        Zeigt eine Warnung an, wenn kein Benutzername oder Passwort eingegeben wurde
        oder wenn bereits ein Passwort für den angegebenen Benutzernamen existiert.
        """
        username = self.username_input.text()
        password = self.password_input.text()
        if not username or not password:
            QMessageBox.warning(self, "Passwort speichern", "Bitte geben Sie Benutzernamen und Passwort ein.")
            return
        if self.password_manager.get_password(username):
            QMessageBox.warning(self, "Passwort speichern", "Ein Passwort für diesen Benutzernamen existiert bereits.")
            return
        self.password_manager.save_password(username, password)
        self.username_input.clear()
        self.password_input.clear()

    def retrieve_password(self):
        """
        Ruft das Passwort für den angegebenen Benutzernamen ab.
        Zeigt eine Warnung an, wenn kein Benutzername eingegeben wurde
        oder wenn der Benutzername ungültig ist.
        """
        username = self.username_input.text()
        if not username:
            QMessageBox.warning(self, "Passwort abrufen", "Bitte geben Sie den Benutzernamen ein.")
            return
        stored_password = self.password_manager.get_password(username)
        if stored_password:
            QMessageBox.information(
                self, "Passwort abrufen", f"Des Passwort des Benutzername {username} lautet:\n\n{stored_password}"
            )
        else:
            QMessageBox.warning(self, "Passwort abrufen", "Ungültiger Benutzername")
        self.username_input.clear()
        self.password_input.clear()

    def show_all_passwords(self):
        """
        Zeigt alle gespeicherten Benutzernamen und Passwörter in einer Tabelle an.
        """
        all_passwords = self.password_manager.get_all_passwords()
        dialog = QDialog(self)
        dialog.setWindowTitle("Alle Passwörter anzeigen")
        layout = QGridLayout()
        dialog.setLayout(layout)

        table_widget = QTableWidget(dialog)
        table_widget.setColumnCount(2)
        table_widget.setHorizontalHeaderLabels(["Benutzername", "Passwort"])
        table_widget.setRowCount(len(all_passwords))

        row = 0
        for username, password in all_passwords.items():
            username_item = QTableWidgetItem(username)
            password_item = QTableWidgetItem(password)
            table_widget.setItem(row, 0, username_item)
            table_widget.setItem(row, 1, password_item)
            row += 1

        table_widget.resizeColumnsToContents()
        table_widget.horizontalHeader().setStretchLastSection(True)
        table_widget.verticalHeader().setVisible(False)

        layout.addWidget(table_widget)
        dialog.exec_()

    def closeEvent(self, event):
        """
        Behandelt das Ereignis des Schließens des Fensters.
        Sendet das Signal `closed` aus und akzeptiert das Ereignis.
        """
        self.closed.emit()
        event.accept()
