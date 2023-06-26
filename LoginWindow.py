"""
Author: Taha Al-Bukhaiti

RegisterWindow Modul:

Dieses Modul enthält die `RegisterWindow`-Klasse, die das Fenster zur Benutzerregistrierung darstellt.

Klassen:
- RegisterWindow: Das Registrierungsfenster.

"""

import hashlib
import json
import os
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout



class RegisterWindow(QDialog):
    """
    Die Klasse `RegisterWindow` repräsentiert das Registrierungsfenster der Anwendung.

    Attribute:
        username_label (QLabel): Das Label für den Benutzernamen.
        username_input (QLineEdit): Das Eingabefeld für den Benutzernamen.
        password_label (QLabel): Das Label für das Passwort.
        password_input (QLineEdit): Das Eingabefeld für das Passwort.
        email_label (QLabel): Das Label für die E-Mail-Adresse.
        email_input (QLineEdit): Das Eingabefeld für die E-Mail-Adresse.
        register_button (QPushButton): Der Registrieren-Button.

    Methoden:
        register(): Registriert einen neuen Benutzer.
        user_exists(username): Überprüft, ob ein Benutzer bereits existiert.
        register_user(username, password, email): Registriert einen neuen Benutzer in der Benutzerdatenbank.
        show_message(title, message): Zeigt eine Dialognachricht an.
    """

    def __init__(self):
        """
        Initialisiert das `RegisterWindow`.

        Erstellt das Registrierungsfenster mit den entsprechenden Eingabefeldern und Buttons.
        """
        super().__init__()
        self.setWindowTitle("Registrierung")
        self.setGeometry(100, 100, 300, 200)

        self.username_label = QLabel("Benutzername:", self)
        self.username_input = QLineEdit(self)

        self.password_label = QLabel("Passwort:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.email_label = QLabel("E-Mail:", self)
        self.email_input = QLineEdit(self)

        self.register_button = QPushButton("Registrieren", self)
        self.register_button.clicked.connect(self.register)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def register(self):
        """
        Registriert einen neuen Benutzer.

        Erfasst die eingegebenen Daten, überprüft die Gültigkeit und registriert den Benutzer,
        falls alle Daten korrekt sind.
        """
        username = self.username_input.text()
        password = self.password_input.text()
        email = self.email_input.text()

        if username and password and email:
            if not self.user_exists(username):
                self.register_user(username, password, email)
                self.accept()
            else:
                self.show_message("Registrierung fehlgeschlagen", "Benutzername bereits vergeben.")
        else:
            self.show_message("Registrierung fehlgeschlagen", "Ungültige Eingabe.")

    def user_exists(self, username):
        """
        Überprüft, ob ein Benutzer bereits existiert.

        Parameters:
            username (str): Der Benutzername.

        Returns:
            bool: True, falls der Benutzer existiert, ansonsten False.
        """
        if os.path.exists("users.json"):
            with open("users.json", "r") as file:
                users = json.load(file)
                return username in users
        return False

    def register_user(self, username, password, email):
        """
        Registriert einen neuen Benutzer in der Benutzerdatenbank.

        Parameters:
            username (str): Der Benutzername.
            password (str): Das Passwort.
            email (str): Die E-Mail-Adresse.
        """
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user_data = {
            "username": username,
            "password": hashed_password,
            "email": email
        }

        if os.path.exists("users.json"):
            with open("users.json", "r") as file:
                users = json.load(file)
                users.append(user_data)
        else:
            users = [user_data]

        with open("users.json", "w") as file:
            json.dump(users, file)

    def show_message(self, title, message):
        """
        Zeigt eine Dialognachricht an.

        Parameters:
            title (str): Der Titel der Dialognachricht.
            message (str): Die Nachricht.
        """
        dialog = QDialog(self)
        dialog.setWindowTitle(title)

        layout = QVBoxLayout()
        label = QLabel(message, dialog)
        layout.addWidget(label)
        dialog.setLayout(layout)

        dialog.exec_()


"""
Author: Taha Al-Bukhaiti

LoginWindow Modul:

Dieses Modul enthält die `LoginWindow`-Klasse, die das Fenster zur Benutzeranmeldung darstellt.

Klassen:
- LoginWindow: Das Anmeldungs-Fenster.

"""


class LoginWindow(QDialog):
    """
    Die Klasse `LoginWindow` repräsentiert das Anmeldungs-Fenster der Anwendung.

    Attribute:
        username_label (QLabel): Das Label für den Benutzernamen.
        username_input (QLineEdit): Das Eingabefeld für den Benutzernamen.
        password_label (QLabel): Das Label für das Passwort.
        password_input (QLineEdit): Das Eingabefeld für das Passwort.
        login_button (QPushButton): Der Anmelden-Button.
        register_button (QPushButton): Der Registrieren-Button.

    Methoden:
        login(): Führt den Anmeldevorgang aus.
        register(): Öffnet das Registrierungsfenster.
        user_exists(username): Überprüft, ob ein Benutzer bereits existiert.
        check_password(username, password): Überprüft das eingegebene Passwort für den angegebenen Benutzer.
        show_message(title, message): Zeigt eine Dialognachricht an.
    """

    def __init__(self):
        """
        Initialisiert das `LoginWindow`.

        Erstellt das Anmeldungs-Fenster mit den entsprechenden Eingabefeldern und Buttons.
        """
        super().__init__()
        self.setWindowTitle("Anmeldung")
        self.setGeometry(100, 100, 300, 200)

        self.username_label = QLabel("Benutzername:", self)
        self.username_input = QLineEdit(self)

        self.password_label = QLabel("Passwort:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Anmelden", self)
        self.login_button.clicked.connect(self.login)

        self.register_button = QPushButton("Registrieren", self)
        self.register_button.clicked.connect(self.register)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

        self.username = None
        self.password = None

    def login(self):
        """
        Führt den Anmeldevorgang aus.

        Erfasst die eingegebenen Daten, überprüft die Gültigkeit und führt den Anmeldevorgang aus,
        wenn die Daten korrekt sind.
        """
        self.username = self.username_input.text()
        self.password = self.password_input.text()

        if self.username and self.password:
            if self.user_exists(self.username):
                if self.check_password(self.username, self.password):
                    self.accept()
                else:
                    self.show_message("Anmeldung fehlgeschlagen", "Falsches Passwort.")
            else:
                self.show_message("Anmeldung fehlgeschlagen", "Benutzer existiert nicht.")
        else:
            self.show_message("Anmeldung fehlgeschlagen", "Ungültige Eingabe.")

    def register(self):
        """
        Öffnet das Registrierungsfenster.

        Öffnet das Registrierungsfenster und erfasst die eingegebenen Daten,
        wenn die Registrierung erfolgreich ist.
        """
        register_window = RegisterWindow()
        if register_window.exec_() == QDialog.Accepted:
            self.username = register_window.username_input.text()
            self.password = register_window.password_input.text()
            self.accept()

    def user_exists(self, username):
        """
        Überprüft, ob ein Benutzer bereits existiert.

        Parameters:
            username (str): Der Benutzername.

        Returns:
            bool: True, falls der Benutzer existiert, ansonsten False.
        """
        if os.path.exists("users.json"):
            with open("users.json", "r") as file:
                users = json.load(file)
                return any(user["username"] == username for user in users)
        return False

    def check_password(self, username, password):
        """
        Überprüft das eingegebene Passwort für den angegebenen Benutzer.

        Parameters:
            username (str): Der Benutzername.
            password (str): Das Passwort.

        Returns:
            bool: True, falls das Passwort korrekt ist, ansonsten False.
        """
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if os.path.exists("users.json"):
            with open("users.json", "r") as file:
                users = json.load(file)
                return any(user["username"] == username and user["password"] == hashed_password for user in users)
        return False

    def show_message(self, title, message):
        """
        Zeigt eine Dialognachricht an.

        Parameters:
            title (str): Der Titel der Dialognachricht.
            message (str): Die Nachricht.
        """
        dialog = QDialog(self)
        dialog.setWindowTitle(title)

        layout = QVBoxLayout()
        label = QLabel(message, dialog)
        layout.addWidget(label)
        dialog.setLayout(layout)

        dialog.exec_()
