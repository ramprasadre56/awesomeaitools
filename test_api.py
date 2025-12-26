"""Test Product Hunt Data"""

from awesomeaitools.api.product_hunt_api import get_categories, get_products

# Test categories
print("Fetching categories...")
categories = get_categories()
print(f"Found {len(categories)} categories")
for c in categories[:5]:
    print(f"  - {c.get('name')}: {c.get('postsCount')} posts")

# Test products
print("\nFetching products...")
products = get_products(limit=5)
print(f"Found {len(products)} products")
for p in products[:5]:
    print(f"  - {p.get('name')}: {p.get('votesCount')} votes")
