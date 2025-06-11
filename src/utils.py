import sounddevice as sd
import soundfile as sf
import tkinter as tk


def play_audio(sound_file):
    """Plays a .wav sound file using sounddevice."""
    data, fs = sf.read(sound_file, dtype='float32')  # Load the WAV file
    sd.play(data, fs)  # Play the sound
    sd.wait()  # Wait until the sound finishes playing


def show_fading_popup_with_sound(title, message, duration=2000):
    """Show a fading popup notification with sound at the top-right corner."""

    popup = tk.Tk()
    popup.title(title)
    popup.overrideredirect(True)  # Remove window borders
    popup.attributes('-topmost', True)  # Keep the popup on top
    popup.configure(bg="lightyellow")

    # Get screen width and height to position the popup at the top-right corner
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()  # Not used, but kept in case you want further adjustments.

    # Define popup size
    popup_width, popup_height = 300, 100
    x_position = screen_width - popup_width - 10  # 10px margin from right
    y_position = 10  # 10px margin from the top (for top-right corner)

    # Set popup geometry
    popup.geometry(f"{popup_width}x{popup_height}+{x_position}+{y_position}")

    # Add a message label
    label = tk.Label(popup, text=message, font=("Arial", 11), bg="lightyellow", wraplength=280)
    label.pack(expand=True, pady=15, padx=15)

    # Fade-in and fade-out effect
    def fade_in():
        alpha = 0.0
        while alpha < 1.0:
            popup.attributes("-alpha", alpha)
            alpha += 0.05
            popup.update()
            popup.after(50)  # Adjust speed of fade-in

    def fade_out():
        alpha = 1.0
        while alpha > 0.0:
            popup.attributes("-alpha", alpha)
            alpha -= 0.05
            popup.update()
            popup.after(50)  # Adjust speed of fade-out
        popup.destroy()

    # Show the fade-in effect, wait for the duration, and fade out
    fade_in()
    popup.after(duration, fade_out)

    # Run the popup
    popup.mainloop()