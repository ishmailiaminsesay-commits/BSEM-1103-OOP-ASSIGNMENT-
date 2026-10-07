"""A privacy-conscious, in-memory vaccination record tracker.

Created as an Object-Oriented Programming 1 assignment project.
Run with: python oop-assignment.py
"""

from datetime import date


class Patient:
    """A minimal patient profile and its latest vaccination record."""

    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.vaccine_name = "Not recorded"
        self.dose_date = "Not recorded"
        self.status = "Not vaccinated"

    def update_vaccination(self, vaccine_name, dose_date, status):
        """Replace this patient's latest vaccination details."""
        self.vaccine_name = vaccine_name
        self.dose_date = dose_date
        self.status = status

    def display_info(self):
        """Return a readable summary without exposing extra personal data."""
        return (
            f"Patient ID: {self.patient_id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Vaccine: {self.vaccine_name}\n"
            f"Dose date: {self.dose_date}\n"
            f"Status: {self.status}"
        )


class VaccinationTracker:
    """Manage patient objects in a dictionary indexed by unique patient ID."""

    # Immutable options: this tuple demonstrates the optional tuple extension.
    VALID_STATUSES = ("Completed", "Partially vaccinated", "Not vaccinated")

    def __init__(self):
        self.patients = {}

    @classmethod
    def is_valid_status(cls, status):
        """Check a status against the tracker's approved status options."""
        return status in cls.VALID_STATUSES

    @staticmethod
    def normalize_patient_id(patient_id):
        """Normalize IDs so lookups are case-insensitive and whitespace-safe."""
        return patient_id.strip().upper()

    def add_patient(self, patient):
        """Store a Patient object; return False when its ID already exists."""
        patient_id = self.normalize_patient_id(patient.patient_id)
        if not patient_id or patient_id in self.patients:
            return False
        patient.patient_id = patient_id
        self.patients[patient_id] = patient
        return True

    def find_patient(self, patient_id):
        """Find one patient by ID, ignoring letter case and surrounding spaces."""
        return self.patients.get(self.normalize_patient_id(patient_id))

    def display_all_patients(self):
        """Return summaries for all records in insertion order."""
        if not self.patients:
            return "No patient records have been added yet."
        summaries = ""
        for patient in self.patients.values():
            if summaries:
                summaries += "\n\n\n\n"
            summaries += patient.display_info()
        return summaries

    def update_vaccination(self, patient_id, vaccine_name, dose_date, status):
        """Update a patient's latest vaccination record after input validation."""
        patient = self.find_patient(patient_id)
        if patient is None or not self.is_valid_status(status):
            return False
        patient.update_vaccination(vaccine_name.strip(), dose_date, status)
        return True

    def get_summary(self):
        """Count patients by vaccination status."""
        completed = 0
        partially_vaccinated = 0
        not_vaccinated = 0
        for patient in self.patients.values():
            if patient.status == "Completed":
                completed += 1
            elif patient.status == "Partially vaccinated":
                partially_vaccinated += 1
            else:
                not_vaccinated += 1
        summary = f"Total patient records: {len(self.patients)}"
        summary += f"\nCompleted: {completed}"
        summary += f"\nPartially vaccinated: {partially_vaccinated}"
        summary += f"\nNot vaccinated: {not_vaccinated}"
        return summary


def read_non_empty(prompt):
    """Prompt until the user enters a non-empty value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a value.")


def read_age():
    """Prompt for an age in the supported range."""
    while True:
        value = input("Age (0-120): ").strip()
        try:
            age = int(value)
            if 0 <= age <= 120:
                return age
        except ValueError:
            pass
        print("Enter a whole number from 0 to 120.")


def read_date():
    """Prompt for a real calendar date in ISO YYYY-MM-DD format."""
    while True:
        value = input("Dose date (YYYY-MM-DD): ").strip()
        try:
            parsed_date = date.fromisoformat(value)
            if parsed_date > date.today():
                print("Dose date cannot be in the future.")
                continue
            return parsed_date.isoformat()
        except ValueError:
            print("Enter a valid date in YYYY-MM-DD format.")


def read_status():
    """Display and collect one of the approved vaccination statuses."""
    while True:
        print("Choose status:")
        for number, status in enumerate(VaccinationTracker.VALID_STATUSES, start=1):
            print(f"  {number}. {status}")
        choice = input("Selection: ").strip()
        try:
            selection = int(choice)
            if 1 <= selection <= len(VaccinationTracker.VALID_STATUSES):
                status = VaccinationTracker.VALID_STATUSES[selection - 1]
                if VaccinationTracker.is_valid_status(status):
                    return status
        except (ValueError, IndexError):
            pass
        print("Choose one of the listed numbers.")


def add_patient_flow(tracker):
    """Collect and add a patient, then optionally attach vaccination details."""
    patient_id = read_non_empty("\n\nPatient ID: ")
    name = read_non_empty("Name: ")
    age = read_age()
    patient = Patient(patient_id, name, age)
    if not tracker.add_patient(patient):
        print("That patient ID is already in use.")
        return
    print("Patient added.")
    if input("Add vaccination details now? (y/n): ").strip().lower() == "y":
        record_vaccination_flow(tracker, patient.patient_id)


def record_vaccination_flow(tracker, patient_id=None):
    """Collect vaccination details for an existing patient."""
    if patient_id is None:
        patient_id = read_non_empty("Patient ID: ")
    patient = tracker.find_patient(patient_id)
    if patient is None:
        print("No patient was found with that ID.")
        return

    status = read_status()
    if status == "Not vaccinated":
        vaccine_name = "Not recorded"
        dose_date = "Not recorded"
    else:
        vaccine_name = read_non_empty("Vaccine name: ")
        dose_date = read_date()

    tracker.update_vaccination(patient.patient_id, vaccine_name, dose_date, status)
    print("Vaccination record updated.")


def show_patient_flow(tracker):
    """Find and display one patient record."""
    patient = tracker.find_patient(read_non_empty("Patient ID: "))
    if patient is None:
        print("No patient was found with that ID.")
    else:
        print(patient.display_info())


def show_menu():
    """Print the main menu."""
    print("\nVACCINATION TRACKER")
    print("1. Add patient")
    print("2. Record or update vaccination")
    print("3. Find patient")
    print("4. Display all patients")
    print("5. View summary")
    print("0. Exit")


def main():
    """Run the interactive application."""
    tracker = VaccinationTracker()
    print("Welcome to the Vaccination Tracker.")
    print("Records remain in memory for this session and are not saved to disk.")
    while True:
        show_menu()
        choice = input("Select an option: ").strip()
        if choice == "0":
            print("Session ended. No records were saved.")
            break
        if choice == "1":
            add_patient_flow(tracker)
        elif choice == "2":
            record_vaccination_flow(tracker)
        elif choice == "3":
            show_patient_flow(tracker)
        elif choice == "4":
            print(tracker.display_all_patients())
        elif choice == "5":
            print(tracker.get_summary())
        else:
            print("Choose a number from 0 to 5.")


if __name__ == "__main__":
    main()
