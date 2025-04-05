# Todo-Listen-Verwaltung REST API

Dieses Projekt implementiert eine REST-API zur Verwaltung von Todo-Listen und Todo-Einträgen. Die API ermöglicht folgende Funktionen:

- **Listenverwaltung:**
  - **GET /lists:** Alle Todo-Listen abrufen.
  - **POST /list:** Eine neue Todo-Liste erstellen.
  - **GET /list/&lt;list_id&gt;:** Alle Todo-Einträge einer bestimmten Liste abrufen.
  - **DELETE /list/&lt;list_id&gt;:** Eine Todo-Liste (und zugehörige Einträge) löschen.

- **Todo-Einträge:**
  - **POST /todo-list/&lt;list_id&gt;/entry:** Einen neuen Todo-Eintrag zu einer bestehenden Liste hinzufügen.
  - **PUT /todo-list/&lt;list_id&gt;/entry/&lt;entry_id&gt;:** Einen bestehenden Todo-Eintrag aktualisieren.
  - **DELETE /todo-list/&lt;list_id&gt;/entry/&lt;entry_id&gt;:** Einen Todo-Eintrag löschen.

## Installation

1. **Voraussetzungen:**  
   Stelle sicher, dass Python 3.x installiert ist.

2. **Abhängigkeiten installieren:**  
   Führe folgenden Befehl im Projektverzeichnis aus:
   ```bash
   pip install -r requirements.txt