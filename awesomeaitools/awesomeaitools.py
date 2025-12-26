"""
Awesome AI Tools - Production App with Product Hunt API

Features:
- Rundown AI Tab: 70+ tools from rundown.ai
- Product Hunt Tab: Real API integration with fallback data
- Category filtering with 18 categories
- Upvote functionality
- Responsive design
"""

import reflex as rx
from typing import List

from .data.rundown_tools import RUNDOWN_TOOLS, RUNDOWN_CATEGORIES
from .api.product_hunt_api import (
    get_categories,
    get_products,
    FALLBACK_CATEGORIES,
    FALLBACK_PRODUCTS,
)


# ============================================================================
# STATE MANAGEMENT
# ============================================================================


class AppState(rx.State):
    """Application state."""

    # Tab state
    active_tab: str = "rundown"

    # Rundown state
    rundown_category: str = "All"
    rundown_view: str = "grid"

    # Product Hunt state
    ph_category: str = "all"
    upvoted_products: List[str] = []

    def set_tab(self, tab: str):
        self.active_tab = tab

    def set_rundown_category(self, category: str):
        self.rundown_category = category

    def set_rundown_view(self, view: str):
        self.rundown_view = view

    def set_ph_category(self, category: str):
        self.ph_category = category

    def toggle_upvote(self, product_id: str):
        if product_id in self.upvoted_products:
            self.upvoted_products.remove(product_id)
        else:
            self.upvoted_products.append(product_id)


# Get categories and products from API/fallback
PH_CATEGORIES = get_categories()
PH_PRODUCTS = get_products(limit=30)


# ============================================================================
# HEADER
# ============================================================================


def header() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Logo
            rx.hstack(
                rx.box(
                    rx.icon("sparkles", size=20, color="white"),
                    width="36px",
                    height="36px",
                    background="linear-gradient(135deg, #ff6154 0%, #ff9b52 100%)",
                    border_radius="10px",
                    display="flex",
                    align_items="center",
                    justify="center",
                ),
                rx.text(
                    "Awesome AI Tools",
                    font_weight="700",
                    font_size="18px",
                    color="#171717",
                ),
                spacing="3",
                align_items="center",
            ),
            # Tabs
            rx.hstack(
                rx.button(
                    "Rundown AI",
                    on_click=lambda: AppState.set_tab("rundown"),
                    variant="ghost",
                    size="2",
                    background=rx.cond(
                        AppState.active_tab == "rundown", "#171717", "transparent"
                    ),
                    color=rx.cond(AppState.active_tab == "rundown", "white", "#666"),
                    border_radius="8px",
                    cursor="pointer",
                ),
                rx.button(
                    "Product Hunt",
                    on_click=lambda: AppState.set_tab("producthunt"),
                    variant="ghost",
                    size="2",
                    background=rx.cond(
                        AppState.active_tab == "producthunt", "#ff6154", "transparent"
                    ),
                    color=rx.cond(
                        AppState.active_tab == "producthunt", "white", "#666"
                    ),
                    border_radius="8px",
                    cursor="pointer",
                ),
                spacing="2",
                background="#f5f5f5",
                padding="4px",
                border_radius="10px",
            ),
            rx.spacer(),
            rx.button(
                rx.icon("plus", size=14),
                "Submit",
                size="2",
                background="#ff6154",
                color="white",
                cursor="pointer",
                display=["none", "none", "flex"],
            ),
            width="100%",
            max_width="1400px",
            margin="0 auto",
            padding_x="24px",
            gap="4",
        ),
        width="100%",
        padding_y="12px",
        border_bottom="1px solid #eee",
        background="white",
        position="sticky",
        top="0",
        z_index="100",
    )


# ============================================================================
# RUNDOWN TAB
# ============================================================================


def rundown_hero() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Discover the best AI tools",
                size="7",
                font_weight="700",
                color="#171717",
            ),
            rx.text(
                f"Browse {len(RUNDOWN_TOOLS)}+ vetted AI tools for coding, marketing, design & more.",
                color="#666",
                font_size="14px",
            ),
            spacing="2",
            align_items="center",
            padding_y="20px",
        ),
        background="white",
    )


def rundown_filters() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                *[
                    rx.button(
                        cat,
                        on_click=lambda c=cat: AppState.set_rundown_category(c),
                        variant="ghost",
                        size="1",
                        background=rx.cond(
                            AppState.rundown_category == cat, "#171717", "white"
                        ),
                        color=rx.cond(
                            AppState.rundown_category == cat, "white", "#171717"
                        ),
                        border="1px solid #e5e5e5",
                        border_radius="20px",
                        font_size="11px",
                        cursor="pointer",
                    )
                    for cat in RUNDOWN_CATEGORIES[:8]
                ],
                spacing="2",
                flex_wrap="wrap",
            ),
            rx.spacer(),
            rx.hstack(
                rx.button(
                    rx.icon("layout-grid", size=14),
                    variant="ghost",
                    size="1",
                    on_click=lambda: AppState.set_rundown_view("grid"),
                    background=rx.cond(
                        AppState.rundown_view == "grid", "#eee", "transparent"
                    ),
                    cursor="pointer",
                ),
                rx.button(
                    rx.icon("list", size=14),
                    variant="ghost",
                    size="1",
                    on_click=lambda: AppState.set_rundown_view("list"),
                    background=rx.cond(
                        AppState.rundown_view == "list", "#eee", "transparent"
                    ),
                    cursor="pointer",
                ),
                spacing="1",
                background="#f5f5f5",
                padding="3px",
                border_radius="6px",
            ),
        ),
        max_width="1400px",
        margin="0 auto",
        padding="12px 24px",
        background="white",
        border_bottom="1px solid #eee",
    )


def rundown_card(tool: dict) -> rx.Component:
    return rx.link(
        rx.box(
            rx.hstack(
                rx.box(
                    rx.text(tool["icon"], font_size="20px"),
                    width="40px",
                    height="40px",
                    background="#f5f5f5",
                    border_radius="10px",
                    display="flex",
                    align_items="center",
                    justify="center",
                ),
                rx.vstack(
                    rx.text(
                        tool["name"],
                        font_weight="600",
                        font_size="13px",
                        color="#171717",
                    ),
                    rx.text(
                        tool["description"][:60] + "...", color="#666", font_size="11px"
                    ),
                    spacing="0",
                    align_items="start",
                    flex="1",
                ),
                spacing="3",
                width="100%",
            ),
            background="white",
            border="1px solid #eee",
            border_radius="10px",
            padding="12px",
            cursor="pointer",
            _hover={"box_shadow": "0 2px 8px rgba(0,0,0,0.05)", "border_color": "#ddd"},
        ),
        href=tool["url"],
        is_external=True,
        style={"text_decoration": "none"},
    )


def rundown_grid() -> rx.Component:
    return rx.box(
        rx.cond(
            AppState.rundown_view == "grid",
            rx.box(
                *[rundown_card(t) for t in RUNDOWN_TOOLS],
                display="grid",
                grid_template_columns=[
                    "1fr",
                    "repeat(2, 1fr)",
                    "repeat(3, 1fr)",
                    "repeat(4, 1fr)",
                ],
                gap="12px",
            ),
            rx.vstack(
                *[rundown_card(t) for t in RUNDOWN_TOOLS], spacing="2", width="100%"
            ),
        ),
        max_width="1400px",
        margin="0 auto",
        padding="20px 24px",
    )


def rundown_tab() -> rx.Component:
    return rx.box(
        rundown_hero(),
        rundown_filters(),
        rundown_grid(),
        background="#fafafa",
        min_height="calc(100vh - 60px)",
    )


# ============================================================================
# PRODUCT HUNT TAB
# ============================================================================


def ph_category_item(cat: dict) -> rx.Component:
    icon = cat.get("icon", "📦")
    count = cat.get("postsCount", 0)
    return rx.box(
        rx.hstack(
            rx.text(icon, font_size="16px"),
            rx.vstack(
                rx.text(
                    cat["name"], font_weight="500", font_size="12px", color="#171717"
                ),
                rx.text(f"{count:,} products", color="#999", font_size="10px"),
                spacing="0",
                align_items="start",
            ),
            spacing="3",
            width="100%",
        ),
        padding="8px 10px",
        border_radius="8px",
        cursor="pointer",
        background=rx.cond(AppState.ph_category == cat["id"], "#fff5f4", "transparent"),
        border=rx.cond(
            AppState.ph_category == cat["id"],
            "1px solid #ff6154",
            "1px solid transparent",
        ),
        on_click=lambda c=cat["id"]: AppState.set_ph_category(c),
        _hover={"background": "#f8f8f8"},
    )


def ph_sidebar() -> rx.Component:
    return rx.box(
        rx.vstack(
            # All products
            rx.box(
                rx.hstack(
                    rx.text("🏆", font_size="16px"),
                    rx.vstack(
                        rx.text("All Products", font_weight="500", font_size="12px"),
                        rx.text(
                            f"{len(PH_PRODUCTS)} products",
                            color="#999",
                            font_size="10px",
                        ),
                        spacing="0",
                        align_items="start",
                    ),
                    spacing="3",
                ),
                padding="8px 10px",
                border_radius="8px",
                cursor="pointer",
                background=rx.cond(
                    AppState.ph_category == "all", "#fff5f4", "transparent"
                ),
                border=rx.cond(
                    AppState.ph_category == "all",
                    "1px solid #ff6154",
                    "1px solid transparent",
                ),
                on_click=lambda: AppState.set_ph_category("all"),
                _hover={"background": "#f8f8f8"},
            ),
            rx.divider(margin_y="8px"),
            rx.text(
                "CATEGORIES",
                font_size="10px",
                font_weight="600",
                color="#999",
                padding_x="10px",
            ),
            *[ph_category_item(c) for c in PH_CATEGORIES],
            spacing="1",
            width="100%",
        ),
        background="white",
        border="1px solid #eee",
        border_radius="12px",
        padding="10px 6px",
        width="240px",
        position="sticky",
        top="80px",
        max_height="calc(100vh - 100px)",
        overflow_y="auto",
    )


def ph_product_card(product: dict) -> rx.Component:
    return rx.link(
        rx.box(
            rx.hstack(
                # Icon
                rx.box(
                    rx.text("🚀", font_size="24px"),
                    width="52px",
                    height="52px",
                    background="#f8f8f8",
                    border_radius="12px",
                    display="flex",
                    align_items="center",
                    justify="center",
                ),
                # Content
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            product["name"],
                            font_weight="600",
                            font_size="14px",
                            color="#171717",
                        ),
                        rx.cond(
                            product.get("featured", False),
                            rx.badge("Featured", color_scheme="orange", size="1"),
                            rx.box(),
                        ),
                        spacing="2",
                    ),
                    rx.text(product["tagline"], color="#666", font_size="12px"),
                    rx.hstack(
                        rx.hstack(
                            rx.icon("message-circle", size=11, color="#999"),
                            rx.text(
                                str(product.get("commentsCount", 0)),
                                color="#999",
                                font_size="10px",
                            ),
                            spacing="1",
                        ),
                        spacing="2",
                    ),
                    spacing="1",
                    align_items="start",
                    flex="1",
                ),
                # Upvote
                rx.button(
                    rx.vstack(
                        rx.icon("chevron-up", size=14),
                        rx.text(
                            str(product.get("votesCount", 0)),
                            font_size="11px",
                            font_weight="600",
                        ),
                        spacing="0",
                    ),
                    variant="outline",
                    size="2",
                    min_width="54px",
                    height="54px",
                    border_radius="10px",
                    cursor="pointer",
                    on_click=lambda p=product["id"]: AppState.toggle_upvote(p),
                    background=rx.cond(
                        AppState.upvoted_products.contains(product["id"]),
                        "#fff5f4",
                        "white",
                    ),
                    color=rx.cond(
                        AppState.upvoted_products.contains(product["id"]),
                        "#ff6154",
                        "#666",
                    ),
                    border_color=rx.cond(
                        AppState.upvoted_products.contains(product["id"]),
                        "#ff6154",
                        "#e5e5e5",
                    ),
                    _hover={"border_color": "#ff6154", "color": "#ff6154"},
                ),
                spacing="4",
                width="100%",
            ),
            background="white",
            border="1px solid #eee",
            border_radius="12px",
            padding="14px",
            cursor="pointer",
            _hover={
                "box_shadow": "0 4px 16px rgba(0,0,0,0.05)",
                "border_color": "#ff6154",
            },
        ),
        href=product.get("url", product.get("website", "#")),
        is_external=True,
        style={"text_decoration": "none"},
    )


def ph_products_list() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text("🔥 Top Products", font_weight="600", font_size="15px"),
            rx.spacer(),
            rx.text(f"{len(PH_PRODUCTS)} products", color="#999", font_size="11px"),
            width="100%",
            padding_bottom="10px",
        ),
        *[ph_product_card(p) for p in PH_PRODUCTS],
        spacing="3",
        width="100%",
    )


def ph_discussions() -> rx.Component:
    discussions = [
        {
            "title": "What's the best AI tool you've discovered?",
            "category": "AI",
            "replies": 234,
        },
        {
            "title": "How do you monetize your side project?",
            "category": "Startup",
            "replies": 187,
        },
        {
            "title": "Favorite developer tools for 2024?",
            "category": "Dev",
            "replies": 156,
        },
    ]
    return rx.box(
        rx.vstack(
            rx.text("💬 Trending", font_weight="600", font_size="13px"),
            rx.divider(margin_y="8px"),
            *[
                rx.box(
                    rx.vstack(
                        rx.text(d["title"], font_size="11px", color="#171717"),
                        rx.hstack(
                            rx.badge(d["category"], size="1"),
                            rx.text(
                                f"{d['replies']} replies",
                                color="#999",
                                font_size="10px",
                            ),
                            spacing="2",
                        ),
                        spacing="1",
                    ),
                    padding_y="8px",
                    border_bottom="1px solid #f0f0f0",
                    cursor="pointer",
                )
                for d in discussions
            ],
            width="100%",
        ),
        background="white",
        border="1px solid #eee",
        border_radius="12px",
        padding="12px",
        width="260px",
    )


def product_hunt_tab() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(ph_sidebar(), display=["none", "none", "block"]),
            rx.box(ph_products_list(), flex="1", min_width="0"),
            rx.box(ph_discussions(), display=["none", "none", "none", "block"]),
            spacing="5",
            width="100%",
            max_width="1400px",
            margin="0 auto",
            padding="20px 24px",
        ),
        background="#fafafa",
        min_height="calc(100vh - 60px)",
    )


# ============================================================================
# MAIN PAGE
# ============================================================================


def index() -> rx.Component:
    return rx.box(
        header(),
        rx.cond(AppState.active_tab == "rundown", rundown_tab(), product_hunt_tab()),
        min_height="100vh",
        background="#fafafa",
    )


app = rx.App(
    theme=rx.theme(accent_color="orange", radius="medium"),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
    ],
)
app.add_page(index, route="/", title="Awesome AI Tools")
