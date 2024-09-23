from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from project_calculator import excel_file
import tkinter as tk


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
        def insert():
            name = name_field.get()
            calories = float(calories_field.get())
            protein = float(protein_field.get())
            fats = float(fats_field.get())
            carbs = float(carbs_field.get())
            food = Food(name, calories, protein, fats, carbs)
            self.today.append(food)

            # Check for empty name
            if not name.strip():
                print("The name can not be empty!")
                self.today.remove(food)
                return

            # Validate that the sum of entered values does not exceed the goals and if is - remove the food from the list
            if sum(food.calories for food in self.today) > self.CALORIES_GOAL_LIMIT or \
                    sum(food.protein for food in self.today) > self.PROTEIN_GOAL or \
                    sum(food.fats for food in self.today) > self.FATS_GOAL or \
                    sum(food.carbs for food in self.today) > self.CARBS_GOAL:
                print(
                    "Invalid input! The sum of calories, protein, fats, and carbs have not exceeds their corresponding goals.")
                self.view_nutrition_goal_for_the_day()
                self.today.remove(food)
                return

            # Check for negative values
            found_negative_values = self._check_for_negative_values(self.today, "calories", "protein", "fats", "carbs")
            if found_negative_values:
                print("The nutrition values can not be negative!")
                self.today.remove(food)
                return

            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            excel_file.add_food_to_excel(current_time, name, calories, protein, fats, carbs)
            window.destroy()

        window = tk.Tk()
        window.title("Add Food Entry")

        name_label = tk.Label(window, text="Food Name:")
        name_label.grid(row=0, column=0)
        name_field = tk.Entry(window)
        name_field.grid(row=0, column=1)

        calories_label = tk.Label(window, text="Calories:")
        calories_label.grid(row=1, column=0)
        calories_field = tk.Entry(window)
        calories_field.grid(row=1, column=1)

        protein_label = tk.Label(window, text="Protein:")
        protein_label.grid(row=2, column=0)
        protein_field = tk.Entry(window)
        protein_field.grid(row=2, column=1)

        fats_label = tk.Label(window, text="Fats:")
        fats_label.grid(row=3, column=0)
        fats_field = tk.Entry(window)
        fats_field.grid(row=3, column=1)

        carbs_label = tk.Label(window, text="Carbs:")
        carbs_label.grid(row=4, column=0)
        carbs_field = tk.Entry(window)
        carbs_field.grid(row=4, column=1)

        submit_button = tk.Button(window, text="Submit", command=insert)
        submit_button.grid(row=5, column=1)

        window.mainloop()

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
                axs[0, 1].set_xticks([0, 1, 2])
                axs[0, 1].set_xticklabels(["Protein", "Fats", "Carbs"])
                axs[0, 1].bar([0.5, 1.5, 2.5], [self.PROTEIN_GOAL, self.FATS_GOAL, self.CARBS_GOAL], width=0.4)
                axs[0, 1].set_title("Macronutrients progress")
                axs[1, 0].pie([calories_sum, self.CALORIES_GOAL_LIMIT - calories_sum], labels=["Calories", "Remaining"], autopct='%1.1f%%')
                axs[1, 0].set_title("Calories Goal Progress")
                axs[1, 1].plot(list(range(len(self.today))), np.cumsum([food.calories for food in self.today]), label="Calories Eaten")
                axs[1, 1].plot(list(range(len(self.today))), [self.CALORIES_GOAL_LIMIT] * len(self.today), label="Calories Goal")
                axs[1, 1].legend()
                axs[1, 1].set_title("Calories Goal Over Time")

                fig.tight_layout()
                plt.show()
            else:
                print("The progress can not visualise if any macronutrients sum is less than or equal to zero!")

        else:
            print("There is no added information for food yet!")

    def view_food_in_list(self):
        if self.today:
            max_name_length = max(len(food.name) for food in self.today)
            food_data = [
                f"\n[{idx + 1}]. Food name: {food.name.ljust(max_name_length)} || " +
                f"Calories: {str(food.calories).ljust(3)} || " +   # Equal number spaces
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
            index_to_remove = (
                next((index for index, food in enumerate(self.today) if food.name == food_to_remove), None))

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
    @staticmethod
    def _take_number_input(nutrient):
        while True:
            try:
                current_nutrient = float(input(f"{nutrient}: "))
                if current_nutrient >= 0:
                    break
                else:
                    print("Invalid input! Please enter a number greater than or equal to zero!")
            except ValueError:
                print("Invalid input! Please enter a number.")
        return current_nutrient

    @staticmethod
    def _take_input(info):
        while True:
            data = input(f"{info}: ")
            if len(data) > 0:
                break
            else:
                print("Invalid input. The string cannot be empty!")
        return data

    @staticmethod
    def _check_for_negative_values(lst, *nutrients):
        negative_value = next((food for food in lst if any(getattr(food, nutrient) < 0 for nutrient in nutrients)),
                              None)
        return negative_value

    @staticmethod
    def _print_prompt_message():
        pr_message = ''
        pr_message += "---------------Enter your goals!---------------\n"
        pr_message += "The progress can not visualise if any macronutrients sum is less than or equal to zero!"
        return print(pr_message)


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
