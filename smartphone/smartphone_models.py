from .smartphone import Smartphone
from .battery import Battery
from .storage import Storage
from .camera import Camera

class FlagshipPhone(Smartphone):
    def __init__(self, brand: str, model: str, serial_number: str):
        battery = Battery(5000, "Li-Ion")
        storage = Storage(512)
        cameras = [
            Camera(108, 1.8, True),  # Main camera
            Camera(12, 2.2, True),   # Ultra-wide
            Camera(10, 2.4, True)    # Telephoto
        ]
        super().__init__(brand, model, serial_number, 6.7, battery, storage, cameras)
        self._has_5g = True
        self._has_wireless_charging = True

    def enable_5g(self) -> None:
        if self.is_powered_on() and self._has_5g:
            print("5G enabled")
            self._battery.discharge(2)

    def wireless_charge(self) -> None:
        if self._has_wireless_charging:
            print("Wireless charging started")
            self._battery.charge(10)

class MidRangePhone(Smartphone):
    def __init__(self, brand: str, model: str, serial_number: str):
        battery = Battery(4500, "Li-Ion")
        storage = Storage(128)
        cameras = [
            Camera(64, 1.9, False),  # Main camera
            Camera(8, 2.4, False)    # Wide-angle
        ]
        super().__init__(brand, model, serial_number, 6.4, battery, storage, cameras)
        self._has_5g = False
        self._has_nfc = True

    def enable_nfc(self) -> None:
        if self.is_powered_on() and self._has_nfc:
            print("NFC enabled")
            self._battery.discharge(1)

class BudgetPhone(Smartphone):
    def __init__(self, brand: str, model: str, serial_number: str):
        battery = Battery(4000, "Li-Ion")
        storage = Storage(64)
        cameras = [
            Camera(48, 2.0, False),  # Main camera
        ]
        super().__init__(brand, model, serial_number, 6.1, battery, storage, cameras)
        self._has_5g = False
        self._has_headphone_jack = True

    def use_headphone_jack(self) -> None:
        if self.is_powered_on() and self._has_headphone_jack:
            print("Headphones connected via jack")
            self._battery.discharge(1)