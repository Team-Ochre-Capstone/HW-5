# DevOps Exercise

This is a skeleton repository for your exercise. 
The goal of this exercise is to implement a Python package for sorting integer 
lists using the DevOps software development approach.

> **Warning**: If working on windows, some directories and files in this archive
will not be visible because they start with a '.'. In the file browser, change 
the View to display "Hidden items".

You will need to:
1. Add .pre-commit-config.yml which:  
    1. Limits maximal file size.
    2. Runs the black and flake8 linters.
    3. Detect presence of aws credentials private keys.    
2. Implement the algorithms for bubble, quick and insertion sort, see sort_lib directory,
code should be documented using standard Python practices (there are several [docstring 
styles](https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format)
select one and be consistent).
3. Implement testing using the [pytest](https://docs.pytest.org/en/6.2.x/) framework, see test directory.
4. Implement linting, style checking using both [flake8](https://flake8.pycqa.org/en/latest/) and 
[black](https://black.readthedocs.io/en/stable/). 
5. Modify the GitHub actions workflow so that it tests and builds the package for all 
three operating systems (OSX/Linux/Win) and for Python versions 3.9 and 3.10. Read more about [Distributing Python packages](https://docs.python.org/3/distributing/index.html).
6. Modify this file to describe this repository and the DevOps workflow you implemented (add badges to this file showing testing status).
EC. **Optional**: Add a job to the workflow which uploads the wheel to [TestPyPI](https://test.pypi.org/). As every package on TestPyPI is required to have a unique name you need to update the UNIQUE_SUFFIX both in the directory name and in the .toml file. Possibly use your team number.
    >**Warning**: Do not upload to the authoritative Python Package Index (PyPI).  

Matrix:
OS / Python Version     Bubble Sort CPU Usage   Quick Sort Runtime	Insertion Sort Memory Usage
macOS (3.9)	            0.05%	                0.021297s	        0.000000 MB
macOS (3.10)	        0.25%	                0.018475s	        0.000000 MB
Windows (3.9)	        0.00%	                0.027898s	        0.210938 MB
Windows (3.10)	        0.00%	                0.027051s	        0.226562 MB
Ubuntu (3.9)	        0.00%	                0.028827s	        0.000000 MB
Ubuntu (3.10)	        0.00%	                0.028293s	        0.000000 MB


Possible work division, three sub-teams:
1. Adding pre-commit and implementing algorithm code and documentation (tasks 1,2,6).
2. Implementing testing code, mastering pytest, black, flake8 (tasks 3,4,6).
3. Understanding pytest, black, flake8 and mastering GitHub workflows (tasks 5,6).

Black Linting (Ethan Wyman)
Implemented the black linting. Black automatically reformats Python code to adhere to a strict, opinionated style, largely based on PEP 8. It aims for consistency, readability, and minimizing diffs in version control.
Black Linting was pushed through and reformatted the Python code to follow the style
https://github.com/psf/black
https://black.readthedocs.io/en/stable

