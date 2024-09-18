from setuptools import setup, find_packages

setup(
    name="pdf_merger",
    version="1.0.0",
    author="IPG2004",
    author_email="osteriz167@gmail.com",
    description="A graphical interface for merging PDF files.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/IPG2004/PDF-Merger",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'customtkinter',
        'pypdf',
    ],
    entry_points={
        'console_scripts': [
            'pdf_merger=src.app:main',
        ],
    },
    license='MIT',
    keywords='pdf merger tkinter',
)