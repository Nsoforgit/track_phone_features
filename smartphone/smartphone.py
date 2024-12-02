from typing import List
from .device import Device
from .battery import Battery
from .storage import Storage
from .camera import Camera

class Smartphone(Device):
    def __init__(self, brand: str, model: str, serial_number: str,
                 screen_size: float, battery: Battery, storage: Storage,
                 cameras: List[Camera]):
        super().__init__(brand, model, serial_number)
        self._screen_size = screen_size
        self._battery = battery
        self._storage = storage
        self._cameras = cameras
        self._is_screen_on = False
        self._active_apps = []

    @property
    def screen_size(self) -> float:
        return self._screen_size

    def wake_screen(self) -> None:
        if self.is_powered_on() and not self._is_screen_on:
            self._is_screen_on = True
            self._battery.discharge(1)
            print("Screen turned on")

    def sleep_screen(self) -> None:
        if self._is_screen_on:
            self._is_screen_on = False
            print("Screen turned off")

    def take_photo_with_camera(self, camera_index: int = 0) -> str:
        if not self.is_powered_on():
            return "Phone is powered off"
        if 0 <= camera_index < len(self._cameras):
            self._battery.discharge(2)
            return self._cameras[camera_index].take_photo()
        return "Invalid camera index"

    def record_video_with_camera(self, duration: int, camera_index: int = 0) -> str:
        if not self.is_powered_on():
            return "Phone is powered off"
        if 0 <= camera_index < len(self._cameras):
            self._battery.discharge(duration * 3)
            return self._cameras[camera_index].record_video(duration)
        return "Invalid camera index"

    def install_app(self, app_name: str, app_size: int) -> bool:
        if not self.is_powered_on():
            print("Phone is powered off")
            return False
        return self._storage.install_app(app_name, app_size)

    def uninstall_app(self, app_name: str, app_size: int) -> bool:
        if not self.is_powered_on():
            print("Phone is powered off")
            return False
        return self._storage.uninstall_app(app_name, app_size)

    def launch_app(self, app_name: str) -> None:
        if not self.is_powered_on():
            print("Phone is powered off")
            return
        if app_name in self._storage.list_installed_apps():
            if app_name not in self._active_apps:
                self._active_apps.append(app_name)
                self._battery.discharge(5)
                print(f"Launched {app_name}")
            else:
                print(f"{app_name} is already running")
        else:
            print(f"{app_name} is not installed")

    def close_app(self, app_name: str) -> None:
        if app_name in self._active_apps:
            self._active_apps.remove(app_name)
            print(f"Closed {app_name}")
        else:
            print(f"{app_name} is not running")

    def list_running_apps(self) -> List[str]:
        return self._active_apps

    def get_battery_level(self) -> int:
        return self._battery.current_level

    def charge_battery(self, amount: int) -> None:
        self._battery.charge(amount)