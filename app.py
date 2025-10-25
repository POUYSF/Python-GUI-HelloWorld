import tkinter as tk
from PIL import Image, ImageTk

def hello():
    label.config(text="Hello, World! 🐍", fg="#009900")


# ایجاد پنجره اصلی
window = tk.Tk()
window.title("Python")
window.geometry("500x350")
window.configure(bg="#c2d6d6")

# افزودن متن Hello World
label = tk.Label(window, text="", font=("", 26, "bold"), bg="#c2d6d6")
label.pack(expand=True)

# افزودن دکمه
button = tk.Button(window, text="Click Me!", font=("Arial", 14, "bold"), fg="gray", bg="#c2d6d6", command=hello)
button.place(relx=0.5, rely=0.85, anchor="center")

# بارگذاری و افزودن لوگو پایین راست
logo = Image.open("Logo.png")
logo = logo.resize((60, 60))
logo_photo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(window, image=logo_photo, bg="#c2d6d6")
logo_label.place(relx=0.95, rely=0.95, anchor="se")



window.mainloop()