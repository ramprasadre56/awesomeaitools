"""Test Product Hunt API"""

from awesomeaitools.api.product_hunt_api import ph_api

# Test topics
print("Fetching topics...")
topics = ph_api.get_topics()
print(f"Found {len(topics)} topics")
for t in topics[:5]:
    print(f"  - {t.get('name')}: {t.get('postsCount')} posts")

# Test posts
print("\nFetching posts...")
posts = ph_api.get_posts(first=5)
print(f"Found {len(posts)} posts")
for p in posts[:5]:
    print(f"  - {p.get('name')}: {p.get('votesCount')} votes")
