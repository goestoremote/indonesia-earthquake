import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="earthquake-id-warning",                     # This is the name of the package
    version="0.0.2",                        # The initial release version
    author="Heru Setiawan",                     # Full name of the author
    author_email="lenterabots@gmail.com",
    description="this project will report the latest earthquake in Indonesia from BMKG",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    url="https://github.com/goestoremote/indonesia-earthquake",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],                                      # Information to filter the project on PyPi website
    packages=setuptools.find_packages(),  # List of all python modules to be installed
    python_requires='>=3.6',  # Minimum version requirement of the package
    # py_modules=["quicksample"],             # Name of the python package
    # package_dir={'':'quicksample/src'},     # Directory of the source code of the package
    # install_requires=[]                     # Install other dependencies if any
)