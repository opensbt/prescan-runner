from sqlite3 import connect
import matlab.engine
import os
from pathlib import Path

def add_variable(eng,name, value):
    eng.workspace[name] = value

def refresh_workspace(eng):
    eng.eval("clear", nargout=0)
    add_variable(eng,"NUTS_defined", True)

def cd(eng,path):
    eng.cd(path)

def add_path(eng, path, recursive=False):
    if recursive:
        if not os.path.isdir(path):
            path = Path(path).parent
        eng.addpath(eng.genpath(str(path)), nargout=0)
        print("++ paths added ++")
    else:
        eng.addpath(path, nargout=0)

def connect_to_matlab():
    future = matlab.engine.connect_matlab(background=True)
    if future is None:
        print("++ no matlab session is shared")
        return None
    else:
        print("++ connecting to matlab ")
        eng = future.result()
        return eng

def change_to_dir_file(eng,filepath):
    p = Path(filepath)
    experimentDir = p.parent
    cd(eng,str(experimentDir))