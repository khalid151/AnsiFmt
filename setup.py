import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="ansifmt",
    version="0.1.0",
    author="Khalid",
    author_email="khalid.y96@outlook.com",
    description="ANSI escape sequences to format printed strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/khalid151/AnsiFmt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
