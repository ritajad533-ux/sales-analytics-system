def calculate_revenue(transactions):
    """Returns total revenue from all transactions."""
    return sum(t['Quantity'] * t['UnitPrice'] for t in transactions)

def get_region_statistics(transactions):
    """Calculates revenue and percentage share per region."""
    stats = {}
    total_rev = calculate_revenue(transactions)
    
    for t in transactions:
        reg = t['Region']
        rev = t['Quantity'] * t['UnitPrice']
        if reg not in stats:
            stats[reg] = {'revenue': 0, 'count': 0}
        stats[reg]['revenue'] += rev
        stats[reg]['count'] += 1
        
    for reg in stats:
        stats[reg]['percentage'] = (stats[reg]['revenue'] / total_rev) * 100 if total_rev > 0 else 0
        
    return stats

def get_low_performance_products(transactions, threshold=10):
    """Identifies products with total quantity below the threshold."""
    prod_counts = {}
    for t in transactions:
        name = t['ProductName']
        prod_counts[name] = prod_counts.get(name, 0) + t['Quantity']
        
    return [name for name, qty in prod_counts.items() if qty < threshold]