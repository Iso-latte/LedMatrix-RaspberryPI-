# LED Matrix GIF Display for Raspberry Pi

## Overview
This project allows you to display animated GIFs on an LED matrix using a Raspberry Pi. It provides a Tkinter-based GUI to select, manage, and display GIFs on the matrix.

## Features
- Load and display GIFs on an RGB LED matrix
- Delete unwanted GIFs
- Store and manage GIFs in a dedicated directory
- Convert GIF frames into images suitable for the LED matrix
- GUI for easy GIF selection and management

## Hardware Requirements
- Raspberry Pi (Tested on Raspberry Pi)
- Adafruit RGB LED Matrix (32x32)
  - [Adafruit 32x32 RGB LED Matrix](https://www.adafruit.com/product/3211)
  - [RGB Matrix HAT](https://www.adafruit.com/product/607)

## Software Requirements
- Python 3
- Required libraries:
  - `tkinter`
  - `PIL` (Pillow)
  - `rgbmatrix` ([hzeller/rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix))
  - `shutil`
  - `os`
  - `time`
  - `RPi.GPIO`

## Installation
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/Iso-latte/LedMatrix-RaspberryPI-.git
   cd LedMatrix-RaspberryPI-
   ```
2. **Install Dependencies:**
   ```sh
   pip install pillow
   ```
   Ensure you have installed [hzeller's RGB Matrix library](https://github.com/hzeller/rpi-rgb-led-matrix) on your Raspberry Pi.

## Usage
1. **Run the GUI Application:**
   ```sh
   python3 GifGUIv03.py
   ```
2. **Select a GIF** from the file picker to set up and display.
3. **Delete a GIF** using the delete button.
4. **Restart the application** after adding new GIFs for them to appear in the list.

## Project Files
- `GIFGUIv03.py`: Main script to run the Tkinter GUI.
- `GifHandler.py`: Handles GIF processing (saving, extracting frames, resizing, deleting).
- `LEDGifController.py`: Controls the LED matrix display.

## Video Demonstration
[![Project Video](https://img.youtube.com/vi/jb1RCWxOmg4/0.jpg)](https://www.youtube.com/watch?v=jb1RCWxOmg4)

## References
- [hzeller/rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix)
- [Adafruit RGB LED Matrix](https://www.adafruit.com/product/3211)

## License
This project is open-source. Feel free to modify and contribute!

---

For any questions or issues, feel free to open an issue on GitHub!

