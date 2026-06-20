"""
Module for data visualization (BI charts).

This module contains PlotManager class which is responsible for
creating different types of charts for Game of Thrones battles dataset.

Supported visualizations:
    - Battles by region (bar chart)
    - Battles by year (line chart)
    - Region vs Year heatmap
    - Battle outcomes distribution (pie chart)

Uses:
    - matplotlib for plotting
    - pandas for data aggregation

Author: Viktoria Chelpykh
Date: 2026-06-15
"""

import matplotlib.pyplot as plt
import pandas as pd


class PlotManager:
    """
    Class for generating analytical plots from battles dataset.
    All methods are static because no internal state is required.
    """

    # ================= REGIONS =================

    @staticmethod
    def plot_regions(df: pd.DataFrame):
        """
        Plots number of battles per region.

        Args:
            df (pd.DataFrame): dataset with "region" column

        Returns:
            None
        """

        if df is None or df.empty or "region" not in df.columns:
            return

        plt.figure(figsize=(10, 5))

        df["region"].value_counts().plot(kind="bar")

        plt.title("Battles by Region")
        plt.xlabel("Region")
        plt.ylabel("Number of Battles")

        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # ================= YEARS =================

    @staticmethod
    def plot_years(df: pd.DataFrame):
        """
        Plots number of battles per year.

        Args:
            df (pd.DataFrame): dataset with "year" column

        Returns:
            None
        """

        if df is None or df.empty or "year" not in df.columns:
            return

        plt.figure(figsize=(10, 5))

        # clean and convert year data
        data = df["year"].astype(str)
        data = data[data.str.isnumeric()].astype(int)

        counts = data.value_counts().sort_index()

        counts.plot(marker="o")

        plt.title("Battles by Year")
        plt.xlabel("Year")
        plt.ylabel("Number of Battles")

        plt.grid(True)
        plt.tight_layout()
        plt.show()
