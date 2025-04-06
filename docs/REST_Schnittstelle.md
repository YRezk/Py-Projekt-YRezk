
# Entwurf und Implementierung einer REST-Schnittstelle

| Endpunkt | HTTP-Methode | Beschreibung | Parameter | Rückgabewerte |
|----------|--------------|--------------|-----------|---------------|
| `/todo-list/{list_id}/entries` | GET | Liefert alle Einträge einer Todo-Liste zurück. | URL-Element: ID der gewünschten Liste | **Statuscodes:**<br>200 bei Erfolg<br>404 bei falscher ID<br>**Body:** JSON-Objekt: Liste aller Einträge der gegebenen Liste |
| `/todo-list/{list_id}` | DELETE | Löscht eine komplette Todo-Liste mit allen Einträgen. | URL-Element: ID der gewünschten Liste | **Statuscodes:**<br>200 bei Erfolg<br>404 bei falscher ID<br>**Body:** `{‚msg‘: ‚success‘}` |
| `/todo-list` | POST | Fügt eine neue Todo-Liste hinzu. | JSON-Objekt im Body:<br>`{‚name‘: ‚???‘}` | **Statuscodes:**<br>200 bei Erfolg<br>400 bei fehlerhaftem Request<br>**Body:** `{‚id‘: ‚???‘, ‚name‘: ‚???‘}` |
| `/todo-list/{list_id}/entry` | POST | Fügt einen Eintrag zu einer bestehenden Todo-Liste hinzu. | URL-Element: ID der gewünschten Liste<br>JSON-Objekt im Body:<br>`{‚name‘: ‚???‘, ‚description‘: ‚???‘}` | **Statuscodes:**<br>200 bei Erfolg<br>400 bei fehlerhaftem Request<br>404 bei falscher ID<br>**Body:** `{‚id‘: ‚???‘, ‚name‘: ‚???‘, ‚description‘: ‚???‘}` |
| `/todo-list/{list_id}/entry/{entry_id}` | PUT | Aktualisiert einen bestehenden Eintrag. | URL-Element: ID der gewünschten Liste, ID des Eintrags<br>JSON-Objekt im Body:<br>`{‚name‘: ‚???‘, ‚description‘: ‚???‘}` | **Statuscodes:**<br>200 bei Erfolg<br>400 bei fehlerhaftem Request<br>404 bei falscher ID<br>**Body:** `{‚id‘: ‚???‘, ‚name‘: ‚???‘, ‚description‘: ‚???‘}` |
| `/todo-list/{list_id}/entry/{entry_id}` | DELETE | Löscht einen einzelnen Eintrag einer Todo-Liste. | URL-Element: ID der gewünschten Liste, ID des Eintrags | **Statuscodes:**<br>200 bei Erfolg<br>404 bei falscher ID<br>**Body:** `{‚msg‘: ‚success‘}` |
| `/todo-lists` | GET | Liefert alle Todo-Listen zurück. | - | **Statuscodes:**<br>200 bei Erfolg<br>**Body:** JSON-Objekt: Liste aller Todo-Listen |
| `/todo-list/{list_id}` | GET | Liefert eine Liste zurück. | URL-Element: ID der gewünschten Liste | **Statuscodes:**<br>200 bei Erfolg<br>404 bei falscher ID<br>**Body:** `{‚id‘: ‚???‘, ‚name‘: ‚???‘}` |

## Allgemeines

- Alle Endpunkte liefern `405` zurück, wenn die falsche Methode verwendet wurde.
- Alle Endpunkte liefern `500` bei einem Fehler im Server.
