import os
import sys

def unlock_guns():
    os.system("cd C:\Users\robee\OneDrive\Documents\Call of Duty\players")
    os.system("echo \"sv_cheats 1\" > config_mp.cfg")
    os.system("echo \"give all\" > config_mp.cfg")
    os.system("echo \"sv_cheats 0\" > config_mp.cfg")

if __name__ == "__main__":
    unlock_guns()
    print("All guns unlocked! Have fun!")
