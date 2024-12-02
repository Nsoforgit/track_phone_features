"""
Script to generate Python bytecode cache files.
This will create __pycache__ directories when imported and run.
"""

from smartphone import (
    FlagshipPhone,
    MidRangePhone,
    BudgetPhone,
    Smartphone,
    Device,
    Battery,
    Storage,
    Camera
)
from smartphone.phone_detector import PhoneDetector
from smartphone.usb_controller import USBController

def main():
    # Create instances to trigger bytecode compilation
    phone_detector = PhoneDetector()
    usb_controller = USBController()
    
    # Create different types of phones
    flagship = FlagshipPhone("Samsung", "Galaxy S23 Ultra", "SN123456789")
    midrange = MidRangePhone("Google", "Pixel 6a", "SN987654321")
    budget = BudgetPhone("Motorola", "Moto G Power", "SN456789123")
    
    print("Python bytecode cache files have been generated!")
    print("You can find them in the smartphone/__pycache__ directory")

if __name__ == "__main__":
    main()