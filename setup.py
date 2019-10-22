import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="locust-ion",
    version="0.0.1",
    author="Mahfuzur Rahman",
    author_email="mahfuz.sust001@gmail.com",
    description="Locust wrapper for execution in multiple files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mahfuzsust/locust-ion",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Locust"
    ],
    install_requires=[
        'markdown',
    ],
    python_requires='>=3.6',
)
