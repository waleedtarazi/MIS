import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
window = tk.Tk()
window.title("convert image RGB to HSV and save ")
def input_image():
    global file
    file = filedialog.askopenfilename()
    img = cv2.imread(file)

choose_image = tk.Button(window, text="Choose_image", command=input_image)
choose_image.pack()
def convert_to_hsv():
    img = cv2.imread(file)
    global hsv_img
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(window, image=img)
    panel.image = img
    panel.pack()
convert_for_hsv = tk.Button(window, text="convert orginal to Hsv", command=convert_to_hsv)
convert_for_hsv.pack()
def save_hsvImage():
        save_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        hsv_img_save = Image.fromarray(hsv_img)
        hsv_img_save.save(save_path)
save = tk.Button(window, text="save the modified image ", command=save_hsvImage)
save.pack()
window.mainloop()
