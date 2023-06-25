# Automatisierte Aufgaben App

Die **Automatisierte Aufgaben App** ist eine Anwendung, die entwickelt wurde, um verschiedene automatisierte Aufgaben zu verwalten und einen Passwortmanager bereitzustellen. Die App wurde mit Python und der PyQt5-Bibliothek erstellt.

## Funktionen

Die Automatisierte Aufgaben App bietet folgende Funktionen:

1. **Automatisierungs-App**: Die App ermöglicht die Verwaltung von automatisierten Aufgaben. Benutzer können Aufgaben erstellen, bearbeiten und löschen. Jede Aufgabe kann einen Namen, eine Beschreibung und eine geplante Ausführungszeit haben. Die App unterstützt auch das Hinzufügen von Benachrichtigungen für Aufgaben.

2. **Passwortmanager**: Die App enthält einen Passwortmanager, mit dem Benutzer ihre Passwörter sicher speichern und verwalten können. Benutzer können Benutzernamen und zugehörige Passwörter eingeben, speichern und abrufen. Die Passwörter werden verschlüsselt gespeichert, um die Sicherheit zu gewährleisten.

## Verwendung

Um die Automatisierte Aufgaben App auszuführen, müssen Sie Python und die PyQt5-Bibliothek installiert haben. Folgen Sie diesen Schritten:

1. Stellen Sie sicher, dass Python installiert ist. Wenn nicht, können Sie es von der offiziellen Python-Website herunterladen und installieren: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Installieren Sie die PyQt5-Bibliothek. Öffnen Sie die Kommandozeile und geben Sie den folgenden Befehl ein:
pip install pyqt5
3. Laden Sie den Quellcode der App herunter und extrahieren Sie ihn in ein Verzeichnis Ihrer Wahl.

4. Navigieren Sie in der Kommandozeile zum Verzeichnis, in dem Sie den Quellcode extrahiert haben.

5. Geben Sie den folgenden Befehl ein, um die App auszuführen:

$ python MainApp.py

6. Das Hauptfenster der App wird geöffnet. Sie werden aufgefordert, sich anzumelden. Geben Sie Ihren Benutzernamen ein und klicken Sie auf "Anmelden".

7. Nach der Anmeldung haben Sie Zugriff auf die Hauptfunktionen der App: die Automatisierungs-App und den Passwortmanager. Klicken Sie auf die entsprechenden Schaltflächen, um die Apps zu öffnen und ihre Funktionen zu nutzen.

## Hinweis

Die App speichert die Passwörter in einer JSON-Datei. Stellen Sie sicher, dass die Datei "passwords.json" im selben Verzeichnis wie der Quellcode der App vorhanden ist. Wenn die Datei nicht vorhanden ist, wird sie automatisch erstellt, wenn Sie ein Passwort speichern.

Bitte beachten Sie, dass die App grundlegende Sicherheitsmaßnahmen enthält, aber es wird empfohlen, zusätzliche Sicherheitsvorkehrungen zu treffen, um die Passwörter zu schützen, wie zum Beispiel das Sperren Ihres Computers und das Verwenden eines sicheren Benutzerkontos.
