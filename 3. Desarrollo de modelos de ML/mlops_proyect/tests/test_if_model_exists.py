import os

import pytest


def test_joblib_file_exists():
    # Obtener la lista de archivos en el directorio actual
    files = os.listdir()

    # Filtrar los archivos .joblib
    joblib_files = [file for file in files if file.endswith(".joblib")]

    # Asegurarse de que hay al menos un archivo .joblib
    assert joblib_files


if __name__ == "__main__":
    pytest.main()
