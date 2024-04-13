from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

@dataclass
class Food:
    name: str
    calories: float
    protein: float
    fats: float
    carbs: float


class NutritionTracker:

    def __init__(self):
        self.today = []
        self.nutrition_goal_for_the_day = {"Calories Goal": 0, "Protein Goal": 0, "Fat Goal": 0, "Carbs Goal": 0}
        self._print_prompt_message()
        self.CALORIES_GOAL_LIMIT = self._take_integer_input("Calories Goal")
        self.PROTEIN_GOAL = self._take_integer_input("Protein Goal")
        self.FATS_GOAL = self._take_integer_input("Fats Goal")
        self.CARBS_GOAL = self._take_integer_input("Carbs Goal")
        self.nutrition_goal_for_the_day["Calories Goal"] = self.CALORIES_GOAL_LIMIT
        self.nutrition_goal_for_the_day["Protein Goal"] = self.PROTEIN_GOAL
        self.nutrition_goal_for_the_day["Fat Goal"] = self.FATS_GOAL
        self.nutrition_goal_for_the_day["Carbs Goal"] = self.CARBS_GOAL

    def add_food_entry(self):
        print("---Adding a new food---")
        name = self._take_input("Name")

        # Check if name is already in the list
        if any(food.name.lower() == name.lower() for food in self.today):
            print(f"The food with the name '{name}' already exists in the list.")
            return

        calories = self._take_integer_input("Calories")
        protein = self._take_integer_input("Protein")
        fats = self._take_integer_input("Fats")
        carbs = self._take_integer_input("Carbs")
        food = Food(name, calories, protein, fats, carbs)
        self.today.append(food)

        # Validate that the sum of entered values does not exceed the goals and if is - remove the food from the list
        if sum(food.calories for food in self.today) > self.CALORIES_GOAL_LIMIT or \
                sum(food.protein for food in self.today) > self.PROTEIN_GOAL or \
                sum(food.fats for food in self.today) > self.FATS_GOAL or \
                sum(food.carbs for food in self.today) > self.CARBS_GOAL:
            print("Invalid input! The sum of calories, protein, fats, and carbs have not exceeds their corresponding goals.")
            self.view_nutrition_goal_for_the_day()
            self.today.remove(food)
            return

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")

        # Write food data in text file
        with open('added_food.txt', "a") as file:
            file.write(f"Date: {current_time} || Food: {name} ||"
                       f"Calories: {calories} || Protein: {protein} || Carbs: {carbs}\n")

        print(f"The food: '{food.name}' is successfully added!")

    def visualize_progress(self):
        if self.today:
            calories_sum = sum(food.calories for food in self.today)
            protein_sum = sum(food.protein for food in self.today)
            fats_sum = sum(food.fats for food in self.today)
            carbs_sum = sum(food.carbs for food in self.today)

            fig, axs = plt.subplots(2, 2)
            axs[0, 0].pie([protein_sum, fats_sum, carbs_sum], labels=["Proteins", "Fats", "Carbs"],
                          autopct=lambda p: f'{p * sum([protein_sum, fats_sum, carbs_sum]) / 100:.0f}')
            axs[0, 0].set_title("Macronutrients Distribution")
            axs[0, 1].bar([0, 1, 2], [protein_sum, fats_sum, carbs_sum], width=0.4)
            axs[0, 1].bar([0.5, 1.5, 2.5], [self.PROTEIN_GOAL, self.FATS_GOAL, self.CARBS_GOAL], width=0.4)
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
        else:
            print("There is no added information for food yet!")

    def view_food_in_list(self):
        if self.today:
            max_name_length = max(len(food.name) for food in self.today)
            food_data = [
                f"\n[{idx + 1}]. Food name: {food.name.ljust(max_name_length)} || " +
                f"Calories: {str(food.calories).ljust(3)} || " +
                f"Proteins: {str(food.protein).ljust(3)} || " +
                f"Fats: {str(food.fats).ljust(3)} || " +
                f"Carbs: {str(food.carbs).ljust(3)} ||" +
                f"\n{'=' * (max_name_length + 90)}"  # Border line
                for idx, food in enumerate(self.today)
            ]

            return print(f"The food in today list: {''.join(food_data)}")
        else:
            return print("There is no food in the list!")

    def remove_food_from_list(self):
        self.view_food_in_list()
        if self.today:
            food_to_remove = self._take_input("Enter the name of the food which you want to remove!")
            # Find the index of the food with the given name
            index_to_remove = next((index for index, food in enumerate(self.today) if food.name == food_to_remove), None)

            if index_to_remove is not None:
                removed_food = self.today.pop(index_to_remove)
                print(f"Removed food: {removed_food.name}")
                self.view_food_in_list()
            else:
                print(f"There is no food in the list with the name {food_to_remove}")

    def view_nutrition_goal_for_the_day(self):
        max_nutrient_length = max(len(nutrient) for nutrient in self.nutrition_goal_for_the_day)

        print("---Nutrition goal for the day---")
        for nut, val in self.nutrition_goal_for_the_day.items():
            formatted_nutrient = f"{nut}:".ljust(max_nutrient_length + 1)
            formatted_value = f"{val}"

            print(f"{formatted_nutrient} {formatted_value}")

    # Helper methods
    def _take_integer_input(self, nutrient):
        while True:
            try:
                current_nutrient = float(input(f"{nutrient}: "))
                if current_nutrient > 0:
                    break
                else:
                    print("Invalid input! Please enter a number greater than zero!")
            except ValueError:
                print("Invalid input! Please enter an integer.")
        return current_nutrient

    def _take_input(self, info):
        while True:
            data = input(f"{info}: ")
            if len(data) > 0:
                break
            else:
                print("Invalid input. The string cannot be empty!")
        return data

    def _print_prompt_message(self):
        return print("---------------Enter your goals!---------------\n")


if __name__ == "__main__":
    nutrition_tracker = NutritionTracker()
    done = False

    while not done:
        print("=" * 80)
        print("==== Calories Calculator Options ====")
        print("(1) - Add a new food")
        print("(2) - Visualise the progress")
        print("(3) - View food in the list")
        print("(4) - Remove food from the list")
        print("(5) - View nutrition goal for the day")
        print("(q) - Quit")
        print("=" * 80)
        choice = input("Choose an option: ")

        if choice == "1":
            nutrition_tracker.add_food_entry()
        elif choice == "2":
            nutrition_tracker.visualize_progress()
        elif choice == "3":
            nutrition_tracker.view_food_in_list()
        elif choice == "4":
            nutrition_tracker.remove_food_from_list()
        elif choice == "5":
            nutrition_tracker.view_nutrition_goal_for_the_day()
        elif choice.lower() == "q":
            done = True
        else:
            print("Invalid choice!")
