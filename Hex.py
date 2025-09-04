import pyautogui
import pytesseract
from PIL import ImageGrab
import time

# Path to Tesseract (Windows only)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# -----------------------------
# CONFIG
# -----------------------------

# Screen regions (x1, y1, x2, y2) - adjust these to match your game window
ENEMY_REGION = (200, 100, 300, 200)   # region where the enemy hex appears
BINARY_REGION = (100, 400, 700, 450)  # region where the binary row is

# Hardcoded click positions for each binary digit box (left to right)
# You need to use pyautogui.position() to record exact coords for your setup
BINARY_BOXES = [
    (120, 430), (170, 430), (220, 430), (270, 430),
    (320, 430), (370, 430), (420, 430), (470, 430),
]

SCAN_DELAY = 1.0  # seconds


# -----------------------------
# FUNCTIONS
# -----------------------------

def capture_region(region):
    """Capture part of the screen."""
    return ImageGrab.grab(bbox=region)


def get_enemy_hex():
    """OCR the enemy's hex value."""
    img = capture_region(ENEMY_REGION)
    text = pytesseract.image_to_string(
        img, config="--psm 8 -c tessedit_char_whitelist=0123456789ABCDEF"
    )
    return text.strip().upper()


def hex_to_binary(hex_val):
    """Convert hex to 8-bit binary string."""
    try:
        return bin(int(hex_val, 16))[2:].zfill(8)
    except:
        return None


def click_binary(binary_str):
    """Click the boxes corresponding to the binary string."""
    for i, bit in enumerate(binary_str):
        if bit == "1":
            x, y = BINARY_BOXES[i]
            pyautogui.click(x, y)
            time.sleep(0.1)  # small delay between clicks


# -----------------------------
# MAIN LOOP
# -----------------------------

print("[*] Starting Hex→Binary Clicker. Press CTRL+C to stop.")

try:
    while True:
        hex_val = get_enemy_hex()
        if hex_val:
            binary_str = hex_to_binary(hex_val)
            if binary_str:
                print(f"[+] Enemy HEX: {hex_val} -> {binary_str}")
                click_binary(binary_str)
        else:
            print("[-] No hex detected.")
        
        time.sleep(SCAN_DELAY)

except KeyboardInterrupt:
    print("\n[!] Stopped by user.")
