# Simle Calories-Calculator
Nutrition Tracking System with Visual Progress and Goal Setting

Code Review: Nutrition Tracker in Python

- Initialization:

The program starts by initializing the NutritionTracker class, which sets up the daily nutrition goals for calories, protein, fats, and carbs.

- Menu-Driven Interface:

The code presents a menu-driven interface that allows users to choose various options:

Option 1: Add a new food entry.

Option 2: Visualize the progress of macronutrients and calorie goals.

Option 3: View the list of foods added for the day.

Option 4: Remove a food item from the list.

Option 5: View the set nutrition goals for the day.

Option q: Quit the program.

- Adding a New Food Entry:

Users can add a new food entry by providing details such as name, calories, protein, fats, and carbs.
The code checks if the sum of entered values exceeds the daily nutrition goals. If so, it rejects the entry; otherwise, it adds the entry to the list of foods for the day.

- Visualizing Progress:

This option generates visual representations of nutrition progress:

A pie chart for macronutrient distribution (proteins, fats, carbs).

A bar chart comparing the intake of macronutrients against the daily goals.

A pie chart for calorie goal progress.

A line chart showing calorie consumption over time, comparing it with the calorie goal.

- Viewing Food List:

Users can view a list of foods added for the day, including details such as name, calories, protein, fats, and carbs.

- Removing Food from the List:

Users can remove a specific food item from the list by entering its name.

- Viewing Nutrition Goals:

This option displays the nutrition goals set for the day, including calories, protein, fats, and carbs.

- Data Persistence:

Added food entries are stored in a text file (added_food.txt) with additional information such as the date and time of entry.

- User Input Validation:

The code includes robust input validation, ensuring that users provide valid input and preventing invalid entries.

- Colorama Integration:

The colorama library is used to enhance the visual appeal of the console output, providing color-coded information for better user experience.

Users can exit the program by choosing the quit option ('q').

The code is adaptable and ready for future improvements, making it a solid foundation for expanding features or incorporating additional functionalities
