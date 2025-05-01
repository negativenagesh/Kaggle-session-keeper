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
                
                # Perform scrolling actions to keep session active
                if activity_count % 3 == 0:
                    # Occasional click to ensure focus
                    pyautogui.click()
                    print(f"Clicked at position ({start_x}, {start_y}) at {elapsed_seconds}s")
                
                # Random scroll amount - negative values scroll down, positive scroll up
                scroll_amount = random.randint(-10, 10) * 10  # Scale for more noticeable scrolling
                
                # Perform the scroll
                pyautogui.scroll(scroll_amount)
                direction = "up" if scroll_amount > 0 else "down"
                print(f"Scrolled {direction} by {abs(scroll_amount)} units at {elapsed_seconds}s")
                
                # Sometimes do a second scroll in opposite direction
                if random.random() > 0.6:  # 40% chance
                    time.sleep(0.5)
                    opposite_scroll = -scroll_amount // 2
                    pyautogui.scroll(opposite_scroll)
                    opposite_dir = "up" if opposite_scroll > 0 else "down"
                    print(f"Additional scroll {opposite_dir} by {abs(opposite_scroll)} units")
            else:
                print("WARNING: Simulated movement only (no actual mouse control)")
                
            # Fixed wait time of 5 seconds
            print(f"Activity count: {activity_count} - Next action in 5 seconds")
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
