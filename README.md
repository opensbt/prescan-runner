# Prescan Runner
Prescan Runner is a plugin for OpenSBT to apply search based testing to system simulated in Prescan.

## Prerequisites
This plugin is only compatible with the python 3.7 interpreter. Installation has been tested with Windows 10/11.

## Getting Started

### Python Wheel
The easiest way to get the Prescan Runner up and running is to build it as a Python package and install it.
To build the package, run `python -m build` in the repository's root directory (npms build package has to be installed). Once completed, install the *.whl package found in the newly created dist/ folder via `python -m pip install /path/to/the/package.whl`

### Assumptions

The current implemenation of this plugin has the following assumptions:

- The scenario is parametrized using `input.json` file
- A `ChangeModel.m` script is provided to update the `.pb` experiment file using the `input.json file`
- The simulink model contains blocks to write traces of actors of interest into `trace_online.csv`.  

### Before Running Experiment

Execute the following steps before running experiments with OpenSBT:

(Step 1 is only required once)

1. Execute the following to import the matlab engine:

    ```
    cd MATLAB_DIR/extern/engines/python
    py -3.7 setup.py install --prefix="C:\Path\To\Project\venv"

    ```
    Further description/options are available [here](https://de.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html).

2. Start MATLAB via Prescan using: `matlab.engine.shareEngine`

3. Make sure all files have been added to the matlab path which a required for executing the simulink SUT