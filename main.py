"""
Main entry point for Game of Thrones BI Dashboard application.

This module starts the application, initializes the main window,
and launches the CustomTkinter event loop.

The application is a simple BI-style dashboard that allows:
    - loading and analyzing battles dataset
    - filtering data by year, region, and search query
    - visualizing statistics and charts

Modules used:
    - customtkinter: UI framework
    - main_window: main application window

Author: Viktoria Chelpykh
Date: 2026-06-15
"""

import customtkinter as ctk
from main_window import MainWindow


def main():
    """
    Starts the BI dashboard application.

    Steps:
        1. Initialize main window
        2. Start GUI event loop

    Returns:
        None
    """

    # Optional global UI settings
    ctk.set_appearance_mode("dark")

    # Create application instance
    app = MainWindow()

    # Run application
    app.mainloop()


if __name__ == "__main__":
    main()