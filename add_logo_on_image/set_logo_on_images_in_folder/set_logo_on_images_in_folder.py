import os
from PIL import Image


# Run - pip install Pillow

# Without Resize
# Define paths
input_folder = 'input_images_folder'  # Folder with the images to process
output_folder = 'output_images_folder'  # Folder to save images with the logo
logo_path = 'logo.jpg'  # Path to the logo file

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

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.png') or filename.endswith('.jpg'):  # Add more formats if needed
        # Open the background image
        background = Image.open(os.path.join(input_folder, filename)).convert("RGBA")

        # Use the logo's original size without resizing
        # Position the logo (e.g., bottom-right corner)
        position = (background.width - logo_with_transparency.width, background.height - logo_with_transparency.height)

        # Paste the transparent logo onto the background
        background_with_logo = background.copy()
        background_with_logo.paste(logo_with_transparency, position, logo_with_transparency)

        # Save the new image in the output folder
        new_filename = f'logo_{filename}'
        # background_with_logo.save(os.path.join(output_folder, new_filename), format="PNG")
        background_with_logo.save(os.path.join(output_folder, new_filename), format="PNG", dpi=(72, 72))

print("Logo added to all images and saved.")




#  With Resize

# import os
# from PIL import Image
#
# # Define paths
# input_folder = 'input_images_folder'  # Folder with the images to process
# output_folder = 'output_images_folder'  # Folder to save images with the logo
# logo_path = 'logo.png'  # Path to the logo file
#
# # Load the logo image
# logo = Image.open(logo_path).convert("RGBA")
#
# # Define transparency for the logo
# alpha = 150  # Adjust the transparency level (0-255)
# logo_with_transparency = Image.new("RGBA", logo.size)
#
# # Adjust transparency of the logo
# for x in range(logo.width):
#     for y in range(logo.height):
#         r, g, b, a = logo.getpixel((x, y))
#         logo_with_transparency.putpixel((x, y), (r, g, b, int(a * (alpha / 255))))
#
# # Ensure the output folder exists
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#
# # Process each image in the input folder
# for filename in os.listdir(input_folder):
#     if filename.endswith('.png') or filename.endswith('.jpg'):  # Add more formats if needed
#         # Open the background image
#         background = Image.open(os.path.join(input_folder, filename)).convert("RGBA")
#
#         # Resize logo to fit the background (optional, adjust as needed)
#         resized_logo = logo_with_transparency.resize((int(background.width * 0.3), int(background.height * 0.3)))
#
#         # Position the logo (e.g., bottom-right corner)
#         position = (background.width - resized_logo.width, background.height - resized_logo.height)
#
#         # Paste the transparent logo onto the background
#         background_with_logo = background.copy()
#         background_with_logo.paste(resized_logo, position, resized_logo)
#
#         # Save the new image in the output folder
#         new_filename = f'logo_{filename}'
#         background_with_logo.save(os.path.join(output_folder, new_filename), format="PNG")
#
# print("Logo added to all images and saved.")
