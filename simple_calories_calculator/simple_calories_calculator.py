from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore, Back, Style, init
from datetime import datetime

init(autoreset=True)


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
        self.CALORIES_GOAL_LIMIT = self._take_number_input("Calories Goal")
        self.PROTEIN_GOAL = self._take_number_input("Protein Goal")
        self.FATS_GOAL = self._take_number_input("Fats Goal")
        self.CARBS_GOAL = self._take_number_input("Carbs Goal")
        self.nutrition_goal_for_the_day["Calories Goal"] = self.CALORIES_GOAL_LIMIT
        self.nutrition_goal_for_the_day["Protein Goal"] = self.PROTEIN_GOAL
        self.nutrition_goal_for_the_day["Fat Goal"] = self.FATS_GOAL
        self.nutrition_goal_for_the_day["Carbs Goal"] = self.CARBS_GOAL

    def add_food_entry(self):
        print("---Adding a new food---")
        name = self._take_input("Name")

        # Check if name is already in the list
        if any(food.name.lower() == name.lower() for food in self.today):
            print(Back.YELLOW + Fore.BLACK + f"The food with the name '{name}' already exists in the list.")
            return

        calories = self._take_number_input("Calories")
        protein = self._take_number_input("Protein")
        fats = self._take_number_input("Fats")
        carbs = self._take_number_input("Carbs")
        food = Food(name, calories, protein, fats, carbs)
        self.today.append(food)

        # Validate that the sum of entered values does not exceed the goals and if is - remove the food from the list
        if sum(food.calories for food in self.today) > self.CALORIES_GOAL_LIMIT or \
                sum(food.protein for food in self.today) > self.PROTEIN_GOAL or \
                sum(food.fats for food in self.today) > self.FATS_GOAL or \
                sum(food.carbs for food in self.today) > self.CARBS_GOAL:
            print(Back.YELLOW + Fore.BLACK + "Invalid input! The sum of calories, protein, fats, and carbs have not exceeds their corresponding goals.")
            self.view_nutrition_goal_for_the_day()
            self.today.remove(food)
            return

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")

        # Write food data in text file
        with open('added_food.txt', "a") as file:
            file.write(f"Date: {current_time} || Food: {name} ||"
                       f"Calories: {calories} || Protein: {protein} || Carbs: {carbs}\n")

        print(Fore.LIGHTGREEN_EX + f"The food: '{Fore.YELLOW + food.name + Fore.RESET + Fore.LIGHTGREEN_EX}' is successfully added!")

    def visualize_progress(self):
        if self.today:
            calories_sum = sum(food.calories for food in self.today)
            protein_sum = sum(food.protein for food in self.today)
            fats_sum = sum(food.fats for food in self.today)
            carbs_sum = sum(food.carbs for food in self.today)

            if calories_sum > 0 and protein_sum > 0 and fats_sum > 0 and carbs_sum > 0:
                fig, axs = plt.subplots(2, 2)
                axs[0, 0].pie([protein_sum, fats_sum, carbs_sum], labels=["Proteins", "Fats", "Carbs"], autopct='%1.1f%%')
                axs[0, 0].set_title("Macronutrients Distribution")
                axs[0, 1].bar([0, 1, 2], [protein_sum, fats_sum, carbs_sum], width=0.4)
                axs[0, 1].bar([0.5, 1.5, 2.5], [self.PROTEIN_GOAL, self.FATS_GOAL, self.CARBS_GOAL], width=0.4)
                axs[0, 1].set_title("Macronutrients progress")
                axs[1, 0].pie([calories_sum, self.CALORIES_GOAL_LIMIT - calories_sum], labels=["Calories", "Remaining"], autopct='%1.1f%%')
                axs[1, 0].set_title("Calories Goal Progress")
                axs[1, 1].plot(list(range(len(self.today))), np.cumsum([food.calories for food in self.today]), label="Calories Eaten")
                axs[1, 1].plot(list(range(len(self.today))), [self.CALORIES_GOAL_LIMIT] * len(self.today), label="Calorie Goal")
                axs[1, 1].legend()
                axs[1, 1].set_title("Calories Goal Over Time")

                fig.tight_layout()
                plt.show()
            else:
                print("The progress can not visualise if any macronutrients sum is less than or equal to zero!")
        else:
            print(Back.YELLOW + Fore.BLACK + "There is no added information for food yet!")

    def view_food_in_list(self):
        if self.today:
            max_name_length = max(len(food.name) for food in self.today)
            food_data = [
                Fore.LIGHTGREEN_EX + f"\n[{idx + 1}]. Food name: {Fore.LIGHTYELLOW_EX + food.name.ljust(max_name_length)} || " + Fore.LIGHTGREEN_EX +
                f"Calories: {Fore.LIGHTYELLOW_EX + str(food.calories).ljust(3)} || " + Fore.LIGHTGREEN_EX +
                f"Proteins: {Fore.LIGHTYELLOW_EX + str(food.protein).ljust(3)} || " + Fore.LIGHTGREEN_EX +
                f"Fats: {Fore.LIGHTYELLOW_EX + str(food.fats).ljust(3)} || " + Fore.LIGHTGREEN_EX +
                f"Carbs: {Fore.LIGHTYELLOW_EX + str(food.carbs).ljust(3)} ||" + Fore.LIGHTGREEN_EX +
                f"\n{Fore.RED + '=' * (max_name_length + 90)}"  # Border line
                for idx, food in enumerate(self.today)
            ]

            return print(f"The food\s in today list: {''.join(food_data)}")
        else:
            return print(Back.YELLOW + Fore.BLACK + "There is no food in the list!")

    def remove_food_from_list(self):
        self.view_food_in_list()
        if self.today:
            food_to_remove = self._take_input("Enter the name of the food which you want to remove!")
            # Find the index of the food with the given name
            index_to_remove = next((index for index, food in enumerate(self.today) if food.name == food_to_remove), None)

            if index_to_remove is not None:
                removed_food = self.today.pop(index_to_remove)
                print(
                    Fore.LIGHTGREEN_EX + f"Removed food: {Fore.YELLOW + removed_food.name + Fore.RESET + Fore.LIGHTGREEN_EX}")
                self.view_food_in_list()
            else:
                print(Back.YELLOW + Fore.BLACK + f"There is no food in the list with the name {food_to_remove}")

    def view_nutrition_goal_for_the_day(self):
        max_nutrient_length = max(len(nutrient) for nutrient in self.nutrition_goal_for_the_day)

        print(f"---Nutrition goal for the day---")
        for nut, val in self.nutrition_goal_for_the_day.items():
            formatted_nutrient = Fore.LIGHTGREEN_EX + f"{nut}:".ljust(max_nutrient_length + 1)
            formatted_value = Fore.LIGHTYELLOW_EX + f"{val}"

            print(f"{formatted_nutrient} {formatted_value}")

    # Helper methods
    def _take_number_input(self, nutrient):
        while True:
            try:
                current_nutrient = float(input(Fore.LIGHTCYAN_EX + f"{nutrient}: "))
                if current_nutrient >= 0:
                    break
                else:
                    print(Back.YELLOW + Fore.BLACK + "Invalid input! Please enter a number greater than zero!")
            except ValueError:
                print(Back.YELLOW + Fore.BLACK + "Invalid input! Please enter an integer.")
        return current_nutrient

    def _take_input(self, info):
        while True:
            data = input(f"{info}: ")
            if len(data) > 0:
                break
            else:
                print(Back.YELLOW + Fore.BLACK + "Invalid input. The string cannot be empty!")
        return data

    def _print_prompt_message(self):
        pr_message = ''
        pr_message += "---------------Enter your goals!---------------\n"
        pr_message += "The progress can not visualise if any macronutrients sum is less than or equal to zero!"
        return print(pr_message)


if __name__ == "__main__":
    nutrition_tracker = NutritionTracker()
    done = False

    while not done:
        print(Fore.RED + "__" * 80)
        print(Fore.LIGHTBLUE_EX + "==== Calories Calculator Options ====\n" + Fore.MAGENTA +
              "(1) - Add a new food\n"
              "(2) - Visualise the progress\n"
              "(3) - View food in the list\n"
              "(4) - Remove food from the list\n"
              "(5) - View nutrition goal for the day\n"
              "(q) - Quit")
        print(Fore.RED + "__" * 80)
        choice = input(Fore.LIGHTCYAN_EX + "Choose an option: ")

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
            print(Back.YELLOW + Fore.BLACK + "Invalid choice!")
