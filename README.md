# csv_analyzer
CSV Analyzer is a Django-based web application that allows users to upload CSV files, perform basic data analysis, and visualize the results. This project leverages the power of pandas for data processing and matplotlib/seaborn for data visualization.

# Django CSV Data Analysis
## Setup Instructions

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Run the development server:
    ```bash
    python manage.py runserver
    ```

5. Open your browser and go to `http://127.0.0.1:8000/data_analysis/upload/`.

## Sample CSV File

A sample CSV file `sample.csv` is provided for testing purposes.
