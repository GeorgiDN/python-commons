import os
from PIL import Image

# Define paths
input_folder = 'input_images_folder'  # Folder with the images to process
output_folder = 'output_images_folder'  # Root folder to save images with the logo
logo_path = 'logo.png'  # Path to the logo file

# Load the logo image (without resizing)
logo = Image.open(logo_path).convert("RGBA")

# Define transparency for the logo
alpha = 38  # Adjust the transparency level (0-255)
logo_with_transparency = Image.new("RGBA", logo.size)

# Adjust transparency of the logo
for x in range(logo.width):
    for y in range(logo.height):
        r, g, b, a = logo.getpixel((x, y))
        logo_with_transparency.putpixel((x, y), (r, g, b, int(a * (alpha / 255))))

# Function to process images in a folder and subfolders
def process_folder(input_folder, output_folder):
    # Iterate over the items in the input folder
    for root, dirs, files in os.walk(input_folder):
        # Create the corresponding output folder with "_logo" suffix
        relative_path = os.path.relpath(root, input_folder)
        current_output_folder = os.path.join(output_folder, f"{relative_path}_logo")

        if not os.path.exists(current_output_folder):
            os.makedirs(current_output_folder)

        # Process all images in the current folder
        for filename in files:
            if filename.endswith('.png') or filename.endswith('.jpg'):  # Add more formats if needed
                # Open the background image
                background = Image.open(os.path.join(root, filename)).convert("RGBA")

                # Position the logo (e.g., bottom-right corner)
                position = (background.width - logo_with_transparency.width, background.height - logo_with_transparency.height)

                # Paste the transparent logo onto the background
                background_with_logo = background.copy()
                background_with_logo.paste(logo_with_transparency, position, logo_with_transparency)

                # Save the new image in the output subfolder
                new_filename = f'{filename}'
                background_with_logo.save(os.path.join(current_output_folder, new_filename), format="PNG", dpi=(72, 72))

        # Recursively process subfolders
        for subfolder in dirs:
            subfolder_input = os.path.join(root, subfolder)
            subfolder_output = os.path.join(current_output_folder, f"{subfolder}_logo")
            process_folder(subfolder_input, subfolder_output)

# Start processing the input folder
process_folder(input_folder, output_folder)

print("Logo added to all images and saved in respective folders.")




# import os
# from PIL import Image
#
# # Define paths
# input_folder = 'input_images_folder'  # Folder with the images to process
# output_folder = 'output_images_folder'  # Root folder to save images with the logo
# logo_path = 'logo_4-5.png'  # Path to the logo file
#
# # Load the logo image (without resizing)
# logo = Image.open(logo_path).convert("RGBA")
#
# # Define transparency for the logo
# alpha = 38  # Adjust the transparency level (0-255)
# logo_with_transparency = Image.new("RGBA", logo.size)
#
# # Adjust transparency of the logo
# for x in range(logo.width):
#     for y in range(logo.height):
#         r, g, b, a = logo.getpixel((x, y))
#         logo_with_transparency.putpixel((x, y), (r, g, b, int(a * (alpha / 255))))
#
# # Function to process images in a folder and subfolders
# def process_folder(input_folder, output_folder):
#     # Iterate over the items in the input folder
#     for root, dirs, files in os.walk(input_folder):
#         # Create the corresponding output folder with "_logo" suffix
#         relative_path = os.path.relpath(root, input_folder)
#         current_output_folder = os.path.join(output_folder, f"{relative_path}-s-logo")
#
#         if not os.path.exists(current_output_folder):
#             os.makedirs(current_output_folder)
#
#         # Process all images in the current folder
#         for filename in files:
#             if filename.endswith('.png') or filename.endswith('.jpg'):  # Add more formats if needed
#                 # Open the background image
#                 background = Image.open(os.path.join(root, filename)).convert("RGBA")
#
#                 # Position the logo (e.g., bottom-right corner)
#                 position = (background.width - logo_with_transparency.width, background.height - logo_with_transparency.height)
#
#                 # Paste the transparent logo onto the background
#                 background_with_logo = background.copy()
#                 background_with_logo.paste(logo_with_transparency, position, logo_with_transparency)
#
#                 # Save the new image in the output subfolder
#                 new_filename = f'{filename}-s-logo'
#                 background_with_logo.save(os.path.join(current_output_folder, new_filename), format="PNG", dpi=(72, 72))
#
#         # Recursively process subfolders
#         for subfolder in dirs:
#             subfolder_input = os.path.join(root, subfolder)
#             subfolder_output = os.path.join(current_output_folder, f"{subfolder}-s-logo")
#             process_folder(subfolder_input, subfolder_output)
#
# # Start processing the input folder
# process_folder(input_folder, output_folder)
#
# print("Logo added to all images and saved in respective folders.")
