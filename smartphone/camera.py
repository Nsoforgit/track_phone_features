class Camera:
    def __init__(self, megapixels: int, aperture: float, has_ois: bool):
        self._megapixels = megapixels
        self._aperture = aperture
        self._has_ois = has_ois
        self._is_flash_on = False

    @property
    def megapixels(self) -> int:
        return self._megapixels

    @property
    def aperture(self) -> float:
        return self._aperture

    @property
    def has_ois(self) -> bool:
        return self._has_ois

    def take_photo(self) -> str:
        stabilization = "with OIS" if self._has_ois else "without OIS"
        flash_status = "with flash" if self._is_flash_on else "without flash"
        return f"Taking photo at {self._megapixels}MP (f/{self._aperture}) {stabilization} {flash_status}"

    def record_video(self, duration: int) -> str:
        return f"Recording {duration}s video at {self._megapixels}MP (f/{self._aperture})"

    def toggle_flash(self) -> None:
        self._is_flash_on = not self._is_flash_on
        status = "on" if self._is_flash_on else "off"
        print(f"Flash turned {status}")