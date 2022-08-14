import pandas as pd


sales_data = {
    ('2012', 'Q1'): {
        ('North', 'Brand A'): 100,
        ("North", "Brand B"): 80,
        ("South", "Brand A"): 25,
        ("South", "Brand B"): 40},
    ("2012", "Q2"): {("North", "Brand A"): 30, ("South", "Brand B"): 50},
    ("2013", "Q1"): {
        ("North", "Brand A"): 80,
        ("North", "Brand B"): 10,
        ("South", "Brand B"): 25},
    ("2013", "Q2"): {
        ("North", "Brand A"): 70,
        ("North", "Brand B"): 50,
        ("South", "Brand A"): 35,
        ("South", "Brand B"): 40}}
sales_df = pd.DataFrame(sales_data)
print(sales_df)
                        
