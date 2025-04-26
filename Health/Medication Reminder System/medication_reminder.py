class MedicationReminder:
    def __init__(self, medication_name,dosage,time_of_day):
        self.medication_name = medication_name
        self.dosage = dosage
        self.time_of_day = time_of_day
        self.reminder_set = False


    def set_reminder(self, new_time_of_day):
       self.time_of_day = new_time_of_day
       self.reminder_set = True
       print(f"Reminder set for {self.medication_name} at {self.time_of_day}.")

    def update_dosage(self, new_dosage):
       self.dosage = new_dosage
       print(f"Dosage for {self.medication_name} updated to {self.dosage}.")


    def info(self):
        """Display the medication reminder information."""
        print("----- Medication Reminder -----")
        print(f"Medication: {self.medication_name}")
        print(f"Dosage: {self.dosage}")
        print(f"Time of Day: {self.time_of_day}")
        print(f"Reminder Set: {self.reminder_set}")
        print("--------------------------------")


# Create a reminder
reminder = MedicationReminder("Vitamin D", "5000 IU", "8:00 AM")
reminder.info()

# Set a new reminder time
reminder.set_reminder("9:00 AM")

# Update the dosage
reminder.update_dosage("6000 IU")

# Display updated info
reminder.info()
