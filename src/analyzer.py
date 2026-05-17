import logging
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


class DataAnalyzer:
    def __init__(self, dataframe):
        self.df = dataframe

    def generate_summary(self):
        """
        Generate summary statistics.
        """

        summary = {
            "total_records": len(self.df),
            "total_revenue": self.df["Revenue"].sum(),
            "average_revenue": self.df["Revenue"].mean(),
            "max_revenue": self.df["Revenue"].max(),
            "min_revenue": self.df["Revenue"].min(),
            "missing_values": self.df.isnull().sum().sum(),
        }

        logging.info("Summary statistics generated.")

        return summary

    def top_regions(self):
        """
        Analyze revenue by region.
        """

        return (
            self.df.groupby("Region")["Revenue"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )

    def monthly_sales(self):
        """
        Analyze monthly revenue trend.
        """

        return (
            self.df.groupby("Month")["Revenue"]
            .sum()
            .reset_index()
        )

    def generate_charts(self):
        """
        Generate charts for the report.
        """

        Path("charts").mkdir(exist_ok=True)

        # -------------------------
        # Revenue by Region Chart
        # -------------------------

        region_data = self.top_regions()

        plt.figure(figsize=(8, 5))

        plt.bar(
            region_data["Region"],
            region_data["Revenue"]
        )

        plt.title("Revenue by Region")
        plt.xlabel("Region")
        plt.ylabel("Revenue")

        plt.tight_layout()

        plt.savefig("charts/sales_by_region.png")

        plt.close()

        # -------------------------
        # Monthly Sales Trend
        # -------------------------

        month_order = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12,
        }

        monthly_data = self.monthly_sales()

        monthly_data["Month_Number"] = (
            monthly_data["Month"]
            .astype(str)
            .map(month_order)
        )

        monthly_data = monthly_data.sort_values(
            "Month_Number"
        )

        # Numeric positions for plotting

        months = list(range(len(monthly_data)))

        plt.figure(figsize=(8, 5))

        plt.plot(
            months,
            monthly_data["Revenue"],
            marker="o"
        )

        plt.xticks(
            months,
            monthly_data["Month"]
        )

        plt.title("Monthly Revenue Trend")
        plt.xlabel("Month")
        plt.ylabel("Revenue")

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.savefig("charts/monthly_sales.png")

        plt.close()

        logging.info("Charts generated successfully.")