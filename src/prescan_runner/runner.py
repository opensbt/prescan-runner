# Copyright (c) 2023 fortiss GmbH
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

import time
import traceback
import matlab.engine
from prescan_runner.matutils import matlib
from  prescan_runner.parser import parser 
import os
import subprocess
import logging as log
import prescan.api.experiment

OUTPUT_FILENAME = "results.csv"
TRACES_FILENAME = "trace_online.csv"
INPUT_FILENAME = "input.json"
EXP_EXECUTABLE = "Demo_AVP_cs"
PATH_KILL_SCRIPT = os.getcwd() + "\\..\\FOCETA\\experiments\\PrescanHangKill.bat"

DO_REPEAT = True
TIME_WAIT = 10 # in seconds
MAX_REPEAT = 10

class Singleton(object):
        def __new__(cls, *args, **kwds):
            it = cls.__dict__.get("__it__")
            if it is not None:
                return it
            cls.__it__ = it = object.__new__(cls)
            it.init(*args, **kwds)
            return it

        def init(self, *args, **kwds):
            pass

class Runner(Singleton):
	eval_counter = 0
     
	def init(self, exp_file, exp_name_executable =EXP_EXECUTABLE):
		self.exp_file = exp_file  
		self.exp_name_executable = exp_name_executable
		
		exp_dir = os.path.dirname(exp_file)

		# connect to matlab
		engine = matlib.connect_to_matlab()
	
		self.engine = engine
	   	
	    # change to experiment directory
		matlib.cd(engine, exp_dir)
		# add all files in experiment directory
		matlib.add_path(engine, exp_file, recursive=True)
	
	def update_experiment(self, input_json_name, do_visualize, sim_time):
		# TODO use dynamic input json path
		self.engine.ChangeModel(do_visualize,sim_time) 
	
	def run_experiment(self, name_executable):
	    subprocess.run(name_executable + ".exe", cwd=os.path.dirname(self.exp_file), shell=True)
	
	def run_experiment_pb(self, sim_time, do_regenerate=True):
		res = self.engine.runExperimentFromPb(self.exp_file, do_regenerate, sim_time)
		return res
	
	def kill_run(self, path_kill_script):
		log.info("Killing Prescan experiment execution...")
		subprocess.Popen(path_kill_script, shell=True, stdout=subprocess.PIPE)

def run_scenario(input_json_name, 
				exp_file, 
				name_executable, 
				do_visualize, 
				sim_time, 
				output_filename=OUTPUT_FILENAME, 
				traces_filename=TRACES_FILENAME,
				path_kill_script=PATH_KILL_SCRIPT,
				do_regenerate=True,
				run_from_pb_file=True):

	runner = Runner(exp_file)
	runner.update_experiment(input_json_name, 
			  				do_visualize=do_visualize, 
							sim_time=sim_time)
	repeat_counter = 0
	do_repeat = DO_REPEAT
	parsed = None

	Runner.eval_counter += 1
	log.info(f"[Prescan Runner] Running evaluation {Runner.eval_counter}")
	while do_repeat and (repeat_counter <= MAX_REPEAT):
		try:
			if run_from_pb_file:
				runner.run_experiment_pb(sim_time=sim_time, do_regenerate=do_regenerate)
			else:
				runner.run_experiment(name_executable)
			parent_dir = os.path.dirname(exp_file)
			parsed = parser.parse_output(parent_dir + os.sep + output_filename, 
						parent_dir + os.sep + traces_filename
			)
			do_repeat = False
		except Exception as e:
			log.info("[Prescan Runner] Exception during simulation ocurred: ")
			traceback.print_exc()
			runner.kill_run(path_kill_script=path_kill_script)
			time.sleep(TIME_WAIT)                
			log.error(f"\n[Prescan Runner] ---- Repeating evalation {Runner.eval_counter} due to exception: ---- \n {e} \n")
			repeat_counter += repeat_counter

	log.info("[Prescan Runner] leaving runner")

	return parsed