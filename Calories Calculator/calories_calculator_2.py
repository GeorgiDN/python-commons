from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class Food:
    name: str
    calories: int
    protein: int
    fats: int
    carbs: int


class NutritionTracker:
    CALORIES_GOAL_LIMIT = 3000  # kcal
    PROTEIN_GOAL = 180  # grams
    FAT_GOAL = 80  # grams
    CARBS_GOAL = 300  # grams

    def __init__(self):
        self.today = []

    def add_food_entry(self):
        print("Adding a new food!")
        name = input("Name: ")
        calories = self._take_integer_input("Calories")
        protein = self._take_integer_input("Protein")
        fats = self._take_integer_input("Fats")
        carbs = self._take_integer_input("Carbs")
        food = Food(name, calories, protein, fats, carbs)
        self.today.append(food)
        print(f"The food: '{food.name}' is successfully added!")

    def visualize_progress(self):
        calories_sum = sum(food.calories for food in self.today)
        protein_sum = sum(food.protein for food in self.today)
        fats_sum = sum(food.fats for food in self.today)
        carbs_sum = sum(food.carbs for food in self.today)

        fig, axs = plt.subplots(2, 2)
        axs[0, 0].pie([protein_sum, fats_sum, carbs_sum], labels=["Proteins", "Fats", "Carbs"],
                      autopct=lambda p: f'{p * sum([protein_sum, fats_sum, carbs_sum]) / 100:.0f}')
        axs[0, 0].set_title("Macronutrients Distribution")
        axs[0, 1].bar([0, 1, 2], [protein_sum, fats_sum, carbs_sum], width=0.4)
        axs[0, 1].bar([0.5, 1.5, 2.5], [self.PROTEIN_GOAL, self.FAT_GOAL, self.CARBS_GOAL], width=0.4)
        axs[0, 1].set_title("Macronutrients progress")
        axs[1, 0].pie([calories_sum, self.CALORIES_GOAL_LIMIT - calories_sum], labels=["Calories", "Remaining"],
                      autopct=lambda p: f'{p * sum([calories_sum, self.CALORIES_GOAL_LIMIT - calories_sum]) / 100:.0f}')
        axs[1, 0].set_title("Calories Goal Progress")
        axs[1, 1].plot(list(range(len(self.today))), np.cumsum([food.calories for food in self.today]), label="Calories Eaten")
        axs[1, 1].plot(list(range(len(self.today))), [self.CALORIES_GOAL_LIMIT] * len(self.today), label="Calorie Goal")
        axs[1, 1].legend()
        axs[1, 1].set_title("Calories Goal Over Time")

        fig.tight_layout()
        plt.show()

    # Helper methods
    def _take_integer_input(self, nutrient):
        while True:
            try:
                current_nutrient = int(input(f"{nutrient}: "))
                break
            except ValueError:
                print("Invalid input! Please enter an integer.")
        return current_nutrient


if __name__ == "__main__":
    nutrition_tracker = NutritionTracker()
    done = False

    while not done:
        print("(1) - Add a new food\n"
              "(2) - Visualise the progress\n"
              "(q) - Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            nutrition_tracker.add_food_entry()
        elif choice == "2":
            nutrition_tracker.visualize_progress()
        elif choice.lower() == "q":
            done = True
        else:
            print("Invalid choice")
