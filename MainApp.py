"""
Author: Taha Al-Bukhaiti

MainApp Modul:

Dieses Modul enthält die `MainApp`-Klasse, die das Hauptfenster der Anwendung darstellt.

Klassen:
- MainApp: Das Hauptfenster der Anwendung.

"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QDialog
from LoginWindow import LoginWindow
from passwortmanager import PasswordManagerApp, PasswordManager
from automatisierung import AutomatisierungApp
import faulthandler

faulthandler.enable()


class MainApp(QMainWindow):
    """
    Die Klasse `MainApp` repräsentiert das Hauptfenster der Anwendung.

    Attribute:
        login_window (LoginWindow): Das Anmeldefenster.
        password_manager (PasswordManager): Der Passwortmanager.

    Signale:
        automatisierung_app_closed: Signal, das ausgelöst wird, wenn das Automatisierungsfenster geschlossen wird.
        passwortmanager_app_closed: Signal, das ausgelöst wird, wenn das Passwortmanagerfenster geschlossen wird.
    """

    def __init__(self):
        """
        Initialisiert die `MainApp`.

        Erstellt das Hauptfenster, lädt den Passwortmanager und zeigt die Login-Dialogbox an.
        """
        super().__init__()
        self.setWindowTitle("Hauptfenster")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)

        button1 = QPushButton("Automatisierung", self)
        button2 = QPushButton("Passwortmanager", self)

        button1.clicked.connect(self.open_automatisierung_app)
        button2.clicked.connect(self.open_passwortmanager_app)

        layout.addWidget(button1)
        layout.addWidget(button2)

        self.login_window = LoginWindow()
        if self.login_window.exec_() != QDialog.Accepted:
            self.close()
            return

        self.password_manager = PasswordManager("passwords.json")
        self.password_manager.load_passwords_from_file()

        self.automatisierung_app = None
        self.passwortmanager_app = None

    def open_automatisierung_app(self):
        """
        Öffnet das Automatisierungsfenster.

        Wenn das Automatisierungsfenster noch nicht geöffnet ist, wird eine neue Instanz erstellt
        und das `closed`-Signal mit der Methode `close_automatisierung_app` verbunden.
        """
        if self.login_window.logged_in:
            if not self.automatisierung_app:
                self.automatisierung_app = AutomatisierungApp()
                self.automatisierung_app.closed.connect(self.close_automatisierung_app)
            self.automatisierung_app.show()

    def close_automatisierung_app(self):
        """
        Behandelt das Schließen des Automatisierungsfensters.

        Setzt die Referenz auf das Automatisierungsfenster auf `None`.
        """
        self.automatisierung_app = None

    def open_passwortmanager_app(self):
        """
        Öffnet das Passwortmanagerfenster.

        Wenn das Passwortmanagerfenster noch nicht geöffnet ist, wird eine neue Instanz erstellt
        und das `closed`-Signal mit der Methode `close_passwortmanager_app` verbunden.
        """
        if self.login_window.logged_in:
            if not self.passwortmanager_app:
                self.passwortmanager_app = PasswordManagerApp(self.password_manager)
                self.passwortmanager_app.closed.connect(self.close_passwortmanager_app)
            self.passwortmanager_app.show()

    def close_passwortmanager_app(self):
        """
        Behandelt das Schließen des Passwortmanagerfensters.

        Setzt die Referenz auf das Passwortmanagerfenster auf `None`.
        """
        self.passwortmanager_app = None


if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()
