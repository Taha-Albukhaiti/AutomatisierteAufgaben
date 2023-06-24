import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


length = int(input("Gib die Länge des Passworts ein: "))


password = generate_password(length)
print("Generiertes Passwort:", password)

