# Expense Survey Tool

## Description
A survey tool for collecting and analyzing income and expense data using Flask and MongoDB.

## Installation
1. Extract the zip folder.
2. Install dependencies:
    ```bash
    pip install flask pymongo pandas matplotlib seaborn
    ```
3. Run the Flask application:
    ```bash
    python app.py
    ```

## Data Processing
1. The data is stored in MongoDB.
2. A Python class processes the data and exports it to a CSV file.
3. Data analysis and visualizations are performed in a Jupyter notebook.

## Deployment
1. Follow AWS documentation to deploy the Flask application on AWS.

## Visualizations
- `highest_income.png`
- `gender_distribution.png`
