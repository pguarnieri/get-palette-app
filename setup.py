import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="get_palette", # Replace with your own username
    version="0.0.1",
    author="Pierandrea Guarnieri",
    author_email="p.guarnieri@me.com",
    description="A simple package to create a colour palette starting from an image",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pguarnieri/get-palette-app",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)