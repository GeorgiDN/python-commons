# Calories-Calculator
Comprehensive Nutrition Tracker with Visual Progress Visualization and Excel Data Storage

This Python code consists of a Nutrition Tracking System that allows users to track their daily food intake and visualize their progress towards nutrition goals. It includes functionalities to add food entries, visualize progress through graphs, view food entries, remove food entries, and view nutrition goals for the day.

Main Code (calories_calculator_main.py):

Imports necessary libraries including dataclass for defining data structures, numpy for numerical calculations, matplotlib.pyplot for plotting graphs, and datetime for handling date and time.
Defines a Food class using the dataclass decorator to represent food items with attributes such as name, calories, protein, fats, and carbs.
Implements a NutritionTracker class responsible for managing food entries and goals for the day.
Provides methods to add a new food entry, visualize progress through graphs, view food entries, remove food entries, and view nutrition goals for the day.
Uses helper methods to handle user input, print prompt messages, and perform data validation.
Excel File (excel_file.py):

Imports load_workbook from openpyxl for handling Excel files.
Defines functions to create a new Excel sheet and write food data to the Excel sheet.
Includes a function to format the Excel sheet by resizing columns and adding headers.
Utilizes the datetime module to record the time of food entries in the Excel sheet.
Usage:

The main code (calories_calculator_main.py) is executed to create a NutritionTracker instance and provide options for users to interact with the system through a command-line interface.
Users can add food entries, view their progress, visualize data through graphs, remove food entries, and view nutrition goals.
Food data is stored in an Excel file (Food_data.xlsx) using the functions defined in excel_file.py.
Note:

Ensure the Excel file path specified in excel_file.py matches the actual file location on your system.
You may need to install additional libraries such as openpyxl if they are not already installed in your Python environment.

Overall, this code provides a comprehensive solution for tracking nutrition intake and visualizing progress, suitable for individuals seeking to manage their dietary habits.

Also there is a potential areas for future development.
