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

    # ================= HEATMAP =================

    @staticmethod
    def plot_heatmap(df: pd.DataFrame):
        """
        Plots heatmap of battles distribution by region and year.

        Args:
            df (pd.DataFrame): dataset with "region" and "year"

        Returns:
            None
        """

        if df is None or df.empty:
            return

        if "region" not in df.columns or "year" not in df.columns:
            return

        pivot = pd.pivot_table(
            df,
            index="region",
            columns="year",
            aggfunc="size",
            fill_value=0
        )

        plt.figure(figsize=(12, 6))

        plt.imshow(pivot, aspect="auto")

        plt.title("Heatmap: Region vs Year")
        plt.xlabel("Year")
        plt.ylabel("Region")

        plt.yticks(range(len(pivot.index)), pivot.index)
        plt.xticks(range(len(pivot.columns)), pivot.columns, rotation=90)

        plt.colorbar(label="Number of Battles")
        plt.tight_layout()
        plt.show()

    # ================= OUTCOMES =================

    @staticmethod
    def plot_outcomes(df: pd.DataFrame):
        """
        Plots distribution of battle outcomes.

        Args:
            df (pd.DataFrame): dataset with "attacker_outcome" column

        Returns:
            None
        """

        if df is None or df.empty or "attacker_outcome" not in df.columns:
            return

        plt.figure(figsize=(6, 6))

        df["attacker_outcome"].value_counts().plot(
            kind="pie",
            autopct="%1.1f%%"
        )

        plt.title("Battle Outcomes")
        plt.ylabel("")
        plt.tight_layout()
        plt.show()