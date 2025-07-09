from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="tvdatafeed",
    version="2.1.0",
    packages=["tvDatafeed"],
    url="https://github.com/qalpha/tvdatafeed/",
    project_urls={
        "YouTube": "https://youtube.com/StreamAlpha?sub_confirmation=1",
        "Funding": "https://www.buymeacoffee.com/StreamAlpha",
        "Telegram Channel": "https://t.me/streamAlpha",
        "Source": "https://github.com/qalpha/tvdatafeed/",
        "Tracker": "https://github.com/qalpha/tvdatafeed/issues",
    },
    license="MIT License",
    author="@qalpha",
    author_email="",
    description="TradingView historical data downloader",
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=[
        "setuptools",
        "pandas",
        "selenium",
        "websocket-client",
        "chromedriver-autoinstaller",
    ],
)
