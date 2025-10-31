"""
Quick Start Script - Easy launcher for Manufacturer Finder Tool
"""

import os
import sys

# Set your OpenAI API key here
# For security, load from environment variable or secrets.toml
API_KEY = os.getenv('OPENAI_API_KEY', '')

if not API_KEY:
    try:
        import streamlit as st
        API_KEY = st.secrets.get("OPENAI_API_KEY", "")
    except:
        pass

if not API_KEY:
    print("ERROR: No API key found!")
    print("Set OPENAI_API_KEY environment variable or add to .streamlit/secrets.toml")
    sys.exit(1)

os.environ['OPENAI_API_KEY'] = API_KEY

print("="*70)
print(" MANUFACTURER FINDER - QUICK START")
print("="*70)
print()
print("Choose an option:")
print()
print("1. 🌐 Launch Web Interface (Recommended)")
print("2. 💻 Analyze Excel file via command line")
print("3. 🧪 Run test analysis")
print("4. ℹ️  Show help")
print()

choice = input("Enter choice (1-4): ").strip()

if choice == '1':
    print()
    print("🚀 Launching web interface...")
    print("📱 Your browser will open automatically")
    print("Press Ctrl+C to stop")
    print()
    os.system('streamlit run app.py')

elif choice == '2':
    print()
    excel_file = input("Enter path to your Excel file (or press Enter for example_input.xlsx): ").strip()
    if not excel_file:
        excel_file = 'example_input.xlsx'
    
    output_file = input("Enter output filename (or press Enter for auto-generated): ").strip()
    
    cmd = f'python3 main.py "{excel_file}" --api-key "{API_KEY}"'
    if output_file:
        cmd += f' --output "{output_file}"'
    
    print()
    print(f"📊 Analyzing {excel_file}...")
    os.system(cmd)

elif choice == '3':
    print()
    print("🧪 Running test analysis...")
    os.system(f'python3 main.py example_input.xlsx --api-key "{API_KEY}" --output test_results.xlsx')

elif choice == '4':
    print()
    print("="*70)
    print(" HELP - HOW TO USE")
    print("="*70)
    print()
    print("📊 Prepare Your Excel File:")
    print("   Your file should have these columns:")
    print("   - MPN (Manufacturing Part Number)")
    print("   - Model Description (Product description)")
    print("   - Quantity (Amount needed)")
    print()
    print("🚀 Run the tool:")
    print("   Option 1: python3 quick_start.py  (this script)")
    print("   Option 2: streamlit run app.py    (web interface)")
    print("   Option 3: python3 main.py your_file.xlsx")
    print()
    print("📖 Full documentation: See README.md")
    print()

else:
    print("Invalid choice. Run the script again.")

