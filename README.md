# Prescan Runner
Prescan Runner is a plugin for OpenSBT to apply search based testing to system simulated in Prescan.


## Prerequisites
This plugin is only compatible with the python 3.7 interpreter. Installation has been tested with Windows 10/11.

## Getting Started

### Python Wheel
The easiest way to get the Prescan interface up and running is to build it as a Python package and install it.
To build the package, run python -m build in the repository's root directory. Once completed, install the *.whl package found in the newly created dist/ folder via python -m pip install /path/to/the/package.whl

### Before Running Experiment

Execute the following steps before running experiments:

1. Import the matlab engine ([s. here](https://de.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html))

2. Start MATLAB via Prescan using: `matlab.engine.shareEngine`

3. Run your experiment script with a python 3.7 interpreter (newer versions are not supported by the matlab engine)
