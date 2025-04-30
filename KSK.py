import time
import random
import os
import sys
import subprocess

# Try to ensure X11 display is properly set
if 'DISPLAY' not in os.environ:
    os.environ['DISPLAY'] = ':0'

# Try to import pyautogui with better error handling
try:
    # First try to fix X11 authorization
    try:
        subprocess.run(['xhost', '+local:'], capture_output=True, text=True)
        print("Enabled local X11 connections")
    except:
        pass  # If xhost command fails, continue anyway
        
    import pyautogui
    # Force test of mouse control functionality
    x, y = pyautogui.position()
    pyautogui.moveTo(x+1, y+1)
    pyautogui.moveTo(x, y)
    
    screen_width, screen_height = pyautogui.size()
    PYAUTOGUI_AVAILABLE = True
    pyautogui.PAUSE = 0.1
    pyautogui.FAILSAFE = True
    print(f"PyAutoGUI successfully controlling mouse! Screen: {screen_width}x{screen_height}")
except Exception as e:
    PYAUTOGUI_AVAILABLE = False
    print(f"PyAutoGUI initialization failed: {e}")
    print("ERROR: Cannot control mouse - Kaggle session may timeout!")

def keep_kaggle_session_active():
    try:
        print("Starting Kaggle session keeper...")
        
        if not PYAUTOGUI_AVAILABLE:
            print("CRITICAL: Mouse control unavailable! Session may timeout!")
            print("Try running: 'xhost +local:' before running this script")
        else:
            print("✓ Mouse control active - Kaggle session will be kept alive")
            print("  Move cursor to top-left corner to abort (failsafe)")
            
        activity_count = 0
        start_time = time.time()
        
        while True:
            if PYAUTOGUI_AVAILABLE:
                activity_count += 1
                elapsed_seconds = int(time.time() - start_time)
                # Remember starting position
                start_x, start_y = pyautogui.position()
                
                # Perform a variety of actions to signal activity
                if activity_count % 3 == 0:
                    # Click action (every third cycle)
                    pyautogui.click()
                    print(f"Clicked at position ({start_x}, {start_y}) at {elapsed_seconds}s")
                    
                    # Small movement after click
                    move_x = random.randint(-20, 20)
                    move_y = random.randint(-20, 20)
                    new_x = max(0, min(screen_width - 10, start_x + move_x)) 
                    new_y = max(0, min(screen_height - 10, start_y + move_y))
                    pyautogui.moveTo(new_x, new_y, duration=0.3)
                else:
                    # More significant random movement
                    move_x = random.randint(-100, 100)
                    move_y = random.randint(-100, 100)
                    new_x = max(0, min(screen_width - 10, start_x + move_x))
                    new_y = max(0, min(screen_height - 10, start_y + move_y))
                    pyautogui.moveTo(new_x, new_y, duration=0.5)
                    print(f"Moved mouse from ({start_x}, {start_y}) to ({new_x}, {new_y}) at {elapsed_seconds}s")
                    
                # Return close to original position (but not exactly)
                return_x = start_x + random.randint(-5, 5)
                return_y = start_y + random.randint(-5, 5)
                pyautogui.moveTo(return_x, return_y, duration=0.3)
            else:
                print("WARNING: Simulated movement only (no actual mouse control)")
                
            # Fixed wait time of 5 seconds
            print(f"Activity count: {activity_count} - Next movement in 5 seconds")
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nStopped by user (Ctrl+C).")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Give time to switch to the Kaggle browser window
    if PYAUTOGUI_AVAILABLE:
        print("\n*** KAGGLE SESSION KEEPER ***")
        print("Switch to your Kaggle browser tab NOW!")
        for i in range(5, 0, -1):
            print(f"Starting in {i} seconds...")
            time.sleep(1)
    else:
        print("Running in simulation mode (WILL NOT KEEP KAGGLE SESSION ACTIVE)")
    
    keep_kaggle_session_active()
