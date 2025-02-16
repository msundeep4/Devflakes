# Define the __all__ variable
__all__ = ["module1", "module2"]

# Import the submodules
from . import module1
from . import module2

# Define a variable called version
version = "1.0.0"

# Print a welcome message
print(f"Welcome to mypackage version {version}")