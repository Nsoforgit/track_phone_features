import usb.core
import usb.util
from typing import Optional, Dict, Any
import json

class USBController:
    def __init__(self):
        self.device = None
        self.interface = None
        self.endpoint = None

    def find_phone(self) -> bool:
        """Find and configure the USB device."""
        # Find all USB devices
        self.device = usb.core.find(find_all=True)
        
        if self.device is None:
            print("No USB device found")
            return False

        for dev in self.device:
            # Check if the device is a smartphone (you would need to add specific vendor/product IDs)
            if self._is_smartphone(dev):
                self.device = dev
                self._configure_device()
                return True
        
        return False

    def _is_smartphone(self, device) -> bool:
        """Check if the USB device is a smartphone."""
        # Add known smartphone vendor IDs
        smartphone_vendors = {
            0x04e8: "Samsung",
            0x18d1: "Google",
            0x22b8: "Motorola"
        }
        return device.idVendor in smartphone_vendors

    def _configure_device(self) -> None:
        """Configure the USB device for communication."""
        # Set configuration
        self.device.set_configuration()
        
        # Get an endpoint instance
        cfg = self.device.get_active_configuration()
        intf = cfg[(0,0)]
        
        self.endpoint = usb.util.find_descriptor(
            intf,
            custom_match=lambda e: 
                usb.util.endpoint_direction(e.bEndpointAddress) == 
                usb.util.ENDPOINT_IN
        )

    def get_device_info(self) -> Dict[str, Any]:
        """Get device information through USB."""
        if not self.device:
            return {}

        try:
            # Request device information
            self.endpoint.write(b'GET_INFO')
            data = self.endpoint.read(1024)
            return json.loads(data.tobytes().decode('utf-8'))
        except:
            return {}

    def request_feature(self, feature: str) -> Dict[str, Any]:
        """Request specific feature information from the device."""
        if not self.device:
            return {}

        try:
            # Send feature request
            self.endpoint.write(f'GET_FEATURE:{feature}'.encode())
            data = self.endpoint.read(1024)
            return json.loads(data.tobytes().decode('utf-8'))
        except:
            return {}