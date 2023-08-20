import zipfile

import pandas as pd

class Loading:

    def __init__(self, model_path):
        self.model_path = model_path

    def loadingData(p1):
        """
            Unzipping and loading data
        """
        # Define the name of the ZIP file you want to extract
        zip_file = p1 + "creditcard.zip"

        # Create an `Zipfile` object for the ZIP file
        with zipfile.ZipFile(zip_file, "r") as zip_ref:

            # Get the file list in the ZIP file
            files = zip_ref.namelist()

            # Itera on the files in the ZIP file
            for file in files:

                # If the file is a CSV file, extra be the current directory
                if file.endswith(".csv"):
                    with zip_ref.open(file) as f:
                        with open(file, "wb") as out_file:
                            out_file.write(f.read())

        df = pd.read_csv(zip_file)
        return df
