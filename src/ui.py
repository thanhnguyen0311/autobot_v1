import tkinter as tk
from tkinter import ttk, messagebox
from src.bot import run_bot  # Importing the bot logic from your existing bot module


# Function to start the bot with the user-provided URL
def start_bot():
    """Starts the bot when the button is clicked."""
    url = url_entry.get()  # Get the value from the entry widget
    if not url.strip():  # Check if URL is empty
        messagebox.showwarning("Input Error", "Please enter a valid URL.")
        return

    try:
        log_text.set("Starting the bot...")
        root.update_idletasks()  # Update the UI before running the bot

        # Passing the URL to your run_bot implementation
        run_bot(url)

        log_text.set("Bot completed successfully!")
        messagebox.showinfo("Success", "Bot has finished running successfully!")
    except Exception as e:
        log_text.set(f"Error: {e}")
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