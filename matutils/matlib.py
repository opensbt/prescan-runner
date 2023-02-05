from sqlite3 import connect
import matlab.engine
import os
from pathlib import Path

def addExperimentLibsPath(eng):
    libsFolder = "prescan_simulation" + os.sep + "libs" + os.sep + "generic"
    abspath = os.getcwd() + os.sep + libsFolder
    eng.addpath(abspath, nargout=0)

def addVariable(eng,name, value):
    eng.workspace[name] = value

def refreshWorkspace(eng):
    eng.eval("clear", nargout=0)
    addVariable(eng,"NUTS_defined", True)

def cd(eng,path):
    eng.cd(path)

def addPath(eng, path, recursive=False):
    if recursive:
        if not os.path.isdir(path):
            path = Path(path).parent
        eng.addpath(eng.genpath(str(path)), nargout=0)
        print("++ paths added ++")
    else:
        eng.addpath(path, nargout=0)

def connectToMatlab():
    future = matlab.engine.connect_matlab(background=True)
    if future is None:
        print("++ no matlab session is shared")
        return None
    else:
        print("++ connecting to matlab ")
        eng = future.result()
        return eng

def connectToPrescanMatlab():
    eng = connectToMatlab()
    if eng is not None:
        addExperimentLibsPath(eng)
    else:
        print("++ could not add prescan exp libs ")
    return eng

def changeToDirFile(eng,filepath):
    p = Path(filepath)
    experimentDir = p.parent
    cd(eng,str(experimentDir))