# CT Monitor

A real-time monitoring system for Current Transformer (CT) data using MCC118 DAQ module on Raspberry Pi.

## Requirements

- Raspberry Pi 5
- MCC118 DAQ module
- Current Transformer (CT) with voltage output (0-5V)
- Python 3.7+

## Initial Setup

1. Install Raspberry Pi OS:
   - Download Raspberry Pi Imager from [raspberrypi.org](https://www.raspberrypi.org/software/)
   - Flash the latest Raspberry Pi OS (64-bit) to your SD card
   - Enable SSH during setup if you want remote access
   - Set up your username and password during the initial setup

2. First Boot Setup:
   ```bash
   # Update system packages
   sudo apt update
   sudo apt upgrade -y
   
   # Install essential tools
   sudo apt install -y git python3-pip python3-venv build-essential
   ```

3. Configure Git (if you haven't already):
   ```bash
   # Set your Git username and email
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

4. Install MCC118 DAQ HAT Library:
   ```bash
   # Clone the MCC DAQ HAT library repository
   git clone https://github.com/mccdaq/daqhats.git
   cd daqhats
   
   # Install the library
   sudo ./install.sh
   
   # Return to home directory
   cd ~
   ```

5. Configure I2C and SPI interfaces:
   ```bash
   # Enable I2C and SPI
   sudo raspi-config
   # Navigate to Interface Options -> I2C -> Yes
   # Navigate to Interface Options -> SPI -> Yes
   
   # Add MCC118 overlay to config.txt
   echo "dtoverlay=mcc118" | sudo tee -a /boot/config.txt
   
   # Reboot to apply changes
   sudo reboot
   ```

6. Verify MCC118 Installation:
   ```bash
   # After reboot, test MCC118 detection
   mcc118_test
   
   # Or test with Python
   python3
   >>> from daqhats import hat_list, HatIDs
   >>> hats = hat_list()
   >>> for hat in hats:
   ...     print(hat)
   ```

7. Create and activate Python virtual environment:
   ```bash
   # Create a new directory for the project
   mkdir ~/ct-monitor
   cd ~/ct-monitor
   
   # Create virtual environment
   python3 -m venv venv
   
   # Activate virtual environment
   source venv/bin/activate
   ```

## Installation

1. Clone this repository:
   ```bash
   # Make sure you're in the correct directory
   cd ~/ct-monitor
   
   # Clone the repository
   git clone https://github.com/sajjad-phd/CT-Edge.git
   
   # Move into the project directory
   cd CT-Edge
   ```

<<<<<<< HEAD
2. Install the required Python packages:
=======
2. Install the MCC118 library first:
   ```bash
   # Update package list
   sudo apt-get update
   
   # Install MCC118 library and Python bindings
   sudo apt-get install -y libdaqhats python3-daqhats
   ```

3. Install the required Python packages:
>>>>>>> c53fb1e1006d4662ed682c3331371e2d9e9de44b
   ```bash
   # Make sure you're in the virtual environment
   source venv/bin/activate
   
   # Make sure you're in the CT-Edge directory
   pwd  # Should show /home/aiog/ct-monitor/CT-Edge
   
   # Verify requirements.txt exists
   ls requirements.txt
   
   # Upgrade pip to latest version
   pip install --upgrade pip
   
<<<<<<< HEAD
   # Install Python dependencies
   pip install streamlit numpy pandas matplotlib
=======
   # Install Python dependencies (excluding mcc118 as it's installed via apt)
   pip install streamlit numpy pandas matplotlib
   ```

4. Configure I2C and SPI interfaces:
   ```bash
   # Enable I2C and SPI
   sudo raspi-config
   # Navigate to Interface Options -> I2C -> Yes
   # Navigate to Interface Options -> SPI -> Yes
   # Reboot after enabling interfaces
   sudo reboot
>>>>>>> c53fb1e1006d4662ed682c3331371e2d9e9de44b
   ```

## Hardware Setup

1. Connect the CT to the MCC118:
   - CT output to Channel 1 of MCC118
   - CT ground to GND of MCC118

2. Verify hardware connections:
   ```bash
   # Check if MCC118 is detected
   dtoverlay -l
   
   # Check I2C devices
   i2cdetect -y 1
   
   # Check HAT devices
   ls /proc/device-tree/hat/
   ```

## Usage

1. Start the dashboard:
   ```bash
   # Make sure you're in the virtual environment
   source venv/bin/activate
   
   # Make sure you're in the project directory
   cd ~/ct-monitor/CT-Edge
   
   # Start the dashboard
   streamlit run dashboard.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:8501
   ```

## Features

- Real-time voltage monitoring at 5kHz sampling rate
- Interactive dashboard with live plotting
- Voltage metrics display
- Configurable buffer size and sample rate

## Project Structure

- `ct_reader.py`: Core data acquisition module
- `dashboard.py`: Streamlit dashboard for visualization
- `requirements.txt`: Python package dependencies

## Troubleshooting

1. If MCC118 is not detected:
   ```bash
   # Check if the module is properly connected
   ls /dev/i2c*
   ls /dev/spi*
   
   # Check I2C bus
   i2cdetect -y 1
   
   # Check HAT devices
   ls /proc/device-tree/hat/
   
   # Test MCC118 with Python
   python3
   >>> from daqhats import hat_list, HatIDs
   >>> hats = hat_list()
   >>> for hat in hats:
   ...     print(hat)
   ```

2. If Python packages fail to install:
   ```bash
   # Make sure you're in the virtual environment
   source venv/bin/activate
   
   # Update pip
   pip install --upgrade pip
   
   # Try installing packages one by one
   pip install streamlit
   pip install numpy
   pip install pandas
   pip install matplotlib
   ```

3. If you get permission errors:
   ```bash
   # Add your user to the i2c and spi groups
   sudo usermod -a -G i2c,spi $USER
   
   # You may need to log out and log back in for changes to take effect
   ```

## License

MIT License
