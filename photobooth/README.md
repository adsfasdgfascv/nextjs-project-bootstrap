# 📸 Raspberry Pi PhotoBooth App

A beginner-friendly photo booth application designed for Raspberry Pi systems. This app provides a simple and fun way to capture photos using your Raspberry Pi camera or USB webcam.

## ✨ Features

- 📺 Live camera preview
- 📸 Easy one-click photo capture
- 💾 Automatic photo saving with timestamps
- 🎨 User-friendly interface
- ℹ️ Status updates and error messages
- 🔄 Automatic directory creation for photos

## 🛠️ Requirements

Before you start, make sure you have:

1. Raspberry Pi (any model)
2. Camera (Raspberry Pi Camera Module or USB webcam)
3. Python 3.x installed
4. The following Python packages:
   - opencv-python (for camera operations)
   - tkinter (for the user interface)
   - pillow (for image handling)

## 📥 Installation Guide

Follow these simple steps to get your photo booth up and running:

### Step 1: Update Your Raspberry Pi

Open a terminal and run:
```bash
sudo apt update
sudo apt upgrade
```

### Step 2: Install Required Packages

Install Python and required system packages:
```bash
sudo apt install python3-tk python3-pip
```

Install required Python packages:
```bash
pip3 install opencv-python pillow
```

### Step 3: Get the PhotoBooth App

1. Create a directory for the app:
```bash
mkdir photobooth
cd photobooth
```

2. Download the app files (photobooth.py) to this directory

## 🚀 Running the App

1. Navigate to the photobooth directory:
```bash
cd photobooth
```

2. Run the app:
```bash
python3 photobooth.py
```

## 📱 Using the PhotoBooth

1. When you start the app, you'll see:
   - A live camera preview
   - A green "Capture Photo" button
   - A status message showing the app is ready

2. To take a photo:
   - Click the "📸 Capture Photo" button
   - The photo will be saved automatically
   - A success message will show the saved photo's location

3. Find your photos:
   - All photos are saved in the 'photos' folder
   - Files are named with timestamps (e.g., 'photo_1234567890.jpg')

## 🔍 Troubleshooting

If you encounter any issues:

1. Camera not working:
   - Check if your camera is properly connected
   - Make sure no other app is using the camera
   - Try unplugging and reconnecting the camera

2. App won't start:
   - Verify all required packages are installed
   - Check if Python 3 is installed correctly
   - Make sure you have permission to access the camera

## 📚 Learning Resources

Want to learn more about the technologies used? Check out these beginner-friendly resources:

- [Python for Beginners](https://www.python.org/about/gettingstarted/) - Official Python getting started guide
- [OpenCV Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) - Learn about computer vision
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html) - Python's standard GUI library
- [Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/) - Official Raspberry Pi guides

## 📝 Notes

- The app creates a 'photos' directory automatically when you take your first photo
- Photos are saved with timestamp filenames to avoid overwriting
- The window size adjusts automatically to your camera's resolution
- You can close the app anytime by clicking the window's close button

## 🤝 Need Help?

If you're new to Python or Raspberry Pi, don't worry! This app is designed to be beginner-friendly. Just follow the installation steps one by one, and you'll be taking photos in no time!

Enjoy your photo booth experience! 📸
