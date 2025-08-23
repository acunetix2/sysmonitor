from setuptools import setup, find_packages

setup(
    name="sysmonitor",
    version="0.2.0",
    packages=find_packages(),
    install_requires=["typer", "psutil", "rich"],
    entry_points={
        "console_scripts": [
            "sysmonitor=sysmonitor.cli:app",
        ],
    },
    author="Your Name",
    description="Cross-platform CLI tool to collect system and resource usage info",
    license="MIT",
    python_requires=">=3.7",
)
