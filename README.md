# Prescan Runner
Prescan Runner is a plugin for OpenSBT to apply search-based testing to a Simulink-based system simulated in [Prescan](https://plm.sw.siemens.com/en-US/simcenter/autonomous-vehicle-solutions/prescan/).

## Prerequisites
This plugin is compatible with python 3.8/3.7. Installation has been tested with Windows 10/11.

## Getting Started

### Python Wheel
The easiest way to get the Prescan Runner up and running is to build it as a Python package and install it.
To build the package, run `python -m build` in the repository's root directory (npms build package has to be installed). Once completed, install the *.whl package found in the newly created dist/ folder via `python -m pip install /path/to/the/package.whl`

### Assumptions

The current implementation of Prescan Runner requires that following is assured:

- The scenario is parametrized using an `input.json` file. 
- A `ChangeModel.m` script is provided to update the `.pb` experiment file using a file called `input.json file`. 
- The simulink model contains blocks to write traces of actors of interest into `trace_online.csv`. The format of the output can be adapted [here](src/prescan_runner/parser/parser.py)
- The prescan experiment has been compiled, i.e. simulation is triggered via running an executable. The name of the executable can be set [here](src/prescan_runner/runner.py)

### Before Running Experiment

Execute the following steps before running experiments with OpenSBT:

(_Note, that step 1 is only required once._)

1. Import the matlab engine into OpenSBT:

    ```bash
    cd MATLAB_DIR/extern/engines/python
    py -3.8 setup.py install --prefix="C:\Path\To\Project\venv"

    ```
    Further description/options are available [here](https://de.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html).

2. Start MATLAB via Prescan Process Manager.

3. Share the MATLAB engine to be accessable by OpenSBT by executing from the MATLAB terminal: 

    `matlab.engine.shareEngine`

3. Make sure all files have been added to the MATLAB path which a required for executing the simulink SUT, as done in [this](example/startup.m) example startup script.