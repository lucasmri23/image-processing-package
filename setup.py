from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-package-lucas",
    version="0.0.1",
    author="Lucas Ribeiro",
    author_email="lucasmribeiro2004@gmail.com",
    description="Image Processing Package using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lucasmri23/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.5",
)