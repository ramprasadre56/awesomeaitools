import reflex as rx

config = rx.Config(
    app_name="awesomeaitools",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)