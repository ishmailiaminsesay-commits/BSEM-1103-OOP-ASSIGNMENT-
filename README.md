<div align="center">

# VaxTrack

### A small, privacy-conscious vaccination record tracker

**PROG211 · Object-Oriented Programming 1 · Individual Assignment**

Built with Python's standard library. No account, network connection, or third-party package is required.

</div>

---

## Overview

VaxTrack is a terminal application for recording a patient's basic profile and latest vaccination status. It demonstrates object creation and interaction, a dictionary of records, instance and class methods, input validation, and privacy-aware design.

The program keeps data in memory only. It asks for a patient ID, name, age, vaccine name, dose date, and vaccination status. It does not request contact details or other sensitive health information, and it does not save records when the session ends.

## Features

- Add a patient and optionally enter vaccination details.
- Find one patient by ID (IDs are normalized to uppercase).
- Record or update the latest vaccination status.
- Display all records and a status summary.
- Validate age, status, and ISO-format dates; future dose dates are rejected.
- Run locally with Python's standard library.

## Requirements

- Python 3.10 or later
- A terminal or command prompt

There are no external dependencies.

## Run the application

From the project directory, run:

```bash
python oop-assignment.py
```

On some systems, the command is `python3 oop-assignment.py`.

## Example session

```text
Welcome to the Vaccination Tracker.
Records remain in memory for this session and are not saved to disk.

VACCINATION TRACKER
1. Add patient
2. Record or update vaccination
3. Find patient
4. Display all patients
5. View summary
0. Exit
Select an option: 1
Patient ID: SL-001
Name: Mariama Kamara
Age (0-120): 24
Patient added.
Add vaccination details now? (y/n): y
Choose status:
  1. Completed
  2. Partially vaccinated
  3. Not vaccinated
Selection: 1
Vaccine name: Example vaccine
Dose date (YYYY-MM-DD): 2026-09-12
Vaccination record updated.

Select an option: 3
Patient ID: sl-001
Patient ID: SL-001
Name: Mariama Kamara
Age: 24
Vaccine: Example vaccine
Dose date: 2026-09-12
Status: Completed
```

The name and sample record above are fictional. This example illustrates the interface; records are not preloaded.

## Object-oriented design

| Assignment concept | Where it appears |
| --- | --- |
| Classes and objects | `Patient` models an individual record; `VaccinationTracker` manages tracker behavior. |
| Attributes | Each `Patient` has an ID, name, age, vaccine name, dose date, and status. |
| Instance methods | `Patient.update_vaccination()` and `Patient.display_info()` operate on a patient object. |
| Class method | `VaccinationTracker.is_valid_status()` checks status against class-level options. |
| Object interaction | The tracker stores `Patient` objects and calls their methods to display and update records. |
| Primary data structure | `VaccinationTracker.patients` is a dictionary keyed by normalized patient ID. |
| Optional tuple extension | `VALID_STATUSES` is a tuple because its allowed status values are fixed. |

## Digital Public Goods alignment

- **Open source:** The source is self-contained and can be published in a public GitHub repository. Choose and include an appropriate open-source license before publishing.
- **Inclusive and accessible:** The application uses a straightforward text menu, clear prompts, and actionable validation messages. It does not depend on color, sound, or a mouse.
- **Privacy respecting:** Only minimal example fields are collected. Data stays in process memory and disappears when the program exits. Do not enter real patient information into this demonstration.
- **Modular and reusable:** The patient model and tracker are separate from the terminal interaction functions, so they can be reused in another interface.

## Project structure

```text
.
├── oop-assignment.py   # Application and OOP model
└── README.md           # Setup, usage, and assignment documentation
```

## Scope and limitations

This is an educational demonstration, not a clinical or production health system. It tracks one latest vaccination entry per patient, stores no data between runs, has no user authentication, and has not been designed for real patient records. A production system would require appropriate security, consent, access controls, durable storage, and clinical review.

## Academic integrity

Use this project as a study aid: read the source, adapt it to your own understanding, and be prepared to explain the classes, dictionary, tuple, and methods. Follow your lecturer's instructions and your university's academic-integrity policy. Update this README with your own student details or repository information if your submission format requires them.

---

**Course:** PROG211 — Object-Oriented Programming 1  
**Assignment:** Real-World Solutions under DPG Standards  
**Language:** Python
