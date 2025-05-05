# CT Monitor

A real-time monitoring system for Current Transformer (CT) data using MCC118 DAQ module on Raspberry Pi.

## Requirements

- Raspberry Pi 5
- MCC118 DAQ module
- Current Transformer (CT) with voltage output (0-5V)
- Python 3.7+

## Installation

1. Clone this repository:
```bash
git clone https://github.com/sajjad-phd/CT-Edge.git
cd ct-monitor
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Install the MCC118 library:
```bash
sudo apt-get update
sudo apt-get install -y libdaqhats
```

## Hardware Setup

1. Connect the CT to the MCC118:
   - CT output to Channel 1 of MCC118
   - CT ground to GND of MCC118

## Usage

1. Start the dashboard:
```bash
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

## License

MIT License 
