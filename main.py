from data_handler import load_sales_data, clean_data
from api_processor import fetch_all_products, create_product_mapping
from analyzer import calculate_revenue, get_region_statistics, get_low_performance_products
from datetime import datetime

def run_system():
    print("--- SALES ANALYTICS SYSTEM ---")
    
    # 1. Load and Clean
    raw_data = load_sales_data('data/sales_data.txt')
    if not raw_data: return
    transactions = clean_data(raw_data)
    print(f"Loaded {len(transactions)} valid transactions.")

    # 2. API Enrichment
    api_data = fetch_all_products()
    mapping = create_product_mapping(api_data)
    
    enriched_data = []
    for t in transactions:
        info = mapping.get(t['ProductID'], {})
        t.update(info)
        t['API_Match'] = t['ProductID'] in mapping
        enriched_data.append(t)

    # 3. User Interaction (Filtering)
    reg_filter = input("Enter region to filter (North/South/East/West) or 'all': ").strip()
    filtered = [t for t in enriched_data if reg_filter.lower() == 'all' or t['Region'].lower() == reg_filter.lower()]

    # 4. Generate Report
    report_file = "output/sales_report.txt"
    os.makedirs('output', exist_ok=True)
    
    stats = get_region_statistics(filtered)
    low_perf = get_low_performance_products(filtered)
    
    with open(report_file, 'w') as f:
        f.write(f"SALES REPORT - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("-" * 30 + "\n")
        f.write(f"Total Revenue: ${calculate_revenue(filtered):,.2f}\n\n")
        f.write("REGIONAL PERFORMANCE:\n")
        for reg, data in stats.items():
            f.write(f"- {reg}: ${data['revenue']:,.2f} ({data['percentage']:.1f}%)\n")
        f.write(f"\nLow Performing Products: {', '.join(low_perf)}\n")

    print(f"Report generated successfully in {report_file}")

if __name__ == "__main__":
    import os
    run_system()