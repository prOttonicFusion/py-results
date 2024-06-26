import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-results",
    version="1.0.0",
    author="prOttonicFusion",
    author_email="otto.lindblom@gmail.com",
    description="A result wrapping object for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prOttonicFusion/py-results",
    packages=setuptools.find_packages(exclude=["tests*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
