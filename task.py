import customtkinter as ctk
from gui.main_window import Assistant
from utils.logger import botlog
from utils.variables import (
    INFO,
    )

def main():
    botlog("Starting the exercise..", INFO)

    # GUI Initialization
    master = ctk.CTk()
    app = Assistant(master)

    botlog("Launching GUI...", "info")
    master.mainloop()  # Starts the GUI loop


if __name__ == "__main__":
    main()