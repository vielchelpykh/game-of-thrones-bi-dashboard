"""
Module for calculating basic statistics from Game of Thrones battles dataset.

This module provides simple BI metrics used in dashboard:
    - total number of battles
    - attacker wins count
    - defender wins count

It is used in KPI panel of the application.

Author: Viktoria Chelpykh
Date: 2026-06-15
"""

import pandas as pd


class StatisticsManager:
    """
    Provides statistical calculations for battles dataset.

    This class is used to compute KPI metrics for BI dashboard.
    All methods are static because no internal state is required.
    """

    @staticmethod
    def get_statistics(df: pd.DataFrame) -> dict:
        """
        Calculates main statistics from dataset.

        Metrics:
            - total number of battles
            - number of attacker wins
            - number of defender wins

        Args:
            df (pd.DataFrame): dataset containing battles data.
                               Expected column: "attacker_outcome"

        Returns:
            dict: dictionary with keys:
                - total (int)
                - attacker_wins (int)
                - defender_wins (int)
        """

        # ================= VALIDATION =================
        if df is None or df.empty:
            return {
                "total": 0,
                "attacker_wins": 0,
                "defender_wins": 0
            }

        total_battles = len(df)

        if "attacker_outcome" not in df.columns:
            return {
                "total": total_battles,
                "attacker_wins": 0,
                "defender_wins": 0
            }

        # ================= PROCESSING =================
        outcomes = df["attacker_outcome"].astype(str).str.lower()

        attacker_wins = (outcomes == "win").sum()
        defender_wins = (outcomes == "loss").sum()

        # ================= RESULT =================
        return {
            "total": int(total_battles),
            "attacker_wins": int(attacker_wins),
            "defender_wins": int(defender_wins)
        }