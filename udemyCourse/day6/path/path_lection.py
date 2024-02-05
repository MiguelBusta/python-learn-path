"""
Date: 05/02/2024
Miguel Ángel Bustamante Pérez

* Directories

TODO: This program is only for educational purposes, in this case to learn how to use the path module from pathlib

Comments:

"""

from pathlib import Path

home_route = Path.home()
print(f"This is the path from the main directory in the pc: {home_route}")