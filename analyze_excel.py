import pandas as pd
import os

# Read the Excel file
df = pd.read_excel('Final.xlsx')

print('=== EXCEL DATA ANALYSIS ===')
print(f'Total rows: {len(df)}')
print(f'Total columns: {len(df.columns)}')

print('\n=== SEGMENTS AND CATEGORIES ===')
# Group by Segment and Category
segment_categories = df.groupby(['Segment', 'Category']).size().reset_index(name='count')
print(segment_categories)

print('\n=== UNIQUE SEGMENTS ===')
for segment in df['Segment'].unique():
    if pd.notna(segment):
        print(f'\n--- {segment} ---')
        segment_data = df[df['Segment'] == segment]
        categories = segment_data['Category'].unique()
        for category in categories:
            if pd.notna(category):
                category_data = segment_data[segment_data['Category'] == category]
                subcategories = category_data['Sub-Category'].dropna().unique()
                products = category_data['Product'].dropna().unique()
                print(f'  Category: {category}')
                print(f'    Subcategories: {len(subcategories)} ({list(subcategories)[:3]}...)')
                print(f'    Products: {len(products)} items')

print('\n=== SAMPLE PRODUCTS ===')
print(df[['Segment', 'Category', 'Sub-Category', 'Product', 'Links']].head(10))