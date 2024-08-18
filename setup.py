from setuptools import setup, find_packages

setup(
    name="webview-checker",
    version="0.1",
    description="CLI tool to check if IoT companion apps use WebView or web technologies",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'shodan',
    ],
    entry_points={
        'console_scripts': [
            'webview-checker=cli:main',
        ],
    },
)
