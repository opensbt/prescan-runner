function simout = runExperimentFromOSC(file, regenerate, simTime)
    exp = prescan.api.experiment.Experiment();
    prescan.api.openscenario.importOpenScenarioFile(exp, file);
    exp.saveToFile('test.pb')
    simout = prescan.api.simulink.run(exp,'Regenerate',regenerate,'StopTime', string(simTime));
end