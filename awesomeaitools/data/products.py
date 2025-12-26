"""Products data for the Product Hunt clone."""

# Sample Products data matching Product Hunt style
PRODUCTS = [
    {
        "id": "hq0",
        "name": "hq0",
        "tagline": "Host meetings on your website instead of Zoom or Google Meet",
        "description": "Turn your website into a meeting room. No downloads, no sign-ups for guests.",
        "categories": ["Productivity", "Video", "Remote Work"],
        "icon": "📹",
        "upvotes": 342,
        "comments": 28,
        "url": "https://hq0.io",
        "featured": True
    },
    {
        "id": "supertools",
        "name": "Supertools",
        "tagline": "The best AI tools directory, organized and categorized",
        "description": "Browse hundreds of vetted AI tools for coding, marketing, design & more.",
        "categories": ["AI", "Productivity", "Developer Tools"],
        "icon": "🛠️",
        "upvotes": 567,
        "comments": 45,
        "url": "https://rundown.ai/tools",
        "featured": True
    },
    {
        "id": "gemma3n",
        "name": "Gemma 3n",
        "tagline": "Google's efficient on-device AI model for mobile and edge",
        "description": "Run powerful AI models directly on your phone or embedded device.",
        "categories": ["AI", "Developer Tools", "Mobile"],
        "icon": "💎",
        "upvotes": 892,
        "comments": 67,
        "url": "https://ai.google.dev/gemma",
        "featured": True
    },
    {
        "id": "ollama",
        "name": "Ollama",
        "tagline": "Run Llama 3, Mistral, and other LLMs locally",
        "description": "Get up and running with large language models locally on your machine.",
        "categories": ["AI", "Developer Tools", "Open Source"],
        "icon": "🦙",
        "upvotes": 1245,
        "comments": 89,
        "url": "https://ollama.ai",
        "featured": False
    },
    {
        "id": "reflex",
        "name": "Reflex",
        "tagline": "Build full-stack web apps in pure Python",
        "description": "Create beautiful, fast web applications without any JavaScript.",
        "categories": ["Developer Tools", "Python", "Web Development"],
        "icon": "⚡",
        "upvotes": 678,
        "comments": 42,
        "url": "https://reflex.dev",
        "featured": False
    },
    {
        "id": "webllm",
        "name": "WebLLM",
        "tagline": "Run LLMs directly in your browser with WebGPU",
        "description": "High-performance in-browser LLM inference engine using WebGPU.",
        "categories": ["AI", "Developer Tools", "Web"],
        "icon": "🌐",
        "upvotes": 456,
        "comments": 34,
        "url": "https://webllm.mlc.ai",
        "featured": False
    },
    {
        "id": "screenly",
        "name": "ScreenREC",
        "tagline": "Free online screen recorder, no download required",
        "description": "Record your screen instantly from your browser. No watermarks, no limits.",
        "categories": ["Productivity", "Video", "Tools"],
        "icon": "🎬",
        "upvotes": 234,
        "comments": 19,
        "url": "https://screen-rec.vercel.app",
        "featured": False
    },
    {
        "id": "cursor",
        "name": "Cursor",
        "tagline": "The AI-first code editor built for pair programming",
        "description": "Write, edit, and understand code faster with AI assistance built in.",
        "categories": ["AI", "Developer Tools", "Productivity"],
        "icon": "✏️",
        "upvotes": 2341,
        "comments": 156,
        "url": "https://cursor.sh",
        "featured": False
    },
]

# Trending forum threads for sidebar
TRENDING_THREADS = [
    {
        "id": 1,
        "title": "What AI tools are you using daily?",
        "replies": 234,
        "category": "AI"
    },
    {
        "id": 2,
        "title": "Best practices for launching on Product Hunt",
        "replies": 189,
        "category": "Launch"
    },
    {
        "id": 3,
        "title": "How do you validate your startup ideas?",
        "replies": 156,
        "category": "Startups"
    },
    {
        "id": 4,
        "title": "Remote work tools for 2025",
        "replies": 98,
        "category": "Tools"
    },
]
