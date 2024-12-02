from setuptools import setup, find_packages

setup(
    name="smartphone-system",
    version="1.0.0",
    description="A comprehensive object-oriented Python project that simulates different types of smartphones",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="StackBlitz User",
    packages=find_packages(),
    install_requires=[
        "pyserial>=3.5",  # For USB communication
        "pyusb>=1.2.0",   # For USB device detection
    ],
    entry_points={
        "console_scripts": [
            "smartphone-sim=smartphone.run:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Hardware",
    ],
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False,
)