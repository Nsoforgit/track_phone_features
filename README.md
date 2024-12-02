# track_phone_features
Program to track any phone features on connection to system

# Smartphone System Simulation

A comprehensive object-oriented Python project that simulates different types of smartphones with various features and capabilities, including USB connectivity and real device detection.

## Prerequisites

- Python 3.7 or higher
- libusb (required for USB communication)

## Installation

### On Linux:
```bash
sudo apt-get install libusb-1.0-0-dev
./install.sh
```

### On Windows:
1. Install libusb using Zadig (https://zadig.akeo.ie/)
2. Run `install.sh`

## Running the Project

Basic usage:
```bash
python run.py
```

Monitor connected phone:
```bash
python run.py --monitor
```

Show phone features:
```bash
python run.py --features
```

## Project Structure

```
smartphone-system/
├── smartphone/
│   ├── __init__.py
│   ├── device.py
│   ├── battery.py
│   ├── camera.py
│   ├── storage.py
│   ├── smartphone.py
│   ├── smartphone_models.py
│   ├── usb_controller.py
│   └── phone_detector.py
├── run.py
└── README.md
```

## Features

- USB device detection and monitoring
- Real-time battery status
- Storage information
- Camera capabilities
- Multiple phone tiers (Flagship, Mid-range, Budget)
- App installation and management
- Power management
- Screen control

## USB Communication

The system now supports:
- Automatic phone detection via USB
- Real-time monitoring of phone status
- Feature detection and reporting
- Battery and storage monitoring
- Support for major smartphone brands
