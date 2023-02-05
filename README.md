# Running PRESCAN experiments from python

## Prerequisites

0. The matlab engine has been imported into python ([s. here](https://de.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html))
1. Start MATLAB via Prescan
2. Expose MATLAB Engine by running in MATLAB console:

```
matlab.engine.shareEngine
```

3. Run your experiment script with a python 3.7 interpreter (newer versions are not supported by the matlab engine)