class FoodItem:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def displayinfo(self):
        print(f"Rodzaj jedzenia {self.name}, Kalorie: {self.calories} kcal")

class Meal:
    def __init__(self, name):
        self.name = name
        self.fooditems = []

    def add_food(self, food):
        self.fooditems.append(food)

    def get_total_calories(self):
        return sum(food.calories for food in self.fooditems)

    def display_meal_info(self):
        print(f"\nPosilek: {self.name}")
        print("Skladniki")
        for food in self.fooditems:
            food.displayinfo()
        print(f"Lacznie: {self.get_total_calories()} kcal\n")

class DailyIntake:
    def __init__(self):
        self.meals = []

    def add_meal(self, meal):
        self.meals.append(meal)

    def get_daily_calories(self):
        return sum(meal.get_total_calories() for meal in self.meals)

    def display_daily_summary(self):
        print("\nPODSUMOWANIE DNIA")
        for meal in self.meals:
            meal.display_meal_info()
        print(f"RAZEM DZISIAJ: {self.get_daily_calories()} kcal")

if __name__ == "__main__":
    banana = FoodItem("Banan", 105)
    oatmeal = FoodItem("Owsianka", 150)
    chicken = FoodItem("Kurczak", 200)
    bread = FoodItem("Chleb", 50)

    breakfast = Meal("Sniadanie")
    breakfast.add_food(banana)
    breakfast.add_food(oatmeal)
    breakfast.add_food(bread)

    dinner = Meal("Obiad")
    dinner.add_food(chicken)

    today = DailyIntake()
    today.add_meal(breakfast)
    today.add_meal(dinner)

    today.display_daily_summary()