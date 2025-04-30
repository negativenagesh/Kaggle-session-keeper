<div align="center">

# Kaggle Session Keeper
Use the Free GPU continuously without any interruptions or you being there, on Kaggle by keeping your session active
  
</div>

## Setup
1. Clone the Repository
```zsh
git clone https://github.com/yourusername/MoodLint.git
cd MoodLint
```

2. Create and activate venv
```zsh
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On Linux/macOS
source .venv/bin/activate  # Bash/Zsh
# OR
source .venv/bin/activate.fish  # Fish
# OR
source .venv/bin/activate.csh  # Csh

# On Windows
.venv\Scripts\activate
```

3. Install dependencies
```zsh
pip3 install -r pkgs.txt
```

4. I use Fedora so System Dependencies for Fedora-
The script requires X11 display access. Install these packages:
```zsh
# Install required system packages
sudo dnf install xorg-x11-xauth xorg-x11-server-utils python3-tkinter libX11-devel libXtst-devel
```

5. Enable X11 Local Connections
Before running the script, enable local X11 connections:
```zsh
xhost +local:
```

6. Run the script
```zsh
python autoscroll.py
```

* The script will:
1. Wait 5 seconds for you to switch to your Kaggle browser tab
2. Move the mouse cursor at regular 5-second intervals
3. Perform random movements and occasional clicks to simulate activity
4. Continue until interrupted with Ctrl+C

* Troubleshooting
If you encounter X11 authorization errors:

1. Ensure X11 is properly configured:
```zsh
xhost +local:
```

2. Verify DISPLAY environment variable:
```zsh
echo $DISPLAY
export DISPLAY=:0
```

3. Check Xauthority:
```zsh
echo $XAUTHORITY
export XAUTHORITY=~/.Xauthority
```

## Features
1. Automated mouse movements every 5 seconds
2. Random movement patterns to appear like real user activity
3. Occasional clicks for additional interactivity
4. Fallback simulation mode when GUI control is unavailable
5. Countdown timer before starting
6. Clear activity logging

## License
[Apache License 2.0](LICENSE)
