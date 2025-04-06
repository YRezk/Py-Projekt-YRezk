# Todo-Listen-Verwaltung REST API

## Table of Contents

- [Todo-Listen-Verwaltung REST API](#todo-listen-verwaltung-rest-api)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
    - [List Management](#list-management)
    - [To-Do Entry Management](#to-do-entry-management)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Server](#running-the-server)
  - [Testing the API](#testing-the-api)
  - [Documentation](#documentation)
  - [Project Structure](#project-structure)
  - [License](#license)
  - [Contact](#contact)

---

## Overview

This repository contains a REST API for managing to-do lists and to-do entries, implemented using the Flask framework. The API allows you to create, retrieve, update, and delete to-do lists and their entries.

---

## Features

### List Management
- **GET `/lists`**: Retrieve all to-do lists.
- **POST `/list`**: Create a new to-do list.
- **GET `/list/<list_id>`**: Retrieve all to-do entries for a specific list.
- **DELETE `/list/<list_id>`**: Delete a to-do list along with its associated entries.

### To-Do Entry Management
- **POST `/todo-list/<list_id>/entry`**: Add a new to-do entry to an existing list.
- **PUT `/todo-list/<list_id>/entry/<entry_id>`**: Update an existing to-do entry.
- **DELETE `/todo-list/<list_id>/entry/<entry_id>`**: Delete a to-do entry.

The full API specification is available in the file:
[OpenAPI-Specification (IFA32).pdf](docs/OpenAPI-Spezifikation%20(IFA32).pdf) located in the `docs/` folder.

---

## Prerequisites

- **Python 3.x**: Ensure you have an up-to-date version of Python 3.x installed.
- **Pip**: The Python package installer (usually installed with Python).

---

## Installation

1. **Clone the Repository**:

```bash
git clone <REPO-URL>
cd TodoListenVerwaltung
```

2. **Install Dependencies**:

The `requirements.txt` file includes at least the following:

```ini
Flask==2.2.5
```

Install all required packages with:

```bash
pip install -r requirements.txt
```

---

## Running the Server

Navigate to the project directory and start the server with:

```bash
python -m app.main
```

The server will run by default at `http://0.0.0.0:5000`.

---

## Testing the API

Automated tests are located in the `tests/` folder. Run the tests with:

```bash
python -m unittest discover -s tests
```

This command runs all tests in the `tests/` directory and displays the results in the terminal.

---

## Documentation

The complete API documentation is available in the file:

[OpenAPI-Specification (IFA32).pdf](docs/OpenAPI-Spezifikation%20(IFA32).pdf) (located in the `docs/` folder)

---

## Project Structure

```
TodoListenVerwaltung/
├── README.md
├── requirements.txt
├── docs/
│   └── OpenAPI-Specification (IFA32).pdf
├── app/
│   ├── __init__.py       # Initializes the Flask app, loads configurations, and imports modules
│   ├── config.py         # Contains configuration settings (e.g., debug mode, host, port)
│   ├── main.py           # Entry point to start the server
│   ├── lists.py          # API endpoints for managing to-do lists (retrieve, create, delete)
│   └── todos.py          # API endpoints for managing to-do entries (add, update, delete)
└── tests/
    └── test_api.py       # Test cases for the API endpoints
```

---

## License

This project is licensed under the **Apache 2.0 License**.

---

## Contact

For any questions or suggestions, please contact:

[Y@Musterman.com](Y@Musterman.com)