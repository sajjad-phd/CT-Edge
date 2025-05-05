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

2. First Boot Setup:
   ```bash
   # Update system packages
   sudo apt update
   sudo apt upgrade -y
   
   # Install essential tools
   sudo apt install -y git python3-pip python3-venv
   ```

3. Create and activate Python virtual environment:
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
git clone <your-repository-url>
cd ct-monitor
```

2. Install the required packages:
   ```bash
   # Make sure you're in the virtual environment
   source venv/bin/activate
   
   # Install Python dependencies
   pip install -r requirements.txt
   ```

3. Install the MCC118 library:
   ```bash
   sudo apt-get update
   sudo apt-get install -y libdaqhats
   ```

4. Configure I2C and SPI interfaces:
   ```bash
   # Enable I2C and SPI
   sudo raspi-config
   # Navigate to Interface Options -> I2C -> Yes
   # Navigate to Interface Options -> SPI -> Yes
   ```

## Hardware Setup

1. Connect the CT to the MCC118:
   - CT output to Channel 1 of MCC118
   - CT ground to GND of MCC118

2. Verify hardware connections:
   ```bash
   # Check if MCC118 is detected
   dtoverlay -l
   ```

## Usage

1. Start the dashboard:
   ```bash
   # Make sure you're in the virtual environment
   source venv/bin/activate
   
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
   ```

2. If Python packages fail to install:
   ```bash
   # Update pip
   pip install --upgrade pip
   # Try installing packages again
   pip install -r requirements.txt
   ```

## License

MIT License 
