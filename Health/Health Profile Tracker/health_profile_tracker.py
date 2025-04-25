from tkinter.font import names


class HealthProfile:
    def __init__(self, name, age, gender, height, weight, blood_type):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.blood_type = blood_type
        self.blood_pressure = None

    def update_weight(self, new_weight):
        self.weight = new_weight
        print(f"Updated weight to {self.weight} kg.")

    def update_blood_pressure(self, systolic, diastolic):
        self.blood_pressure = (systolic, diastolic)
        print(f"Updated blood pressure to {self.blood_pressure[0]}/ {self.blood_pressure[1]} mmHg.")

    def info(self):
        print("----- Health Profile -----")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Height: {self.height} cm")
        print(f"Weight: {self.weight} kg")
        print(f"Blood Type: {self.blood_type}")
        if self.blood_pressure:
            print(f"Blood Pressure: {self.blood_pressure[0]}/{self.blood_pressure[1]}")
        else:
            print(f"Blood Pressure: Not Available!")

        print("-----------------------------------")

profile = HealthProfile("Peris Kayaro", 26, "Female", 175, 70, "O+")
profile.info()

# Updating weight
profile.update_weight(72)

# Updating blood pressure
profile.update_blood_pressure(120, 80)

# Display updated info
profile.info()

