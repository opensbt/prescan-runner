function simOut = runExperiment(experiment,stopTime)
    simOut = prescan.api.simulink.run(experiment, 'Regenerate', 'on', 'StopTime', str(stopTime));
end