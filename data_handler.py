import os

def load_sales_data(filename):
    """Loads sales data with encoding handling."""
    encodings = ['utf-8', 'latin-1', 'cp1252']
    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as file:
                return file.readlines()
        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            print(f"Error: {filename} not found.")
            return None
    return None

def clean_data(raw_lines):
    """Cleans data based on assignment criteria."""
    cleaned_transactions = []
    header = raw_lines[0].strip().split('|')
    
    for line in raw_lines[1:]:
        parts = line.strip().split('|')
        if len(parts) != len(header):
            continue
            
        # Create dictionary
        row = dict(zip(header, parts))
        
        # Rule: Remove if Region is missing
        if not row['Region'] or row['Region'].strip() == "":
            continue
            
        # Rule: Remove if Quantity or UnitPrice ends with 'T'
        if row['Quantity'].endswith('T') or row['UnitPrice'].endswith('T'):
            continue
            
        try:
            # Rule: Clean commas from Product names and numeric fields
            row['ProductName'] = row['ProductName'].replace(',', '')
            row['Quantity'] = int(row['Quantity'].replace(',', ''))
            row['UnitPrice'] = float(row['UnitPrice'].replace(',', ''))
            cleaned_transactions.append(row)
        except ValueError:
            continue
            
    return cleaned_transactions