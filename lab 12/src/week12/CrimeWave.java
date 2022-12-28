package week12;

import java.lang.Thread.State;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;

public class CrimeWave {

	Random rand = new Random();
	Queue<Crime> crimes = new LinkedList<Crime>();

	Criminal c1 = new Criminal("Criminal 1");
	Criminal c2 = new Criminal("Criminal 2");

	Detective d1 = new Detective("Detective 1");
	Detective d2 = new Detective("Detective 2");

	// Each criminal and each Detective has his/her own thread
	Thread t1 = new Thread(c1);
	Thread t2 = new Thread(c2);
	Thread t3 = new Thread(d1);
	Thread t4 = new Thread(d2);

	private class Crime {
		public Crime(int severity) {

		}
	}

	int totCrimes = 0;
	int crimesSolved = 0;
	int totSeverity = 0;

	/**
	 * method crimeCommited that takes a crime and criminalName as parameters
	 * 
	 * @param crime
	 * @param criminalName
	 */
	public void crimeCommited(Crime crime, String criminalName) {

		int severity = (int) (Math.random() * 10) + 1;

		System.out.println(criminalName + " commits a crime of severity " + severity);

		//((LinkedList<Crime>) crimes).push(crime);
		// the Queue interface uses add() to put an object at the back of the queue
		crimes.add(crime);
		// adds severity to the total
		totSeverity += severity;
		// add one crime to the
		totCrimes++;
	}

	int severity = (int) (Math.random() * 10) + 1;

	// the method that is called when a detective solves a crime
	public void solveCrime(String detectiveName) {

		while (crimes.isEmpty()) {
			try {
				Thread.sleep(2);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}

		// the Queue interface uses poll() to remove one from the front
		if (crimes.poll() != null) {

			crimesSolved++;

			System.out.println(detectiveName + " solves a crime of severity " + severity);
		}

	}

	public class Criminal implements Runnable {

		private String name;

		public Criminal(String name) {
			this.name = name;
		}

		@Override
		public void run() {
			for (int counter = 0; counter < 100; counter++) {
				Crime crime = new Crime(severity);
				crimeCommited(crime, name);
			}
		}
	}

	private class Detective implements Runnable {
		private String name;

		public Detective(String string) {
			name = string;
		}

		@Override
		public void run() {
			while (crimes.isEmpty() == false || t1.getState() != State.TERMINATED
					|| t2.getState() != State.TERMINATED) {
				solveCrime(name);
			}
		}
	}

	public static void main(String[] args) {
		CrimeWave wave = new CrimeWave();
		wave.feed();
	}

	public void feed() {
		t3.start();
		t4.start();
		t1.start();
		t2.start();

		while (t1.getState() != State.TERMINATED || t2.getState() != State.TERMINATED || !(crimes.isEmpty())) {
			try {
				Thread.sleep(1);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}

		System.out.println();

		System.out.println("crimes committed: " + totCrimes);
		float average = (float) totSeverity / totCrimes;
		System.out.println("average severity: " + average);
		System.out.println("crimes solved: " + crimesSolved);
	}
}