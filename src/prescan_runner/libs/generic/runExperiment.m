% Copyright (c) 2023 fortiss GmbH
%
% This work is licensed under the terms of the MIT license.
% For a copy, see <https://opensource.org/licenses/MIT>.

function simOut = runExperiment(experiment,stopTime)
    simOut = prescan.api.simulink.run(experiment, 'Regenerate', 'on', 'StopTime', str(stopTime));
end