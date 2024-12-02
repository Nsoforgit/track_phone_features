from .usb_controller import USBController
from typing import Optional, Dict, Any

class PhoneDetector:
    def __init__(self):
        self.usb_controller = USBController()
        self.connected_phone = None

    def detect_phone(self) -> bool:
        """Detect and initialize connection with a phone."""
        if self.usb_controller.find_phone():
            device_info = self.usb_controller.get_device_info()
            if device_info:
                self.connected_phone = device_info
                print(f"Connected to {device_info.get('brand', 'Unknown')} "
                      f"{device_info.get('model', 'Device')}")
                return True
        return False

    def get_phone_features(self) -> Dict[str, Any]:
        """Get all available features of the connected phone."""
        if not self.connected_phone:
            return {}

        features = {}
        feature_list = [
            'battery', 'storage', 'camera', 'network',
            'sensors', 'charging_capabilities'
        ]

        for feature in feature_list:
            result = self.usb_controller.request_feature(feature)
            if result:
                features[feature] = result

        return features

    def monitor_phone(self) -> None:
        """Start monitoring phone status and features."""
        if not self.connected_phone:
            print("No phone connected")
            return

        try:
            while True:
                battery_info = self.usb_controller.request_feature('battery')
                if battery_info:
                    print(f"Battery Level: {battery_info.get('level')}%")
                    print(f"Charging Status: {battery_info.get('charging')}")
                
                storage_info = self.usb_controller.request_feature('storage')
                if storage_info:
                    print(f"Storage Used: {storage_info.get('used_space')}GB")
                    print(f"Storage Available: {storage_info.get('free_space')}GB")
                
                # Add delay to prevent excessive polling
                import time
                time.sleep(5)
        except KeyboardInterrupt:
            print("\nStopped monitoring phone")