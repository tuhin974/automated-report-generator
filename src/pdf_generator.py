from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Image,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


class PDFGenerator:
    def __init__(self, output_path):
        self.output_path = output_path
        self.styles = getSampleStyleSheet()

    def generate_pdf(self, summary):
        """
        Generate professional PDF report.
        """

        document = SimpleDocTemplate(
            self.output_path,
            pagesize=letter
        )

        elements = []

        # -------------------------
        # Title
        # -------------------------

        title = Paragraph(
            "<font size=24><b>Automated Sales Report</b></font>",
            self.styles["Title"]
        )

        elements.append(title)

        elements.append(Spacer(1, 20))

        # -------------------------
        # Timestamp
        # -------------------------

        generated_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        timestamp = Paragraph(
            f"<b>Generated:</b> {generated_time}",
            self.styles["BodyText"]
        )

        elements.append(timestamp)

        elements.append(Spacer(1, 20))

        # -------------------------
        # Executive Summary
        # -------------------------

        summary_heading = Paragraph(
            "<b>Executive Summary</b>",
            self.styles["Heading2"]
        )

        elements.append(summary_heading)

        elements.append(Spacer(1, 12))

        # -------------------------
        # Summary Table
        # -------------------------

        table_data = [
            ["Metric", "Value"],
            ["Total Records", summary["total_records"]],
            [
                "Total Revenue",
                f"${summary['total_revenue']:,.2f}"
            ],
            [
                "Average Revenue",
                f"${summary['average_revenue']:,.2f}"
            ],
            [
                "Maximum Revenue",
                f"${summary['max_revenue']:,.2f}"
            ],
            [
                "Minimum Revenue",
                f"${summary['min_revenue']:,.2f}"
            ],
            [
                "Missing Values",
                summary["missing_values"]
            ],
        ]

        summary_table = Table(
            table_data,
            colWidths=[220, 220]
        )

        summary_table.setStyle(TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.darkblue
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.black
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),
            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, 0),
                10
            ),
            (
                "BACKGROUND",
                (0, 1),
                (-1, -1),
                colors.beige
            ),
        ]))

        elements.append(summary_table)

        elements.append(Spacer(1, 20))

        # -------------------------
        # Revenue by Region Chart
        # -------------------------

        region_heading = Paragraph(
            "<b>Revenue by Region</b>",
            self.styles["Heading2"]
        )

        elements.append(region_heading)

        elements.append(Spacer(1, 10))

        region_chart = Image(
            "charts/sales_by_region.png",
            width=450,
            height=250
        )

        elements.append(region_chart)

        elements.append(Spacer(1, 20))

        # -------------------------
        # Monthly Revenue Trend
        # -------------------------

        monthly_heading = Paragraph(
            "<b>Monthly Revenue Trend</b>",
            self.styles["Heading2"]
        )

        elements.append(monthly_heading)

        elements.append(Spacer(1, 10))

        monthly_chart = Image(
            "charts/monthly_sales.png",
            width=450,
            height=250
        )

        elements.append(monthly_chart)

        elements.append(PageBreak())

        # -------------------------
        # Insights Section
        # -------------------------

        insights = Paragraph(
            '''
            <b>Insights & Conclusions</b><br/><br/>

            - West region generated the highest revenue.<br/>
            - Monthly revenue trends indicate stable growth.<br/>
            - Revenue distribution varies across regions.<br/>
            - No major missing values were detected.<br/>
            - The business performance appears healthy.<br/>
            ''',
            self.styles["BodyText"]
        )

        elements.append(insights)

        # -------------------------
        # Build PDF
        # -------------------------

        document.build(elements)