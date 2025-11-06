import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import pyttsx3
import threading

root = Tk()
root.title("Text to Speech")
root.geometry("900x450+200+100")
root.resizable(False, False)

current_theme = "Light"

# ---------- THEMES ----------
themes = {
    "Light": {
        "bg": "#f5f5f5",
        "frame_bg": "#ffffff",
        "fg": "#222",
        "accent": "#2b6777",
        "button_fg": "white",
        "button_bg": "#2b6777",
        "footer": "#444"
    },
    "Dark": {
        "bg": "#1e1e1e",
        "frame_bg": "#2a2a2a",
        "fg": "#f1f1f1",
        "accent": "#4cc9f0",
        "button_fg": "black",
        "button_bg": "#4cc9f0",
        "footer": "#bbb"
    }
}

# ---------- SPEAK FUNCTION ----------
def speaknow():
    text = text_area.get(1.0, END).strip()
    if not text:
        messagebox.showwarning("Empty Field", "Please enter some text to speak.")
        return

    gender = gender_combobox.get()
    speed = speed_combobox.get()

    def run_speech():
        try:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')

            # Gender selection
            if gender == 'Male':
                engine.setProperty('voice', voices[0].id)
            else:
                engine.setProperty('voice', voices[1].id)

            # Speed setting
            if speed == 'Fast':
                engine.setProperty('rate', 250)
            elif speed == 'Normal':
                engine.setProperty('rate', 150)
            else:
                engine.setProperty('rate', 60)

            engine.say(text)
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            print("Speech Error:", e)

    # Run in separate thread
    threading.Thread(target=run_speech, daemon=True).start()

# ---------- CLEAR FUNCTION ----------
def clear_text():
    text_area.delete(1.0, END)

# ---------- THEME TOGGLE ----------
def toggle_theme():
    global current_theme
    current_theme = "Dark" if current_theme == "Light" else "Light"
    apply_theme()

def apply_theme():
    theme = themes[current_theme]
    root.config(bg=theme["bg"])
    Top_frame.config(bg=theme["frame_bg"])
    text_area.config(bg=theme["bg"], fg=theme["fg"])
    footer_label.config(bg=theme["bg"], fg=theme["footer"])

    speak_button.config(bg=theme["button_bg"], fg=theme["button_fg"])
    clear_button.config(bg=theme["button_bg"], fg=theme["button_fg"])
    theme_button.config(bg=theme["accent"], fg=theme["button_fg"])

    gender_label.config(bg=theme["accent"], fg="white")
    speed_label.config(bg=theme["accent"], fg="white")

# ---------- ICON ----------
image_icon = PhotoImage(file=r"C:\Users\kumar\Downloads\Text To Speach\Text To Speach\Assets\speak.png")
root.iconphoto(False, image_icon)

# ---------- TOP FRAME ----------
Top_frame = Frame(root, bg='white', width=900, height=100)
Top_frame.place(x=0, y=0)

logo = PhotoImage(file=r'C:\Users\kumar\Downloads\Text To Speach\Text To Speach\Assets\speaker logo.png')
Label(Top_frame, image=logo, bg='white').place(x=10, y=5)
Label(Top_frame, text='TEXT TO SPEECH', font='arial 20 bold', bg='white', fg='black').place(x=100, y=30)

# ---------- TEXT AREA ----------
text_area = Text(root, font="Roboto 18", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

# ---------- LABELS ----------
gender_label = Label(root, text='VOICE', font='arial 15 bold', bg='#305065', fg='white')
gender_label.place(x=580, y=160)
speed_label = Label(root, text='SPEED', font='arial 15 bold', bg='#305065', fg='white')
speed_label.place(x=760, y=160)

# ---------- COMBOBOX ----------
gender_combobox = Combobox(root, values=['Male', 'Female'], font='arial 14', state='readonly', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

speed_combobox = Combobox(root, values=['Slow', 'Normal', 'Fast'], font='arial 14', state='readonly', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

# ---------- BUTTONS ----------
speak_button = Button(root, text='Speak',
                    compound=LEFT,
                    image=image_icon,
                    width=130,
                    font='arial 14 bold',
                    command=speaknow)
speak_button.place(x=550, y=280)

clear_icon = PhotoImage(file=r"C:\Users\kumar\Downloads\Text To Speach\Text To Speach\Assets\clear.png")
clear_button = Button(root,
                    text='Clear',
                    compound=LEFT,
                    image =clear_icon,
                    width=130,
                    font='arial 14 bold',
                    command=clear_text)
clear_button.place(x=730, y=280)

theme_button = Button(root, text='Switch Theme', width=28, bg='#2b6777', fg='white', font='arial 12 bold', command=toggle_theme)
theme_button.place(x=550, y=350)

# ---------- FOOTER ----------
footer_label = Label(root, text="Made by Chhavi ❤️", font=('Arial', 10, 'italic'))
footer_label.place(x=720, y=420)

apply_theme()

root.mainloop()
