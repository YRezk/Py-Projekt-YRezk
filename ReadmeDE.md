
# Todo-Listen-Verwaltung REST API

### Inhaltsverzeichnis

- [Todo-Listen-Verwaltung REST API](#todo-listen-verwaltung-rest-api)
    - [Inhaltsverzeichnis](#inhaltsverzeichnis)
    - [Übersicht](#übersicht)
    - [Funktionen](#funktionen)
      - [Listenverwaltung](#listenverwaltung)
      - [Todo‑Eintragsverwaltung](#todoeintragsverwaltung)
    - [Voraussetzungen](#voraussetzungen)
    - [Installation](#installation)
    - [Server starten](#server-starten)
    - [API testen](#api-testen)
    - [Dokumentation](#dokumentation)
    - [Projektstruktur](#projektstruktur)
    - [Lizenz](#lizenz)
    - [Kontakt](#kontakt)

---

### Übersicht

Dieses Repository enthält eine REST API zur Verwaltung von Todo‑Listen und Todo‑Einträgen, implementiert mit dem Flask‑Framework. Die API ermöglicht es, Todo‑Listen sowie deren Einträge zu erstellen, abzurufen, zu aktualisieren und zu löschen.

---

### Funktionen

#### Listenverwaltung
- **GET `/lists`:** Alle Todo‑Listen abrufen.
- **POST `/list`:** Eine neue Todo‑Liste erstellen.
- **GET `/list/<list_id>`:** Alle Todo‑Einträge einer bestimmten Liste abrufen.
- **DELETE `/list/<list_id>`:** Eine Todo‑Liste samt zugehöriger Einträge löschen.

#### Todo‑Eintragsverwaltung
- **POST `/todo-list/<list_id>/entry`:** Einen neuen Todo‑Eintrag zu einer bestehenden Liste hinzufügen.
- **PUT `/todo-list/<list_id>/entry/<entry_id>`:** Einen bestehenden Todo‑Eintrag aktualisieren.
- **DELETE `/todo-list/<list_id>/entry/<entry_id>`:** Einen Todo‑Eintrag löschen.

Die vollständige API-Spezifikation findest du in der Datei  
[OpenAPI-Spezifikation (IFA32).pdf](docs/OpenAPI-Spezifikation%20(IFA32).pdf)  
im Ordner `docs/`.

---

### Voraussetzungen

- **Python 3.x:** Stelle sicher, dass du eine aktuelle Version von Python 3.x installiert hast.
- **Pip:** Das Python-Paketverwaltungstool (wird normalerweise zusammen mit Python installiert).

---

### Installation

1. **Repository klonen:**

   Klone das Repository in dein lokales System:
   ```bash
   git clone <REPO-URL>
   cd TodoListenVerwaltung
   ```

2. **Abhängigkeiten installieren:**

   Die Datei `requirements.txt` enthält mindestens folgende Zeile:

   ```ini
   Flask==2.2.5
   ```

   Installiere alle benötigten Pakete mit:

   ```bash
   pip install -r requirements.txt
   ```

---

### Server starten

Navigiere in das Projektverzeichnis und starte den Server mit:

```bash
python -m app.main
```

Der Server läuft standardmäßig unter [http://0.0.0.0:5000](http://0.0.0.0:5000).

---

### API testen

Automatisierte Tests befinden sich im Ordner `tests/`. Führe die Tests mit folgendem Befehl aus:

```bash
python -m unittest discover -s tests
```

Dies führt alle Tests im Verzeichnis `tests/` aus und zeigt dir die Ergebnisse im Terminal an.

---

### Dokumentation

Die vollständige API-Dokumentation findest du in der Datei:

[OpenAPI-Spezifikation (IFA32).pdf](docs/OpenAPI-Spezifikation%20(IFA32).pdf)

---

### Projektstruktur

```
TodoListenVerwaltung/
├── README.md
├── requirements.txt
├── docs/
│   └── OpenAPI-Spezifikation (IFA32).pdf
├── app/
│   ├── __init__.py       # Initialisiert die Flask-App, lädt Konfigurationen und importiert Module
│   ├── config.py         # Enthält Konfigurationseinstellungen (z. B. Debug-Modus, Host, Port)
│   ├── main.py           # Einstiegspunkt, der den Server startet
│   ├── lists.py          # API-Endpunkte zur Verwaltung der Todo‑Listen (Abrufen, Erstellen, Löschen)
│   └── todos.py          # API-Endpunkte zur Verwaltung der Todo‑Einträge (Hinzufügen, Aktualisieren, Löschen)
└── tests/
    └── test_api.py       # Testfälle für die API-Endpunkte
```

---

### Lizenz

Dieses Projekt steht unter der Apache 2.0 License.

---

### Kontakt

Bei Fragen oder Anregungen wende dich bitte an:  
[Y@Musterman.com](Y@Musterman.com)

