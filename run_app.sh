#!/bin/bash

# Manufacturer Finder Tool - Quick Launch Script
# This script launches the Streamlit web application

echo "=========================================="
echo "  Manufacturer Finder Tool"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

# Check if dependencies are installed
if ! python3 -c "import streamlit" &> /dev/null; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
    echo ""
fi

# Check for OpenAI API key
if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  Warning: OPENAI_API_KEY environment variable not set"
    echo "You can enter it in the web interface"
    echo ""
fi

# Launch the application
echo "🚀 Launching Manufacturer Finder Tool..."
echo "📱 The web interface will open in your browser"
echo "🔑 Enter your OpenAI API key in the sidebar if not set as environment variable"
echo ""
echo "Press Ctrl+C to stop the application"
echo ""

streamlit run app.py

