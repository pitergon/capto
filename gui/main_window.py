import os 
import customtkinter as ctk
import threading
import time
from tkinter import filedialog, messagebox
from utils.logger import botlog
from gui.widgets import create_label, create_button, create_progress_bar
from utils.variables import (
    INFO,
    DEBUG,
    ERROR,
    )

from services.document_processor import process_document


ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
ctk.set_window_scaling(1.0)
ctk.deactivate_automatic_dpi_awareness()



class Assistant:
    def __init__(self, master):
        self.master = master
        self.master.title("Excercise Robot")
        self.master.iconbitmap("Images/capto.ico")  # Add icon
        
        # Center the window
        window_width = 440
        window_height = 640
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)
        self.master.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
        self.master.configure(bg="#1a1c1e")  # Set dark background

        # Initialize variables
        self.selected_files = None  # Store selected file

        # Create UI Elements
        self.create_gui()
    
    def create_gui(self):
        # Set column weight for centering
        self.master.grid_columnconfigure(0, weight=1)  # Makes the single column expand

        # Title Label
        self.title_label = create_label(self.master, "Welcome to Excercise Robot")
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ns")

        # Information Label
        self.information_label = create_label(self.master, "Please upload PDF or .docx file!", font=("Helvetica", 14, "normal"))
        self.information_label.grid(row=1, column=0, padx=20, pady=25, sticky="ns")

        # File Selection Button
        self.start_button = create_button(self.master, "Upload File", self.upload_file)
        self.start_button.grid(row=2, column=0, padx=20, pady=5, sticky="ns")

        # Status Label
        self.status_label = create_label(self.master, "No file selected", font=("Helvetica", 12, "normal"), color="gray")
        self.status_label.grid(row=3, column=0, padx=20, pady=5, sticky="ns")

        # Process Label (Initially Hidden)
        self.process_label = create_label(self.master, "Please wait while processing..", font=("Helvetica", 12, "normal"), color="white")
        self.process_label.grid(row=5, column=0, padx=20, pady=10, sticky="ns")
        self.process_label.grid_remove()  # Hide initially

        # Progress Bar (Initially Hidden)
        self.progress = create_progress_bar(self.master)
        self.progress.grid(row=6, column=0, padx=20, pady=10, sticky="ns")
        self.progress.grid_remove()  # Hide initially

        # Process Button (Initially Disabled)
        self.submit_btn = create_button(self.master, "Process File", self.process_file, state="disabled")
        self.submit_btn.grid(row=7, column=0, padx=20, pady=20, sticky="ns")

    def show_progress_bar(self):
        """Show the progress bar in the UI."""
        self.process_label.grid()
        self.progress.grid()  
        self.progress.set(0.2) 

    def hide_progress_bar(self):
        """Hide the progress bar after processing is done."""
        self.progress.grid_remove() 
        self.process_label.grid_remove()

    def hide_main_widgets(self):
        """Hides all widgets except the title label & progress bar."""
        self.widgets_to_hide = [
            self.information_label, self.start_button, self.status_label, self.submit_btn
        ]

        for widget in self.widgets_to_hide:
            widget.grid_remove() 

    def show_main_widgets(self):
        """Restores the main UI after processing is done."""
        for widget in self.widgets_to_hide:
            widget.grid() 

        self.hide_progress_bar()   

    def reset_ui(self):
        """Resets the UI to allow uploading a new file."""
        self.selected_file = None
        self.status_label.configure(text="No file selected", text_color="gray") 
        self.submit_btn.configure(state="disabled")  
        
        self.show_main_widgets() 

    def upload_file(self):
        """Allows user to select additional files without losing previously selected ones."""
        new_file_paths = filedialog.askopenfilenames(
            title="Select Files",
            filetypes=[("PDF Files", "*.pdf"), ("Word Documents", "*.docx")],
        )

        if new_file_paths:  
            if not hasattr(self, 'selected_files') or self.selected_files is None:
                self.selected_files = []

            # Append new files without duplicating
            for file in new_file_paths:
                if file not in self.selected_files:
                    self.selected_files.append(file)

            
            file_names = "\n".join([file.split("/")[-1] for file in self.selected_files])

            # Update status label
            self.status_label.configure(text=f"Selected Files:\n{file_names}", text_color="white", justify="left")

            self.submit_btn.configure(state="normal")
            botlog(f"User added more files: {self.selected_files}", "info")
        else:
            botlog("User canceled file selection.", "info")

    def process_file(self):
        """Function for processing the uploaded file."""
        if not self.selected_files:
            messagebox.showerror("Error", "Please select a file first!")
            return

        botlog(f"Processing file: {self.selected_files}", "info")

        self.hide_main_widgets()

        self.show_progress_bar() 
        self.progress.set(0.25)

        # Run processing in a separate thread to keep UI responsive
        threading.Thread(target=self.run_processing, daemon=True).start()

    def run_processing(self):
        """Runs data extraction and uploads in a background thread."""
       
       # Add logic here to handle uploaded file.

        # messagebox.showerror("Info", "Add logic to process file!")

        for i, file in enumerate(self.selected_files):
            process_document(file)

        # try:
        #     for i, file in enumerate(self.selected_files):
        #         process_document(file)
        #         self.progress.set(i/len(self.selected_files))
        #
        #     time.sleep(0.5)
        #
        # except Exception as e:
        #     messagebox.showerror("Error", f"Processing failed: {e}")
        #
        # finally:
        #     self.reset_ui()

