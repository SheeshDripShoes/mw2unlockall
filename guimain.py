import os
import tkinter as tk

def unlock_guns():
    os.system("cd C:/Program Files (x86)/Activision/Call of Duty Modern Warfare 2/players")
    os.system("echo \"sv_cheats 1\" > config_mp.cfg")
    os.system("echo \"give all\" > config_mp.cfg")
    os.system("echo \"sv_cheats 0\" > config_mp.cfg")

def button_clicked():
    unlock_guns()
    result_label.config(text="All guns unlocked!", fg="purple")

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Modern Warfare 2 Unlock All")
    window.geometry("300x100")
