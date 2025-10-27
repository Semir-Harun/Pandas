#!/usr/bin/env python3
"""
Quick Start Script for Pandas Learning Project
==============================================

This script helps you get started with the Pandas learning notebooks.
It checks your environment and provides helpful information.
"""

import sys
import subprocess
import importlib.util

def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    print(f"🐍 Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✅ Python version is compatible!")
        return True
    else:
        print("❌ Python 3.8+ is required for this project")
        return False

def check_package(package_name):
    """Check if a package is installed."""
    spec = importlib.util.find_spec(package_name)
    return spec is not None

def check_dependencies():
    """Check if required packages are installed."""
    required_packages = [
        'pandas', 'numpy', 'matplotlib', 'seaborn', 'jupyter'
    ]
    
    print("\n📦 Checking required packages:")
    all_installed = True
    
    for package in required_packages:
        if check_package(package):
            if package == 'pandas':
                import pandas as pd
                print(f"✅ {package} ({pd.__version__})")
            elif package == 'numpy':
                import numpy as np
                print(f"✅ {package} ({np.__version__})")
            else:
                print(f"✅ {package}")
        else:
            print(f"❌ {package} - Not installed")
            all_installed = False
    
    return all_installed

def main():
    """Main function to run all checks."""
    print("🐼 Pandas Learning Project - Quick Start")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        print("\n🔧 To install missing packages, run:")
        print("pip install -r requirements.txt")
        print("\nOr install individually:")
        print("pip install pandas numpy matplotlib seaborn jupyter")
        sys.exit(1)
    
    print("\n🚀 READY TO START LEARNING!")
    print("=" * 30)
    print("📚 Available notebooks:")
    print("  1. 01_reading_data.ipynb - Data loading and exploration")
    print("  2. 02_groupby_agg.ipynb - GroupBy operations and aggregation")
    print("  3. 03_filtering_cleaning.ipynb - Data filtering and cleaning")
    
    print("\n🎯 To get started:")
    print("  1. Launch Jupyter: jupyter notebook")
    print("  2. Open notebooks/ folder")
    print("  3. Start with 01_reading_data.ipynb")
    
    print("\n🌐 Alternative options:")
    print("  • Binder: https://mybinder.org/v2/gh/Semir-Harun/Pandas/main")
    print("  • Google Colab: Upload notebooks to Colab")
    
    print("\nHappy learning! 🎓📊")

if __name__ == "__main__":
    main()