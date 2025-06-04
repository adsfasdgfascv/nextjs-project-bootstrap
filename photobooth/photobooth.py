"""
Raspberry Pi PhotoBooth Application
A simple and beginner-friendly photo booth application using Python, OpenCV, and Tkinter.
This app provides a live camera preview and allows users to capture and save photos.
"""

import cv2  # OpenCV library for camera operations
import tkinter as tk  # GUI library
from tkinter import Button, Label, messagebox
from PIL import Image, ImageTk  # For handling image display in Tkinter
import threading  # For handling concurrent operations
import time  # For timestamp in filenames
import os  # For file and directory operations

# Configuration constants
WINDOW_TITLE = "Raspberry Pi PhotoBooth"
PHOTOS_DIR = "photos"
CAMERA_INDEX = 0  # Default camera (0 is usually the first/default camera)
UPDATE_DELAY = 15  # Milliseconds between frame updates
BUTTON_WIDTH = 50

class PhotoBoothApp:
    """
    Main PhotoBooth application class.
    Handles the GUI creation and camera operations.
    """
    
    def __init__(self, window, window_title):
        """
        Initialize the PhotoBooth application.
        
        Args:
            window: The main Tkinter window
            window_title: Title for the window
        """
        # Setup the window
        self.window = window
        self.window.title(window_title)
        self.window.resizable(False, False)  # Fixed window size

        try:
            # Initialize the camera
            self.setup_camera()
            
            # Create the user interface
            self.create_ui()
            
            # Start the main update loop
            self.update()
            
            # Handle window closing
            self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
            
            # Start Tkinter main loop
            self.window.mainloop()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start PhotoBooth: {str(e)}")
            self.window.destroy()

    def setup_camera(self):
        """Initialize and configure the camera."""
        self.vid = cv2.VideoCapture(CAMERA_INDEX)
        if not self.vid.isOpened():
            raise ValueError("Unable to open camera. Please check if camera is connected.")

        # Get camera resolution
        self.width = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def create_ui(self):
        """Create the user interface elements."""
        # Create canvas for video display
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height)
        self.canvas.pack(padx=10, pady=5)

        # Create status label
        self.status_label = Label(self.window, text="Ready to capture!", fg="green")
        self.status_label.pack(pady=5)

        # Create capture button
        self.btn_capture = Button(
            self.window,
            text="📸 Capture Photo",
            width=BUTTON_WIDTH,
            command=self.capture_photo,
            bg="#4CAF50",  # Green background
            fg="white",    # White text
            relief=tk.RAISED,
            cursor="hand2"  # Hand cursor on hover
        )
        self.btn_capture.pack(anchor=tk.CENTER, expand=True, pady=10)

    def update(self):
        """Update the video feed on the canvas."""
        try:
            ret, frame = self.vid.read()
            if ret:
                # Convert the image from BGR (OpenCV) to RGB (PIL)
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame_rgb))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

            # Schedule the next update
            self.window.after(UPDATE_DELAY, self.update)
        except Exception as e:
            self.status_label.config(text=f"Error updating camera feed: {str(e)}", fg="red")

    def capture_photo(self):
        """Capture and save a photo."""
        try:
            ret, frame = self.vid.read()
            if ret:
                # Create photos directory if it doesn't exist
                if not os.path.exists(PHOTOS_DIR):
                    os.makedirs(PHOTOS_DIR)

                # Generate filename with timestamp
                filename = f"{PHOTOS_DIR}/photo_{int(time.time())}.jpg"
                
                # Save the photo
                cv2.imwrite(filename, frame)
                
                # Update status
                self.status_label.config(
                    text=f"Photo saved as {filename}",
                    fg="green"
                )
            else:
                raise ValueError("Failed to capture photo")
                
        except Exception as e:
            self.status_label.config(
                text=f"Error capturing photo: {str(e)}",
                fg="red"
            )

    def on_closing(self):
        """Clean up resources when the window is closed."""
        try:
            if self.vid.isOpened():
                self.vid.release()
        finally:
            self.window.destroy()

if __name__ == "__main__":
    try:
        # Create and start the PhotoBooth application
        PhotoBoothApp(tk.Tk(), WINDOW_TITLE)
    except Exception as e:
        print(f"Failed to start application: {str(e)}")
