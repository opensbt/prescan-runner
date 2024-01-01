% Copyright (c) 2023 fortiss GmbH
%
% This work is licensed under the terms of the MIT license.
% For a copy, see <https://opensource.org/licenses/MIT>.

function simout = runExperimentFromPb(file, doRegenerate, simTime)
    if doRegenerate 
        regenerate = 'on';
    else
        regenerate = 'off';
    end
    exp = prescan.api.experiment.loadExperimentFromFile(file);
    simout = prescan.api.simulink.run(exp,'Regenerate',regenerate,'StopTime', string(simTime)); 
    %simout = prescan.api.simulink.run(exp, 'ReturnWorkspaceOutputs', 'on', 'Regenerate', regenerate, 'SaveFormat', 'Structure', 'SaveState','on','StateSaveName','state','SaveOutput','on','OutputSaveName','output', 'StopTime', string(simTime), 'LoggingToFile','on');
end

%TODO problem with loading experiment from files from different directories
