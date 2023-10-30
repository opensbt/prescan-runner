% add sut related paths

addpath(genpath([pwd '/Leuven_AVP_ori']))
addpath(genpath([pwd '/matlab']))
addpath(genpath([pwd '/SUT']))

cd([pwd '/Leuven_AVP_ori'])

% share engine for OpenSBT

matlab.engine.shareEngine
