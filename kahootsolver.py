
#python reads the screen, taking a screenshot, converting images to text
#1. We need to read the screen
#2. We need to translate the words on the screen to an actual string
#3. Feed it to chatgpt
#4. Output
import time
from PIL import ImageGrab
import pytesseract

# Take a screenshot
time.sleep(4)
screenshot = ImageGrab.grab()

# Convert the screenshot to text
text = pytesseract.image_to_string(screenshot)

# Print the extracted text
print(text)
