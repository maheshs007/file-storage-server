# Import the setup function from setuptools
from setuptools import setup

# Call the setup function to define the package
setup(
    name="file_storage_cli",      # The name of the package
    version="1.0",                # Version of the package
    py_modules=["cli"],           # Modules to include, in this case, only `cli.py`
    
    # Specify external dependencies required by the package
    install_requires=[
        "click",                 # Click is used for building the CLI interface
        "requests"               # Requests is used for making HTTP requests to the server
    ],
    
    # Define entry points for the CLI
    entry_points={
        "console_scripts": [
            # Defines `fs-store` as the CLI command and maps it to `cli:cli`
            # This means running `fs-store` in the terminal will execute the `cli` function from `cli.py`
            "fs-store=cli:cli",
        ],
    },
)
