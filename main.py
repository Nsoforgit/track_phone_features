from smartphone.smartphone_models import FlagshipPhone, MidRangePhone, BudgetPhone

def main():
    # Create different types of phones
    flagship = FlagshipPhone("Samsung", "Galaxy S23 Ultra", "SN123456789")
    midrange = MidRangePhone("Google", "Pixel 6a", "SN987654321")
    budget = BudgetPhone("Motorola", "Moto G Power", "SN456789123")

    # Test flagship phone features
    print("\nTesting Flagship Phone:")
    flagship.power_on()
    flagship.wake_screen()
    flagship.take_photo_with_camera(0)  # Using main camera
    flagship.install_app("Instagram", 100)
    flagship.launch_app("Instagram")
    flagship.enable_5g()
    flagship.wireless_charge()
    print(f"Battery level: {flagship.get_battery_level()}%")

    # Test midrange phone features
    print("\nTesting Midrange Phone:")
    midrange.power_on()
    midrange.wake_screen()
    midrange.take_photo_with_camera(0)
    midrange.install_app("WhatsApp", 50)
    midrange.enable_nfc()
    print(f"Battery level: {midrange.get_battery_level()}%")

    # Test budget phone features
    print("\nTesting Budget Phone:")
    budget.power_on()
    budget.wake_screen()
    budget.take_photo_with_camera(0)
    budget.install_app("Facebook Lite", 30)
    budget.use_headphone_jack()
    print(f"Battery level: {budget.get_battery_level()}%")

if __name__ == "__main__":
    main()