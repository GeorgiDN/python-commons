# Image Folder to Excel Link Generator

This script iterates through folders containing images inside the folder directory and 
generates an Excel file where each folder gets its own sheet. 
Each sheet lists the image filenames, extracts a number from the filenames and creates clickable links that open the corresponding images in the folder.

How it works:
Place your images in separate folders under the main_folder directory.
Run the script, and it will:
Go through each subfolder, create a new Excel sheet for each folder.
For each image in a folder, it will extract the number between "_", list it in the Excel sheet, 
and add a clickable link to the image.
The Excel file has to be on the level of the main folder.
Requirements:
Python 3
openpyxl for Excel manipulation
