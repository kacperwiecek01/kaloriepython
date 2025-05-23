class FoodItem:
    def __init__(self, name, calories):
        self.name = name
        self.Calories = calories

    def display_info(self):
        print(f"Jedzenie: {self.name}, Kalorie{self.Calories} kcal")

class Meal:
    def __init__(self, name):
        self.name = name
        self.fooditems = []

    def add_food(self, food):
        self.fooditems.append(food)

    def display_meal_info(self):
        print(f"Posi³ek: {self.name}")
        print("Sk³adniki:")
        for food in self.fooditems:
            food.display_info()
        print(f"£¹czenie: {self.get_total_calories()} kcal\n")

class DailyIntake:
    def __init__(self):
        self.Meals = []

    def add_meal(self, meal):
        self.Meals.append(meal)

    def get_daily_calories(self):
        return sum(meal.get_total_calories() for meal in self.Meals)

    def display_daily_summary(self):
        print("PODSUMOWANIE DNIA")
        for meal in self.Meals:
            meal.display_meal_info()
        print(f"RAZEM DZIŒ: {self.get_daily_calories()} kcal")