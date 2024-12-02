#!/usr/bin/env python3

"""
Enhanced runner script with USB detection and monitoring capabilities.
"""

from smartphone.phone_detector import PhoneDetector
import argparse

def main():
    parser = argparse.ArgumentParser(description='Smartphone USB Detection and Monitoring')
    parser.add_argument('--monitor', action='store_true', help='Monitor connected phone')
    parser.add_argument('--features', action='store_true', help='Show phone features')
    args = parser.parse_args()

    detector = PhoneDetector()
    
    print("Searching for connected phones...")
    if detector.detect_phone():
        if args.features:
            print("\nRetrieving phone features...")
            features = detector.get_phone_features()
            for feature, details in features.items():
                print(f"\n{feature.upper()}:")
                for key, value in details.items():
                    print(f"  {key}: {value}")
        
        if args.monitor:
            print("\nStarting phone monitoring (Press Ctrl+C to stop)...")
            detector.monitor_phone()
    else:
        print("No compatible phone detected. Please connect a phone via USB.")

if __name__ == "__main__":
    main()