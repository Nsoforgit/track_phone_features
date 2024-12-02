class Device:
    def __init__(self, brand: str, model: str, serial_number: str):
        self._brand = brand
        self._model = model
        self._serial_number = serial_number
        self._is_powered_on = False

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def model(self) -> str:
        return self._model

    @property
    def serial_number(self) -> str:
        return self._serial_number

    def power_on(self) -> None:
        if not self._is_powered_on:
            self._is_powered_on = True
            print(f"{self._brand} {self._model} is powering on...")

    def power_off(self) -> None:
        if self._is_powered_on:
            self._is_powered_on = False
            print(f"{self._brand} {self._model} is shutting down...")

    def is_powered_on(self) -> bool:
        return self._is_powered_on

    def __str__(self) -> str:
        return f"{self._brand} {self._model} (S/N: {self._serial_number})"