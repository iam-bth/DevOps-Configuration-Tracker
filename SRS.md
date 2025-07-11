# Software Requirement Specification (SRS)
## Project: DevOps Configuration Tracker
**Author:** Bhuvan T H
**Date:** July 2025
**Version:** 1.0

---

## 1. Introduction

### 1.1 Purpose
This project is a command-line tool called **DevOps Configuration Tracker**, developed using Python. Its purpose is to allow teams to add, view, update, delete and search configuration items used in software development across **Development**, **Staging**, and **Production** environments.

### 1.2 Intended Audience
- Software Engineers
- DevOps Engineers
- Recruiters reviewing the project
- Beginners learning Python and software configuration

### 1.3 Scope
This system allows tracking of configuration items with:
- Name
- Version
- Environment (Dev, Staging, Prod)
- Status (Active, Inactive)

all data is stored in a JSON file, and the interface is entirely CLI-based for simplicity and portability.

---

## 2. Overall Description

### 2.1 Product Perspective
This is a **Standalone tool** with no external dependencies except Python standard library. It runs in the terminal and does not require any GUI or database.

### 2.2 Product Features
- Add configuration items
- View list of all config items
- Update item status
- Delete items with confirmation
- Search for items by name
- Persist data in a JSON file

### 2.3 User Characteristics
- Familiarity with using a terminal or command prompt.
- Basic understanding of configuration items in software development.

### 2.4 Constraints
- Runs in command-line only (no GUI)
- All data is stored in a local JSON file (no cloud/database)

### 2.5 Assumptions and Dependencies
- Python 3.x must be installed.
- User runs the program via terminal or VS Code.

---

## 3. System Features and Requirements

### 3.1 Functional Requirements

#### FR1: Add Configuration Item
- User inputs: name, version, environment, status.
- System appends to the list and saves to JSON.

#### FR2: View Configuration Items
- Display all saved config items with details.

#### FR3: Update Item Status
- Change status from Active ↔ Inactive.

#### FR4: Delete Configuration Item
- User selects by index.
- Confirm deletion before removing.

#### FR5: Search Configuration Items
- Filter by name (case-insensitive match).

#### FR6: Persistent Storage
- All changes saved in `config_items.json` using JSON format.

### 3.2 Non-Functional Requirements

#### NFR1: Usability
- Simple text-based interface.
- Easy to use with numbered options.

#### NFR2: Reliability
- Program handles invalid inputs gracefully.

#### NFR3: Maintainability
- Code is modular with separation of logic (OOP).

#### NFR4: Portability
- Runs on any system with Python installed.

#### NFR5: Performance
- App performs CRUD operations instantly for small to medium datasets.

---

## 4. External Interface Requirements

### 4.1 User Interface
- Command-line input and output.

### 4.2 Hardware Interface
- Any system with Python 3 installed.

### 4.3 Software Interface
- Python Standard Library: `json`, `os`, `input`, `print`.

---

## 5. Future Enhancements

- Export reports to CSV or Excel
- Add timestamp for config creation
- Filter by environment or status
- Add login system (basic auth)
- Create a GUI using Tkinter or Flask

---

## 6. Appendix

### 6.1 Definitions
- **Configuration Item (CI):** A software setting, file, or environment variable required for deployment.
- **Environment:** Where the software runs (Dev, Staging, Prod).
- **Status:** Indicates if a configuration is currently being (Active) or not (Inactive).

---
## 🔗 Project Repository

👉 [View on GitHub](https://github.com/iam-bth/DevOps-Configuration-Tracker)

