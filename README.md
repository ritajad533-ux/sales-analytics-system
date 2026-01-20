# Sales Analytics System
A Python-based data engineering project that processes e-commerce sales data, enriches it via the DummyJSON API, and generates a comprehensive performance report.

## Project Structure
- `data_handler.py`: Manages file I/O and applies cleaning rules (removing 'T' suffix, handling missing regions).
- `api_processor.py`: Integrates with the DummyJSON API to fetch product categories and ratings.
- `analyzer.py`: Performs calculations for revenue, regional performance, and low-performing products.
- `main.py`: The entry point that executes the full workflow.

## Requirements
- Python 3.x
- `requests` library (`pip install requests`)

## How to Run
1. Place the source data in `data/sales_data.txt`.
2. Run the system using `python main.py`.
3. View the generated report in `output/sales_report.txt`.
