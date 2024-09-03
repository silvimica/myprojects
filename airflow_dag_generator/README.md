# Airflow DAG Generator

## Description
This project automates the generation of Apache Airflow Directed Acyclic Graphs (DAGs) from an Excel file (`input.xlsx`). It reads task configurations and dependencies from the Excel sheet and dynamically creates a DAG file using the Jinja2 templating engine. The dag allows to transfer data from tables between clickhouse, postgres and mssql databases with the same structure. 

## Project Structure
- **`input.xlsx`**: Excel file containing the configuration for the DAG tasks and dependencies.
- **`jinja_dag_generator.py`**: Python script that reads the input from `input.xlsx` and generates the DAG using Jinja2 templates.
- **`templates/`**: Folder containing Jinja2 template files used for generating the DAG.
- **`README.md`**: This file. Describes the purpose, usage, and structure of the project.

## Dependencies
Make sure the following Python packages are installed:
- `pandas`: For reading and processing the Excel file.
- `jinja2`: For generating the DAG using templates.
- `apache-airflow`: For running and testing the generated DAGs (ensure Airflow is installed and properly configured).