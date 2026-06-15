"""
Module for GoT BI Dashboard application.

This module creates a graphical interface for analyzing battles dataset
(Game of Thrones). It includes data loading, filtering, visualization,
and interactive analytics dashboard.

Contains:
    MainWindow - main BI application window class

Author: Viktoria Chelpykh
Date: 2026-06-15
"""

import customtkinter as ctk
from tkinter import filedialog
from tkinter import ttk

from data_manager import DataManager
from plot_manager import PlotManager


class MainWindow(ctk.CTk):
    """
    Main application window for BI dashboard.

    Provides:
        - CSV data loading
        - filtering system (year, region, search)
        - statistics dashboard (KPI bar)
        - data table view
        - charts visualization
    """

    def __init__(self):
        super().__init__()

        self.setup_window()

        self.data_manager = DataManager()
        self.df = None
        self.filtered_df = None

        self.build_ui()

    # ================= WINDOW SETUP =================

    def setup_window(self):
        """
        Configures main application window settings.

        Returns:
            None
        """
        self.title("GoT BI Dashboard")
        self.geometry("1450x900")
        ctk.set_appearance_mode("dark")

    # ================= UI =================

    def build_ui(self):
        """
        Builds full UI layout.

        Returns:
            None
        """
        self.configure_grid()
        self.create_sidebar()
        self.create_main_area()

    def configure_grid(self):
        """
        Configures main grid layout.

        Returns:
            None
        """
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    # ================= SIDEBAR =================

    def create_sidebar(self):
        """
        Creates left control panel (sidebar).

        Returns:
            None
        """
        self.sidebar = ctk.CTkFrame(self, width=300, fg_color="#111418")
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.create_title()
        self.create_filters()
        self.create_data_buttons()
        self.create_analysis_buttons()

    def create_title(self):
        """
        Creates sidebar title.

        Returns:
            None
        """
        ctk.CTkLabel(
            self.sidebar,
            text="⚔ GOT BI PANEL",
            font=("Arial", 20, "bold")
        ).pack(pady=10)

    def create_filters(self):
        """
        Creates filter inputs (search, year, region).

        Returns:
            None
        """
        self.search = ctk.CTkEntry(self.sidebar, placeholder_text="SEARCH BATTLES")
        self.search.pack(fill="x", padx=10, pady=5)

        self.year = ctk.CTkComboBox(self.sidebar, values=["ALL YEARS"])
        self.year.set("ALL YEARS")
        self.year.pack(fill="x", padx=10, pady=5)

        self.region = ctk.CTkComboBox(self.sidebar, values=["ALL REGIONS"])
        self.region.set("ALL REGIONS")
        self.region.pack(fill="x", padx=10, pady=5)

    def create_data_buttons(self):
        """
        Creates data loading buttons.

        Returns:
            None
        """
        ctk.CTkLabel(self.sidebar, text="DATA", font=("Arial", 14, "bold")).pack(pady=(15, 5))

        ctk.CTkButton(
            self.sidebar,
            text="LOAD CSV",
            command=self.load_data,
            fg_color="#1f6aa5",
            font=("Arial", 13, "bold"),
            height=40
        ).pack(fill="x", padx=10, pady=5)

    def create_analysis_buttons(self):
        """
        Creates analytics and filtering buttons.

        Returns:
            None
        """
        ctk.CTkLabel(self.sidebar, text="ANALYTICS", font=("Arial", 14, "bold")).pack(pady=(15, 5))

        ctk.CTkButton(
            self.sidebar,
            text="APPLY FILTERS",
            command=self.apply_filters,
            fg_color="#2a7cc7",
            font=("Arial", 13, "bold"),
            height=40
        ).pack(fill="x", padx=10, pady=5)

        ctk.CTkButton(
            self.sidebar,
            text="RESET FILTERS",
            command=self.reset_filters,
            fg_color="#444",
            font=("Arial", 13, "bold"),
            height=40
        ).pack(fill="x", padx=10, pady=5)

        ctk.CTkButton(
            self.sidebar,
            text="REGIONS CHART",
            command=lambda: PlotManager.plot_regions(self.filtered_df),
            fg_color="#1f6aa5",
            font=("Arial", 13, "bold"),
            height=40
        ).pack(fill="x", padx=10, pady=5)

        ctk.CTkButton(
            self.sidebar,
            text="YEARS CHART",
            command=lambda: PlotManager.plot_years(self.filtered_df),
            fg_color="#1f6aa5",
            font=("Arial", 13, "bold"),
            height=40
        ).pack(fill="x", padx=10, pady=5)

    # ================= MAIN AREA =================

    def create_main_area(self):
        """
        Creates main dashboard area (KPI + table).

        Returns:
            None
        """
        self.main = ctk.CTkFrame(self, fg_color="#0b0d10")
        self.main.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.main.grid_rowconfigure(1, weight=1)
        self.main.grid_columnconfigure(0, weight=1)

        self.create_kpi_bar()
        self.create_table()

    # ================= KPI =================

    def create_kpi_bar(self):
        """
        Creates top KPI statistics bar.

        Returns:
            None
        """
        self.kpi_frame = ctk.CTkFrame(self.main, fg_color="#0b0d10")
        self.kpi_frame.grid(row=0, column=0, sticky="ew", pady=(5, 10))

        self.kpi_label = ctk.CTkLabel(
            self.kpi_frame,
            text="LOAD DATASET",
            font=("Arial", 20, "bold"),
            text_color="white"
        )
        self.kpi_label.pack(side="left")

    # ================= TABLE =================

    def create_table(self):
        """
        Creates data table view.

        Returns:
            None
        """
        self.table_frame = ctk.CTkFrame(self.main, fg_color="#111418")
        self.table_frame.grid(row=1, column=0, sticky="nsew")

        self.tree = ttk.Treeview(self.table_frame)
        self.tree.pack(fill="both", expand=True)

        self.apply_table_style()

    def apply_table_style(self):
        """
        Applies dark theme style to table.

        Returns:
            None
        """
        style = ttk.Style()
        style.theme_use("default")

        style.configure(
            "Treeview",
            background="#111418",
            foreground="white",
            fieldbackground="#111418",
            rowheight=28
        )

        style.configure(
            "Treeview.Heading",
            background="#1f1f1f",
            foreground="white",
            font=("Arial", 11, "bold")
        )

        style.map("Treeview", background=[("selected", "#2a7cc7")])

    # ================= DATA =================

    def load_data(self):
        """
        Loads CSV file.

        Returns:
            None
        """
        path = filedialog.askopenfilename()
        if not path:
            return

        self.df = self.data_manager.load_csv(path)
        self.filtered_df = self.df

        self.update_filters()
        self.refresh()

    def update_filters(self):
        """
        Updates filter dropdown values.

        Returns:
            None
        """
        if self.df is None:
            return

        self.year.configure(values=["ALL YEARS"] + list(self.data_manager.get_years()))
        self.region.configure(values=["ALL REGIONS"] + list(self.data_manager.get_regions()))

    # ================= FILTER LOGIC =================

    def apply_filters(self):
        """
        Applies filters to dataset.

        Returns:
            None
        """
        if self.df is None:
            return

        year = self.year.get()
        region = self.region.get()
        search = self.search.get()

        self.filtered_df = self.data_manager.filter_data(
            year=None if year == "ALL YEARS" else year,
            region=None if region == "ALL REGIONS" else region,
            battle_name=search if search else None
        )

        self.refresh()

    def reset_filters(self):
        """
        Resets all filters to default state.

        Returns:
            None
        """
        self.filtered_df = self.df

        self.search.delete(0, "end")
        self.year.set("ALL YEARS")
        self.region.set("ALL REGIONS")

        self.refresh()

    # ================= REFRESH =================

    def refresh(self):
        """
        Refreshes KPI and table view.

        Returns:
            None
        """
        if self.filtered_df is None:
            return

        stats = self.data_manager.get_statistics(self.filtered_df)

        self.kpi_label.configure(
            text=f"⚔ TOTAL: {stats['total']}   |   🔥 ATTACK: {stats['attacker_wins']}   |   🛡 DEFENSE: {stats['defender_wins']}"
        )

        self.render_table()

    def render_table(self):
        """
        Renders dataframe into table.

        Returns:
            None
        """
        df = self.filtered_df

        self.tree.delete(*self.tree.get_children())

        self.tree["columns"] = list(df.columns)
        self.tree["show"] = "headings"

        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))