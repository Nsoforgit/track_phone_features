class Battery:
    def __init__(self, capacity: int, technology: str):
        self._capacity = capacity  # in mAh
        self._technology = technology
        self._current_level = 100
        self._is_charging = False

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def technology(self) -> str:
        return self._technology

    @property
    def current_level(self) -> int:
        return self._current_level

    def charge(self, amount: int) -> None:
        if not self._is_charging:
            self._is_charging = True
            self._current_level = min(100, self._current_level + amount)
            print(f"Battery charging... Current level: {self._current_level}%")

    def discharge(self, amount: int) -> None:
        if self._is_charging:
            self._is_charging = False
        self._current_level = max(0, self._current_level - amount)
        print(f"Battery level: {self._current_level}%")

    def is_charging(self) -> bool:
        return self._is_charging