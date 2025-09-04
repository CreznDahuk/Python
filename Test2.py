import cv2
import numpy as np
import pyautogui
import mss

# Target circle color (blue RGB 59,130,246 converted to HSV range)
lower_color = np.array([209, 150, 200])
upper_color = np.array([229, 255, 255])

with mss.mss() as sct:
    monitor = sct.monitors[1]  # Full screen

    while True:
        # Capture screenshot
        screenshot = np.array(sct.grab(monitor))
        frame = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

        # Convert to HSV and apply color mask
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_color, upper_color)

        # Detect circles
        circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, dp=1.2,
                                   minDist=50, param1=50, param2=30,
                                   minRadius=10, maxRadius=200)

        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for (x, y, r) in circles:
                pyautogui.moveTo(x, y)
                pyautogui.click()
                print(f"Clicked at: {x}, {y}")
