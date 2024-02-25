from PIL import Image


# Create logo icon
logo = Image.open('D:\PYTHON_PROJECTS_5\TKINTER_LIBARY\create_logo\Python_logo.png')
logo.save('D:\PYTHON_PROJECTS_5\TKINTER_LIBARY\create_logo\Python_logo.ico', format="ICO")


# Resize Images
image1 = Image.open("Python_logo.png")
image1_resized = image1.resize((300, 300))
image1_resized.save("Python_logo_resized.png")

# Open image
img = Image.open("Python_logo.png")
img.show()

# img2 = Image.open("Python_logo_resized.png")
# img2.show()
