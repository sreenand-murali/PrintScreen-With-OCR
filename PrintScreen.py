#!/home/sreeennd/Downloads/pyvenv/bin/python
import subprocess
import os
from datetime import datetime
from PIL import Image
import pytesseract
import pyperclip

def snip_screen():
    # Get current date and time for the filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_name = f"screenshot_{timestamp}.png"

    # Define the directory to save the screenshot (custom path)
    save_directory = os.path.expanduser("~/Pictures/Screenshots")  # Save to ~/Pictures/Screenshots
    os.makedirs(save_directory, exist_ok=True)  # Create the directory if it doesn't exist

    # Full path for the screenshot
    screenshot_path = os.path.join(save_directory, screenshot_name)

    # Use 'scrot' to capture the screenshot of the selected area on Linux
    subprocess.run(['scrot', '-s', screenshot_path])

    # Confirm the screenshot was saved
    print(f"Screenshot saved at {screenshot_path}")

    # Perform OCR on the captured screenshot
    extract_text_from_image(screenshot_path)

def extract_text_from_image(image_path):
    try:
        # Open the image file
        img = Image.open(image_path)

        # Use pytesseract to extract text from the image
        extracted_text = pytesseract.image_to_string(img)

        if extracted_text.strip():  # Check if any text was extracted
            print("\nExtracted Text:\n")
            print(extracted_text)

            # Copy the extracted text to the clipboard
            pyperclip.copy(extracted_text)
            print("\nText copied to clipboard!")
        else:
            print("No text detected in the screenshot.")

    except Exception as e:
        print(f"Error during OCR: {e}")

if __name__ == "__main__":
    snip_screen()
