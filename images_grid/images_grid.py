from PIL import Image, ImageDraw, ImageFont
import os
import math

# Configuration
input_folder = "images"
output_folder = "output"
images_per_page = 16
grid_rows = 4
grid_cols = 4
thumbnail_size = (200, 200)

# Get all image files
image_files = [f for f in os.listdir(input_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
image_files.sort()


os.makedirs(output_folder, exist_ok=True)

# Load font (adjust the font path if needed)
try:
    font = ImageFont.truetype("arial.ttf", 40)
except IOError:
    font = ImageFont.load_default()  # Fallback to default font

# Process images in groups of 16
num_pages = math.ceil(len(image_files) / images_per_page)
global_index = 1  # Global index to track numbering

for i in range(num_pages):
    images = []

    for j in range(images_per_page):
        index = i * images_per_page + j
        if index >= len(image_files):
            break
        img = Image.open(os.path.join(input_folder, image_files[index]))
        img.thumbnail(thumbnail_size)

        # Add numbering
        draw = ImageDraw.Draw(img)
        text = str(global_index)

        # Get text size using textbbox
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Position text in top-left corner with padding
        # position = (5, 5)
        position = ((img.width - text_width) // 2, (img.height - text_height) // 2)
        draw.text(position, text, fill="red", font=font)  # Draw the number in red

        images.append(img)
        global_index += 1  # Increment number

    # Determine final grid size
    page_width = grid_cols * thumbnail_size[0]
    page_height = grid_rows * thumbnail_size[1]
    new_image = Image.new("RGB", (page_width, page_height), "white")

    # Paste images onto the new image
    for row in range(grid_rows):
        for col in range(grid_cols):
            index = row * grid_cols + col
            if index >= len(images):
                break
            x_offset = col * thumbnail_size[0]
            y_offset = row * thumbnail_size[1]
            new_image.paste(images[index], (x_offset, y_offset))

    output_path = os.path.join(output_folder, f"page_{i + 1}.jpg")
    new_image.save(output_path)

print("Images successfully combined into multiple pages with numbering.")
