import customtkinter as ctk
from utils.variables import (
    LOG_DIR,
    LOG_FILE,
    INFO,
    DEBUG,
    WARNING,
    ERROR,
    CRITICAL
    )




def create_label(parent, text, font=("Helvetica", 20, "bold"), color="#ffffff",anchor="center"):
    label = ctk.CTkLabel(
        parent,
        text=text,
        text_color=color,
        font=font,
        anchor=anchor
    )
    return label

def create_button(parent, text, command,font=("Arial", 14), state="normal", width=150, height=40):
    button = ctk.CTkButton(
        parent,
        text=text,
        command=command,
        fg_color="#0039de",
        hover_color="#357ab8",
        text_color="white",
        font=font,
        corner_radius=8,
        width=width,
        height=height,
        state=state
    )
    return button

def create_progress_bar(parent, width=250):
    """Creates and returns a CustomTkinter Progress Bar widget."""
    progress = ctk.CTkProgressBar(parent, width=width)
    progress.set(0)  # Initialize to 0%
    return progress
