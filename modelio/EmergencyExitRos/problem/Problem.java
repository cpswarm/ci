package emergencyexitros;

import java.util.ArrayList;
import java.util.Random;
import core.NavigableMap;

import core.AbstractRepresentation;
import core.AbstractSingleProblem;
import core.ProblemXMLData;

import helper.simROS;
import helper.Environment

/**
 */
public class EmergencyExitROS extends AbstractSingleProblem {

	/**
	* Interface to ROS simulator.
	*/
	private simROS sim;

	/**
	* Load configuration parameters and store in simulator interface.
	*/
	private void loadParameters() {
		// general simulation parameters for ROS
		Hashtable<String,String> params = new Hashtable<String, String>();
		params.put("steps", getProperties().get("steps").getValue());
		params.put("agents", getProperties().get("swarmMembers").getValue());
		sim.setParameters(params);

		// name of the environment to simulate in
		sim.setEnvironment(Environment.fromString(getProperties().get("environment").getValue()));
	}

	/**
	* Calculate the fitness score of the last simulation run.
	* @return double: The fitness score.
	*/
	private double calcFitness() {
		// get content from log files
		ArrayList<NavigableMap<Integer,Double>> logs = sim.getLogs();

		// fitness score is negative sum of all distances
		double dist = 0;

		// iterate all log files
		for (NavigableMap<Integer,Double> log : logs) {
			// take last line of log file
			dist = dist + log.lastEntry().getValue();
		}

		// return negative distance as fitness;
		return -dist;
	}

	/**
	*  Simulate without visualization to evaluate the candidate representation.
	*  @param AbstractRepresentation candidate: The candidate to evaluate.
	* @return double: The fitness of the candidate.
	*/
	@Override
	public double evaluateCandidate(AbstractRepresentation candidate) {
		// create new simulator interface
		ProblemXMLData data = (ProblemXMLData) getXMLData();
		sim = new simROS(candidate, getProperties().get("rosWs").getValue(), getProperties().get("rosPackage").getValue(), data.getRequiredNumberOfOutputs());

		// read config for simulation
		loadParameters();

		// run simulation
		sim.run();

		// return fitness
		return calcFitness();
	}
	/**
	*  Simulate with visualization to introspect a certain candidate representation.
	* @param AbstractRepresentation candidate: The candidate to introspect.
	*/
	@Override
	public void replayWithVisualization(AbstractRepresentation candidate) {
		// create new simulator interface
		ProblemXMLData data = (ProblemXMLData) getXMLData();
		sim = new simROS(candidate, getProperties().get("rosWs").getValue(), getProperties().get("rosPackage").getValue(), data.getRequiredNumberOfOutputs());

		// read config for simulation
		loadParameters();

		// run simulation
		sim.runVisual();
		/**
		* Get the maximum possible fitness.
		* @return double: maximum fitness.
		*/
		@Override
		public double getMaximumFitness() {
		// TODO Auto-generated method stub
			return Double.MAX_VALUE;
		}

	}
