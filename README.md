**Sorting Algorithms Performance Analysis**

    A Python package implementing and benchmarking three sorting algorithms with comprehensive DevOps CI/CD pipeline.

📋 **Project Overview**

    This project demonstrates modern DevOps practices by implementing:

    Three sorting algorithms (Bubble Sort, Quick Sort, Insertion Sort)

    Performance metrics (CPU usage, runtime, memory usage)

    Automated CI/CD pipeline with GitHub Actions

    Code quality enforcement with pre-commit hooks

    Cross-platform testing on Windows, Linux, and macOS

🚀 **DevOps Workflow**

    Our CI/CD pipeline ensures code quality and reliability through:

    Pre-commit Hooks

    File size limits to prevent large commits

    Code formatting with Black

    Linting with Flake8

    Security checks for AWS credentials

    GitHub Actions Pipeline

    Multi-OS testing (Windows, Ubuntu, macOS)

    Multi-Python version support (3.9, 3.10)

    Automated testing with pytest

    Package building and distribution

📁 **Project Structure**

    sorting-algorithms/
    ├── .github/
    │   └── workflows/
    │       └── main.yml          # CI/CD pipeline
    ├── sort_lib/
    │   ├── __init__.py
    │   ├── int_sort.py        # Contains all sorting algorithms
    ├── test/
    │   ├── test_basic_sort.py
    ├── .flake8
    ├── .pre-commit-config.yml    # Pre-commit hooks
    ├── pyproject.toml           # Package configuration
    ├── README.md                # README
    ├── requirements-dev.txt     # Dependencies
    └── requirements.txt         # Dependencies

📝 **Code Quality**

    This project maintains high code quality standards through:

    Black for consistent code formatting

    Flake8 for linting and style enforcement

    Pytest for comprehensive testing

    Pre-commit hooks for automatic quality checks

🏗 **CI/CD Pipeline Features**

    ✅ Automated testing on push and pull requests

    ✅ Multi-platform support (Windows, Linux, macOS)

    ✅ Multiple Python versions (3.9, 3.10)

    ✅ Automated package building

    ✅ TestPyPI deployment

    ✅ Performance benchmarking

👥 **Team**

__Bryan Sturdivant__ - Pre-commit

__Ethan Wyman__ - Black Linting

    https://github.com/psf/black
    https://black.readthedocs.io/en/stable

__Gregory Michaud__ - Workflows & Algorithms

__Israk Akafat__ - Flake8 Linting

__Cooper Stepankiw__ - Algorithms and README

**Matrix:**

    OS / Python Version     Bubble Sort CPU Usage   Quick Sort Runtime	Insertion Sort Memory Usage
    macOS (3.9)	            0.05%	                0.021297s	        0.000000 MB
    macOS (3.10)	        0.25%	                0.018475s	        0.000000 MB
    Windows (3.9)	        0.00%	                0.027898s	        0.210938 MB
    Windows (3.10)	        0.00%	                0.027051s	        0.226562 MB
    Ubuntu (3.9)	        0.00%	                0.028827s	        0.000000 MB
    Ubuntu (3.10)	        0.00%	                0.028293s	        0.000000 MB