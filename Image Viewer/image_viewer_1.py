from tkinter import *
from PIL import Image, ImageTk

# Create logo
# logo = Image.open('D:\PYTHON_PROJECTS_5\TKINTER_LIBARY\icons_imges_exit_buttons\Python-logo.png')
# logo.save('D:\PYTHON_PROJECTS_5\TKINTER_LIBARY\icons_imges_exit_buttons\Python-logo.ico', format="ICO")


# Resize Images
# image1 = Image.open("Python-logo.png")
# image1_resized = image1.resize((300, 300))
# image1_resized.save("Python-logo.png")
#
# image2 = Image.open("Python-logo2.png")
# image2_resized = image2.resize((300, 300))
# image2_resized.save("Python-logo2.png")
#
# image3 = Image.open("Python-logo3.png")
# image3_resized = image3.resize((300, 300))
# image3_resized.save("Python-logo3.png")
#
# image4 = Image.open("Python-logo4.png")
# image4_resized = image4.resize((300, 300))
# image4_resized.save("Python-logo4.png")
#

# image5 = Image.open("Python-logo5.png")
# image5_resized = image5.resize((300, 300))
# image5_resized.save("Python-logo5.png")


root = Tk()
root.title("Python")
root.iconbitmap('D:\PYTHON_PROJECTS_5\TKINTER_LIBARY\icons_imges_exit_buttons\Python-logo.ico')
my_img1 = ImageTk.PhotoImage(Image.open("Python-logo.png"))
my_img2 = ImageTk.PhotoImage(Image.open("Python-logo2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("Python-logo3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("Python-logo4.png"))
my_img5 = ImageTk.PhotoImage(Image.open("Python-logo5.png"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()
