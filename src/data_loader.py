import logging
import pandas as pd


class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            data = pd.read_csv(self.file_path)
            logging.info("Data loaded successfully.")
            return data

        except FileNotFoundError:
            logging.error("CSV file not found.")
            raise

        except Exception as error:
            logging.error(f"Error loading data: {error}")
            raise