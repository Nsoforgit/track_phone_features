import usb.core
import usb.backend

backend = usb.backend.libusb1.get_backend()
if backend is None:
    print("No backend available")
else:
    print("Backend is available")