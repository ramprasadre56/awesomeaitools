"""Product Hunt API Client with Fallback Data"""

import httpx
from typing import Optional, List, Dict, Any
from datetime import datetime

# Product Hunt API Configuration
PH_API_URL = "https://api.producthunt.com/v2/api/graphql"
PH_OAUTH_URL = "https://api.producthunt.com/v2/oauth/token"

# Your API credentials
PH_API_KEY = "HgDFis_Oq_fqPi-2b-tOp-xCnThpMW3Y-9cgkct1rdc"
PH_API_SECRET = "vphjJEKQ33N4R7Wyaus_ngMGjZfm0ajwlSpZi6hfxI"

# Fallback categories (from Product Hunt /categories page)
FALLBACK_CATEGORIES = [
    {
        "id": "ai",
        "name": "Artificial Intelligence",
        "slug": "artificial-intelligence",
        "icon": "🤖",
        "description": "AI and machine learning tools",
        "postsCount": 15420,
    },
    {
        "id": "developer-tools",
        "name": "Developer Tools",
        "slug": "developer-tools",
        "icon": "💻",
        "description": "Tools for developers",
        "postsCount": 12350,
    },
    {
        "id": "productivity",
        "name": "Productivity",
        "slug": "productivity",
        "icon": "⚡",
        "description": "Get more done",
        "postsCount": 11280,
    },
    {
        "id": "design-tools",
        "name": "Design Tools",
        "slug": "design-tools",
        "icon": "🎨",
        "description": "Design and creative tools",
        "postsCount": 9840,
    },
    {
        "id": "marketing",
        "name": "Marketing",
        "slug": "marketing",
        "icon": "📢",
        "description": "Marketing and growth",
        "postsCount": 8920,
    },
    {
        "id": "saas",
        "name": "SaaS",
        "slug": "saas",
        "icon": "☁️",
        "description": "Software as a Service",
        "postsCount": 8450,
    },
    {
        "id": "open-source",
        "name": "Open Source",
        "slug": "open-source",
        "icon": "🔓",
        "description": "Open source projects",
        "postsCount": 7890,
    },
    {
        "id": "chrome-extensions",
        "name": "Chrome Extensions",
        "slug": "chrome-extensions",
        "icon": "🌐",
        "description": "Browser extensions",
        "postsCount": 6780,
    },
    {
        "id": "fintech",
        "name": "Fintech",
        "slug": "fintech",
        "icon": "💰",
        "description": "Financial technology",
        "postsCount": 5670,
    },
    {
        "id": "health-fitness",
        "name": "Health & Fitness",
        "slug": "health-fitness",
        "icon": "🏃",
        "description": "Health and wellness",
        "postsCount": 4560,
    },
    {
        "id": "education",
        "name": "Education",
        "slug": "education",
        "icon": "📚",
        "description": "Learning tools",
        "postsCount": 4230,
    },
    {
        "id": "e-commerce",
        "name": "E-Commerce",
        "slug": "e-commerce",
        "icon": "🛒",
        "description": "Online shopping",
        "postsCount": 3980,
    },
    {
        "id": "social-media",
        "name": "Social Media Tools",
        "slug": "social-media-tools",
        "icon": "📱",
        "description": "Social networking",
        "postsCount": 3750,
    },
    {
        "id": "no-code",
        "name": "No-Code",
        "slug": "no-code",
        "icon": "🧩",
        "description": "Build without code",
        "postsCount": 3540,
    },
    {
        "id": "video",
        "name": "Video",
        "slug": "video",
        "icon": "🎬",
        "description": "Video tools",
        "postsCount": 3210,
    },
    {
        "id": "writing",
        "name": "Writing",
        "slug": "writing",
        "icon": "✍️",
        "description": "Writing and content",
        "postsCount": 2980,
    },
    {
        "id": "analytics",
        "name": "Analytics",
        "slug": "analytics",
        "icon": "📊",
        "description": "Data and analytics",
        "postsCount": 2750,
    },
    {
        "id": "automation",
        "name": "Automation",
        "slug": "automation",
        "icon": "🔄",
        "description": "Workflow automation",
        "postsCount": 2540,
    },
]

# Fallback products (top products from Product Hunt)
FALLBACK_PRODUCTS = [
    # AI Category
    {
        "id": "chatgpt-1",
        "name": "ChatGPT",
        "tagline": "Optimizing language models for dialogue",
        "description": "An AI chatbot developed by OpenAI",
        "votesCount": 8542,
        "commentsCount": 1234,
        "url": "https://chat.openai.com",
        "website": "https://chat.openai.com",
        "category": "ai",
        "thumbnail": None,
        "featured": True,
        "createdAt": "2022-11-30",
    },
    {
        "id": "claude-1",
        "name": "Claude 3.5 Sonnet",
        "tagline": "Anthropic's most intelligent AI model",
        "description": "Claude is trained to be helpful, harmless, and honest.",
        "votesCount": 5423,
        "commentsCount": 892,
        "url": "https://claude.ai",
        "website": "https://claude.ai",
        "category": "ai",
        "thumbnail": None,
        "featured": True,
        "createdAt": "2024-06-20",
    },
    {
        "id": "midjourney-1",
        "name": "Midjourney V6",
        "tagline": "AI art generator with photorealistic capabilities",
        "description": "Create stunning AI-generated images",
        "votesCount": 4892,
        "commentsCount": 756,
        "url": "https://midjourney.com",
        "website": "https://midjourney.com",
        "category": "ai",
        "thumbnail": None,
        "featured": True,
        "createdAt": "2024-02-15",
    },
    {
        "id": "perplexity-1",
        "name": "Perplexity AI",
        "tagline": "AI-powered answer engine with real-time citations",
        "description": "Get instant answers with sources",
        "votesCount": 4567,
        "commentsCount": 678,
        "url": "https://perplexity.ai",
        "website": "https://perplexity.ai",
        "category": "ai",
        "thumbnail": None,
        "featured": True,
        "createdAt": "2023-08-15",
    },
    {
        "id": "cursor-1",
        "name": "Cursor",
        "tagline": "The AI-first code editor built for pair programming",
        "description": "Build software faster with AI",
        "votesCount": 4234,
        "commentsCount": 567,
        "url": "https://cursor.sh",
        "website": "https://cursor.sh",
        "category": "ai",
        "thumbnail": None,
        "featured": True,
        "createdAt": "2024-01-10",
    },
    {
        "id": "elevenlabs-1",
        "name": "ElevenLabs",
        "tagline": "Prime AI text to speech and voice cloning",
        "description": "Create natural-sounding AI voices",
        "votesCount": 3987,
        "commentsCount": 534,
        "url": "https://elevenlabs.io",
        "website": "https://elevenlabs.io",
        "category": "ai",
        "thumbnail": None,
        "featured": False,
        "createdAt": "2023-06-20",
    },
    {
        "id": "runway-1",
        "name": "Runway Gen-3 Alpha",
        "tagline": "Next-gen AI video generation",
        "description": "Create cinematic AI videos",
        "votesCount": 3756,
        "commentsCount": 489,
        "url": "https://runway.ml",
        "website": "https://runway.ml",
        "category": "ai",
        "thumbnail": None,
        "featured": False,
        "createdAt": "2024-06-17",
    },
    {
        "id": "suno-1",
        "name": "Suno AI",
        "tagline": "Make any song you can imagine",
        "description": "AI-powered music creation",
        "votesCount": 3542,
        "commentsCount": 423,
        "url": "https://suno.ai",
        "website": "https://suno.ai",
        "category": "ai",
        "thumbnail": None,
        "featured": False,
        "createdAt": "2024-03-20",
    },
    # Developer Tools
    {
        "id": "vercel-1",
        "name": "Vercel",
        "tagline": "Develop. Preview. Ship.",
        "description": "The platform for frontend developers",
        "votesCount": 5678,
        "commentsCount": 789,
        "url": "https://vercel.com",
        "website": "https://vercel.com",
        "category": "developer-tools",
        "thumbnail": None,
        "featured": True,
        "createdAt": "2020-04-21",
    },
    {
        "id": "supabase-1",
        "name": "Supabase",
        "tagline": "The open source Firebase alternative",
        "description": "Build in a weekend, scale to millions",
        "votesCount": 4567,
        "commentsCount": 654,
        "url": "https://supabase.com",
        "website": "https://supabase.com",
        "category": "developer-tools",
        "thumbnail": None,
        "featured": True,
        "createdAt": "2020-06-01",
    },
    {
        "id": "railway-1",
        "name": "Railway",
        "tagline": "Instant deployments, effortless scaling",
        "description": "Deploy code in seconds",
        "votesCount": 3456,
        "commentsCount": 456,
        "url": "https://railway.app",
        "website": "https://railway.app",
        "category": "developer-tools",
        "thumbnail": None,
        "featured": False,
        "createdAt": "2021-02-15",
    },
    {
        "id": "planetscale-1",
        "name": "PlanetScale",
        "tagline": "The database for developers",
        "description": "Serverless MySQL platform",
        "votesCount": 3234,
        "commentsCount": 398,
        "url": "https://planetscale.com",
        "website": "https://planetscale.com",
        "category": "developer-tools",
        "thumbnail": None,
        "featured": False,
        "createdAt": "2021-05-01",
    },
    {
        "id": "neon-1",
        "name": "Neon",
        "tagline": "Serverless Postgres",
        "description": "The database you love, on a serverless platform",
        "votesCount": 2987,
        "commentsCount": 345,
        "url": "https://neon.tech",
        "website": "https://neon.tech",
        "category": "developer-tools",
        "thumbnail": None,
        "featured": False,
        "createdAt": "2022-09-15",
    },
    # Productivity
    {
        "id": "notion-1",
        "name": "Notion",
        "tagline": "All-in-one workspace",
        "description": "Write, plan, collaborate, and organize",
        "votesCount": 7890,
        "commentsCount": 1234,
        "url": "https://notion.so",
        "website": "https://notion.so",
        "category": "productivity",
        "thumbnail": None,
        "featured": True,
        "createdAt": "2018-03-15",
    },
    {
        "id": "linear-1",
        "name": "Linear",
        "tagline": "The issue tracking tool you'll enjoy using",
        "description": "Streamline software project management",
        "votesCount": 5678,
        "commentsCount": 789,
        "url": "https://linear.app",
        "website": "https://linear.app",
        "category": "productivity",
        "thumbnail": None,
        "featured": True,
        "createdAt": "2019-11-15",
    },
    {
        "id": "obsidian-1",
        "name": "Obsidian",
        "tagline": "A second brain for you, forever",
        "description": "Private and flexible note-taking",
        "votesCount": 4567,
        "commentsCount": 654,
        "url": "https://obsidian.md",
        "website": "https://obsidian.md",
        "category": "productivity",
        "thumbnail": None,
        "featured": False,
        "createdAt": "2020-07-15",
    },
    {
        "id": "raycast-1",
        "name": "Raycast",
        "tagline": "A blazingly fast, totally extendable launcher",
        "description": "Speed up your workflow",
        "votesCount": 4234,
        "commentsCount": 567,
        "url": "https://raycast.com",
        "website": "https://raycast.com",
        "category": "productivity",
        "thumbnail": None,
        "featured": False,
        "createdAt": "2020-06-15",
    },
    {
        "id": "cron-1",
        "name": "Cron",
        "tagline": "The calendar for power users",
        "description": "Next-generation calendar",
        "votesCount": 3456,
        "commentsCount": 456,
        "url": "https://cron.com",
        "website": "https://cron.com",
        "category": "productivity",
        "thumbnail": None,
        "featured": False,
        "createdAt": "2021-03-15",
    },
    # Design Tools
    {
        "id": "figma-1",
        "name": "Figma",
        "tagline": "Where teams design together",
        "description": "Collaborative design tool",
        "votesCount": 8234,
        "commentsCount": 1456,
        "url": "https://figma.com",
        "website": "https://figma.com",
        "category": "design-tools",
        "thumbnail": None,
        "featured": True,
        "createdAt": "2016-09-27",
    },
    {
        "id": "framer-1",
        "name": "Framer",
        "tagline": "Design and publish stunning sites",
        "description": "Build responsive websites visually",
        "votesCount": 4567,
        "commentsCount": 678,
        "url": "https://framer.com",
        "website": "https://framer.com",
        "category": "design-tools",
        "thumbnail": None,
        "featured": True,
        "createdAt": "2018-10-16",
    },
    {
        "id": "spline-1",
        "name": "Spline",
        "tagline": "Design amazing 3D experiences for the web",
        "description": "Create 3D designs without code",
        "votesCount": 3456,
        "commentsCount": 489,
        "url": "https://spline.design",
        "website": "https://spline.design",
        "category": "design-tools",
        "thumbnail": None,
        "featured": False,
        "createdAt": "2021-05-04",
    },
    {
        "id": "rive-1",
        "name": "Rive",
        "tagline": "Create and ship interactive animations",
        "description": "Real-time interactive design",
        "votesCount": 2987,
        "commentsCount": 378,
        "url": "https://rive.app",
        "website": "https://rive.app",
        "category": "design-tools",
        "thumbnail": None,
        "featured": False,
        "createdAt": "2020-08-10",
    },
    # Marketing
    {
        "id": "beehiiv-1",
        "name": "beehiiv",
        "tagline": "Newsletter platform built for growth",
        "description": "Scale, monetize, and delight your subscribers",
        "votesCount": 4567,
        "commentsCount": 567,
        "url": "https://beehiiv.com",
        "website": "https://beehiiv.com",
        "category": "marketing",
        "thumbnail": None,
        "featured": True,
        "createdAt": "2022-05-15",
    },
    {
        "id": "dub-1",
        "name": "Dub",
        "tagline": "Open-source link management for modern marketers",
        "description": "Create, share, and track short links",
        "votesCount": 3456,
        "commentsCount": 456,
        "url": "https://dub.co",
        "website": "https://dub.co",
        "category": "marketing",
        "thumbnail": None,
        "featured": True,
        "createdAt": "2023-02-01",
    },
    {
        "id": "convertkit-1",
        "name": "ConvertKit",
        "tagline": "The creator marketing platform",
        "description": "Grow your audience and sell digital products",
        "votesCount": 2987,
        "commentsCount": 378,
        "url": "https://convertkit.com",
        "website": "https://convertkit.com",
        "category": "marketing",
        "thumbnail": None,
        "featured": False,
        "createdAt": "2015-01-15",
    },
    # Open Source
    {
        "id": "cal-1",
        "name": "Cal.com",
        "tagline": "Scheduling infrastructure for everyone",
        "description": "The open source Calendly alternative",
        "votesCount": 4567,
        "commentsCount": 567,
        "url": "https://cal.com",
        "website": "https://cal.com",
        "category": "open-source",
        "thumbnail": None,
        "featured": True,
        "createdAt": "2021-06-30",
    },
    {
        "id": "documenso-1",
        "name": "Documenso",
        "tagline": "The open source DocuSign alternative",
        "description": "Beautiful, open-source signing",
        "votesCount": 3456,
        "commentsCount": 456,
        "url": "https://documenso.com",
        "website": "https://documenso.com",
        "category": "open-source",
        "thumbnail": None,
        "featured": True,
        "createdAt": "2023-03-15",
    },
    {
        "id": "infisical-1",
        "name": "Infisical",
        "tagline": "Open-source secret management",
        "description": "Sync secrets across your team",
        "votesCount": 2987,
        "commentsCount": 378,
        "url": "https://infisical.com",
        "website": "https://infisical.com",
        "category": "open-source",
        "thumbnail": None,
        "featured": False,
        "createdAt": "2022-11-15",
    },
]


class ProductHuntAPI:
    """Product Hunt API Client with fallback data."""

    def __init__(self):
        self.url = PH_API_URL
        self.access_token = None
        self.api_available = False
        self._try_authenticate()

    def _try_authenticate(self):
        """Try to get access token using client credentials."""
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.post(
                    PH_OAUTH_URL,
                    data={
                        "client_id": PH_API_KEY,
                        "client_secret": PH_API_SECRET,
                        "grant_type": "client_credentials",
                    },
                )
                if response.status_code == 200:
                    data = response.json()
                    self.access_token = data.get("access_token")
                    self.api_available = True
                    print("✓ Product Hunt API connected!")
                else:
                    print(f"API auth failed, using fallback data")
                    self.api_available = False
        except Exception as e:
            print(f"API unavailable, using fallback data")
            self.api_available = False

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

    def _execute_query(
        self, query: str, variables: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """Execute a GraphQL query."""
        if not self.api_available:
            return {"data": None}

        payload = {"query": query}
        if variables:
            payload["variables"] = variables

        try:
            with httpx.Client(timeout=15.0) as client:
                response = client.post(
                    self.url, headers=self._get_headers(), json=payload
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"API query failed: {e}")
            return {"data": None}

    def get_topics(self) -> List[Dict]:
        """Get topics/categories."""
        if self.api_available:
            query = """
            query {
                topics(first: 20) {
                    edges { node { id name slug description postsCount } }
                }
            }
            """
            result = self._execute_query(query)
            if result.get("data") and result["data"].get("topics"):
                return [edge["node"] for edge in result["data"]["topics"]["edges"]]

        # Use fallback data
        return FALLBACK_CATEGORIES

    def get_posts(self, first: int = 20, topic: Optional[str] = None) -> List[Dict]:
        """Get posts/products."""
        if self.api_available:
            query = """
            query GetPosts($first: Int!) {
                posts(first: $first, order: VOTES) {
                    edges { 
                        node { 
                            id name tagline description url votesCount commentsCount 
                            website thumbnail { url }
                            topics { edges { node { name slug } } }
                        } 
                    }
                }
            }
            """
            result = self._execute_query(query, {"first": first})
            if result.get("data") and result["data"].get("posts"):
                return [edge["node"] for edge in result["data"]["posts"]["edges"]]

        # Use fallback data, optionally filtered by topic
        products = FALLBACK_PRODUCTS
        if topic and topic != "all":
            products = [p for p in products if p.get("category") == topic]
        return products[:first]


# Singleton instance
ph_api = ProductHuntAPI()


def get_categories() -> List[Dict]:
    """Get categories from API or fallback."""
    return ph_api.get_topics()


def get_products(category: Optional[str] = None, limit: int = 20) -> List[Dict]:
    """Get products from API or fallback."""
    return ph_api.get_posts(first=limit, topic=category)
