from distutils.core import setup

from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="breame",
    packages=find_packages(
        exclude=[
            "*.tests",
            "*.tests.*",
            "tests.*",
            "tests",
            "examples",
            "docs",
            "out",
            "dist",
            "media",
            "test",
        ]
    ),
    version="0.1.0",
    license="Apache-2.0",
    description="Breame is a lightweight Python package with a number of utility tools to aid in the detection of words that have dual spellings and meanings in British and American English.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Charles Pierse",
    author_email="charlespierse@gmail.com",
    url="https://github.com/cdpierse/breame",
    keywords=[
        "text processing",
        "natural language proessing",
        "utility library",
        "spelling",
        "search engine"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.8",
    ],
)
