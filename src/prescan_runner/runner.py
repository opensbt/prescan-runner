import matlab.engine
from prescan_runner.matutils import matlib
from  prescan_runner.parser import parser 
import os
import subprocess

OUTPUT_FILENAME = "results.csv"
TRACES_FILENAME = "trace_online.csv"
INPUT_FILENAME = "input.json"
EXP_EXECUTABLE = "Demo_AVP_cs"

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

def run_scenario(input_json_name, exp_file, name_executable, do_visualize, sim_time, 
						output_filename=OUTPUT_FILENAME, traces_filename=TRACES_FILENAME):

	runner = Runner(exp_file)
	runner.update_experiment(input_json_name, 
			  				do_visualize=do_visualize, 
							sim_time=sim_time)
	
	runner.run_experiment(name_executable)

	parent_dir = os.path.dirname(exp_file)
	parsed = parser.parse_output(parent_dir + os.sep + output_filename, 
			      parent_dir + os.sep + traces_filename
	)

	return parsed



