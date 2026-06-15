"""
Module for data loading, filtering, and basic dataset operations.

This module represents the core data layer of the BI dashboard.
It handles all operations with the battles dataset, including:

    - loading CSV data
    - extracting filter values (years, regions)
    - filtering dataset by user parameters
    - calculating basic statistics

This class is the central data provider for UI and analytics modules.

Author: Student (HSE Project)
Date: 2026
"""

import pandas as pd


class DataManager:
    """
    Core data manager for BI dashboard.

    Responsibilities:
        - Load and store dataset
        - Provide filtering functionality
        - Provide unique values for UI filters
        - Compute basic dataset statistics
    """

    def __init__(self):
        """
        Initializes empty dataset.
        """
        self.df = pd.DataFrame()

    # ================= LOAD DATA =================

    def load_csv(self, file_path: str) -> pd.DataFrame:
        """
        Loads dataset from CSV file.

        Args:
            file_path (str): path to CSV file

        Returns:
            pd.DataFrame: loaded dataset
        """
        self.df = pd.read_csv(file_path).fillna("")
        return self.df

    # ================= FILTER OPTIONS =================

    def get_years(self) -> list:
        """
        Returns sorted list of available years in dataset.

        Returns:
            list: unique years as strings
        """
        if self.df.empty or "year" not in self.df.columns:
            return []

        return sorted(self.df["year"].astype(str).unique())

    def get_regions(self) -> list:
        """
        Returns sorted list of available regions in dataset.

        Returns:
            list: unique regions as strings
        """
        if self.df.empty or "region" not in self.df.columns:
            return []

        return sorted(self.df["region"].astype(str).unique())

    # ================= FILTER DATA =================

    def filter_data(
        self,
        year: str = None,
        region: str = None,
        battle_name: str = None
    ) -> pd.DataFrame:
        """
        Filters dataset by year, region and battle name.

        Args:
            year (str, optional): selected year filter
            region (str, optional): selected region filter
            battle_name (str, optional): search text for battle name

        Returns:
            pd.DataFrame: filtered dataset
        """

        if self.df.empty:
            return pd.DataFrame()

        df = self.df.copy()

        # -------- YEAR FILTER --------
        if year:
            df = df[df["year"].astype(str) == str(year)]

        # -------- REGION FILTER --------
        if region:
            df = df[df["region"].astype(str) == str(region)]

        # -------- SEARCH FILTER --------
        if battle_name:
            search = battle_name.lower()

            df = df[
                df.astype(str).apply(
                    lambda row: row.str.lower().str.contains(search).any(),
                    axis=1
                )
            ]

        return df

    # ================= STATISTICS =================

    def get_statistics(self, df: pd.DataFrame = None) -> dict:
        """
        Calculates basic KPI statistics.

        Args:
            df (pd.DataFrame, optional): dataset to analyze.
                                         If None, uses internal dataset.

        Returns:
            dict: statistics dictionary containing:
                - total (int)
                - attacker_wins (int)
                - defender_wins (int)
        """

        if df is None:
            df = self.df

        if df.empty:
            return {
                "total": 0,
                "attacker_wins": 0,
                "defender_wins": 0
            }

        if "attacker_outcome" not in df.columns:
            return {
                "total": len(df),
                "attacker_wins": 0,
                "defender_wins": 0
            }

        outcomes = df["attacker_outcome"].astype(str).str.lower()

        return {
            "total": int(len(df)),
            "attacker_wins": int((outcomes == "win").sum()),
            "defender_wins": int((outcomes == "loss").sum())
        }


# ================= DEBUG =================
if __name__ == "__main__":
    print("DATA_MANAGER LOADED SUCCESSFULLY")