% Copyright (c) 2023 fortiss GmbH
%
% This work is licensed under the terms of the MIT license.
% For a copy, see <https://opensource.org/licenses/MIT>.

unction simout = runExperimentFromOSC(file, regenerate, simTime)
    exp = prescan.api.experiment.Experiment();
    prescan.api.openscenario.importOpenScenarioFile(exp, file);
    exp.saveToFile('test.pb')
    simout = prescan.api.simulink.run(exp,'Regenerate',regenerate,'StopTime', string(simTime));
end