import logging
from pathlib import Path

from analyzer import DataAnalyzer
from data_loader import DataLoader
from pdf_generator import PDFGenerator


# -------------------------
# Logging Configuration
# -------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    """
    Main application workflow.
    """

    try:
        # -------------------------
        # File Paths
        # -------------------------

        data_path = "data/sample_data.csv"

        output_pdf = "output/generated_report.pdf"

        # Create output folder automatically

        Path("output").mkdir(exist_ok=True)

        # -------------------------
        # Load Data
        # -------------------------

        loader = DataLoader(data_path)

        dataframe = loader.load_data()

        # -------------------------
        # Analyze Data
        # -------------------------

        analyzer = DataAnalyzer(dataframe)

        summary = analyzer.generate_summary()

        analyzer.generate_charts()

        # -------------------------
        # Generate PDF
        # -------------------------

        pdf = PDFGenerator(output_pdf)

        pdf.generate_pdf(summary)

        logging.info(
            "PDF report generated successfully."
        )

    except Exception as error:

        logging.error(
            f"Application failed: {error}"
        )


if __name__ == "__main__":
    main()