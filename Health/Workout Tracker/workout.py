class Workout:
    def __init__(self, exercise_name, duration, calories_burned):
        self.exercise_name = exercise_name
        self.duration = duration
        self.calories_burned = calories_burned
        self.intensity = None

    def log_workout(self):
        print(f"Logged Workout: {self.exercise_name} for {self.duration} min,"
              f"burned {self.calories_burned} cal.")

    def update_intensity(self, intensity):
        self.intensity = intensity
        print(f"Intensity for '{self.exercise_name}' set to : {self.intensity}")

    def info(self):
        print("----- Workout Details -----")
        print(f"Exercise       : {self.exercise_name}")
        print(f"Duration       : {self.duration} minutes")
        print(f"Calories Burned: {self.calories_burned} kcal")
        print(f"Intensity      : {self.intensity if self.intensity else '(not set)'}")
        print("---------------------------")

w = Workout("Running", 30, 300)
w.log_workout()                # 🏃 Logged workout: Running for 30 min, burned 300 cal.
w.update_intensity("High")     # ⚡ Intensity for 'Running' set to: High
w.info()
