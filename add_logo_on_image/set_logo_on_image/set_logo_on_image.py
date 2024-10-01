from PIL import Image

# Run - pip install Pillow

# Load the background and logo images (both PNG)
current_image = Image.open('image.jpg').convert("RGBA")
logo = Image.open('logo.jpg').convert("RGBA")


# Resize the logo if needed
# logo = logo.resize((int(background.width * 0.3), int(background.height * 0.3)))

# Adjust transparency of the logo (alpha blending)
alpha = 70  # Desired transparency level (0-255, where 255 is fully opaque)
logo_with_transparency = Image.new("RGBA", logo.size)

# Loop through logo pixels and apply transparency
for x in range(logo.width):
    for y in range(logo.height):
        r, g, b, a = logo.getpixel((x, y))  # Get RGBA values
        logo_with_transparency.putpixel((x, y), (r, g, b, int(a * (alpha / 255))))

# Position the logo (e.g., top-left corner or center)
logo_position = (0, 0)  # (x, y) coordinates for logo placement

# Create a copy of the background to modify
combined_image = current_image.copy()

# Paste the transparent logo onto the background, using the logo's alpha channel as mask
combined_image.paste(logo_with_transparency, logo_position, logo_with_transparency)

# Save the result as a PNG to preserve transparency
combined_image.save('output_image_with_logo.png', format="PNG")

