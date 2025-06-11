import tkinter as tk
from tkinter import ttk, messagebox

from src.browser import focus_chrome_window
from src.utils import show_fading_popup_with_sound


def start_bot():
    """Starts the bot when the button is clicked."""
    url = url_entry.get()  # Get the value from the entry widget
    # Check and focus on running Chrome browser, or show an alert if not found
    if focus_chrome_window():
        show_fading_popup_with_sound(title="Browser Found", message="Focusing on the open Chrome browser.")

    else:
        show_fading_popup_with_sound(title="Browser Not Found", message="No open Chrome browser found. Please open Chrome manually.")
        return

    try:
        root.update_idletasks()  # Update the UI before running the bot

        messagebox.showinfo("Success", "Bot has finished running successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while running the bot:\n{e}")



# Function to create and display the Tkinter-based user interface
def create_ui():
    global root, url_entry, log_text  # Declare global variables to be used across the functions

    # Initialize the main Tkinter window
    root = tk.Tk()
    root.title("Automation Bot")  # Window title
    root.geometry("400x300")  # Set the initial window size (width x height)

    # Add a title label to the window
    ttk.Label(root, text="Automation Bot", font=("Arial", 16)).pack(pady=10)

    # Add a label and entry field for the URL input
    ttk.Label(root, text="Enter URL:").pack(anchor="w", padx=20)
    url_entry = ttk.Entry(root, width=50)  # Input entry field
    url_entry.pack(padx=20, pady=5)

    # Add a Start button to trigger the bot
    ttk.Button(root, text="Start Bot", command=start_bot).pack(pady=20)

    # Add a label to display status log
    ttk.Label(root, text="Status:").pack(anchor="w", padx=20)
    log_text = tk.StringVar()  # Variable to hold the log/status text
    log_text.set("Waiting for actions...")
    ttk.Label(root, textvariable=log_text, foreground="blue", wraplength=360).pack(padx=20, pady=5)

    # Run the main Tkinter event loop
    root.mainloop()