class Storage:
    def __init__(self, capacity: int):
        self._capacity = capacity  # in GB
        self._used_space = 0
        self._installed_apps = []

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def used_space(self) -> int:
        return self._used_space

    @property
    def free_space(self) -> int:
        return self._capacity - self._used_space

    def install_app(self, app_name: str, app_size: int) -> bool:
        if app_size <= self.free_space:
            self._used_space += app_size
            self._installed_apps.append(app_name)
            print(f"Installed {app_name}. Space remaining: {self.free_space}GB")
            return True
        print(f"Not enough space to install {app_name}")
        return False

    def uninstall_app(self, app_name: str, app_size: int) -> bool:
        if app_name in self._installed_apps:
            self._installed_apps.remove(app_name)
            self._used_space -= app_size
            print(f"Uninstalled {app_name}. Space remaining: {self.free_space}GB")
            return True
        print(f"{app_name} is not installed")
        return False

    def list_installed_apps(self) -> list:
        return self._installed_apps