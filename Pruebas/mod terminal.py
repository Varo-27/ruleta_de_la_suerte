import ctypes
import time

def maximize_console():
    # Get the handle for the console window
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    
    # Check if the handle is valid
    if hwnd:
        # Maximize the console window
        ctypes.windll.user32.ShowWindow(hwnd, 3)  # SW_MAXIMIZE = 3

# Call the function to maximize the console window
maximize_console()

# Your script logic goes here
print("This is running in maximized mode!")
time.sleep(5)  # Keep the console open for 5 seconds    