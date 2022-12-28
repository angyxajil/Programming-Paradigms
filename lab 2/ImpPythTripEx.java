package pythex;

public class ImpPythTripEx {

	public static double sideA;
	public static double sideB;
	public static double hyp;

	/**
	 * Represent the Pythagorean triples with a 3 x 3 array of doubles called
	 * triples. Each row should contain the values for the side A, side B, and
	 * hypotenuse of a Pythagorean Triple.
	 */
	public static double[][] triples = new double[3][3];

	/**
	 * This method should take values for side A, side B, and an array row index,
	 * calculate the hypotenuse, and add the values to the 2D array at the specified
	 * row.
	 */
	public static void takeTwoSides(double sideAIn, double sideBIn, int indexIn) {
		sideA = sideAIn;
		sideB = sideBIn;
		hyp = Math.sqrt(Math.pow(sideA, 2) + Math.pow(sideB, 2));

		triples[indexIn][0] = sideA;
		triples[indexIn][1] = sideB;
		triples[indexIn][2] = hyp;

	}

	/**
	 * This method should take values for side A, hyp, and an array row index,
	 * calculate side B, and add the values to the 2D array at the specified row.
	 */
	public static void takeOneSideAndHyp(double sideAIn, double hypIn, int indexIn) {
		sideA = sideAIn;
		hyp = hypIn;
		sideB = Math.sqrt(Math.pow(hyp, 2) - Math.pow(sideA, 2));

		triples[indexIn][0] = sideA;
		triples[indexIn][1] = sideB;
		triples[indexIn][2] = hyp;
	}
	
	/**
	 * Write a main() method that uses the *same examples* used in my driver class
	 * and generates output formatted similarly to the output in the example. The
	 * methods that do calculations should *not* produce any user output; the output
	 * must be done in main().
	 */
	public static void main(String[] args) {

		/**
		 * instanciating a PythTriple object
		 */
		ImpPythTripEx pt1 = new ImpPythTripEx();
		/**
		 * calling the takeTwoSide method where side A is 3, side B is 4 and the index
		 * is 0
		 */
		pt1.takeTwoSides(3, 4, 0);
		
		/**
		 * instanciating a second PythTriple object
		 */
		ImpPythTripEx pt2 = new ImpPythTripEx();
		/**
		 * calling the takeOneSideAndHyp method where side A is 1, the hypotenuse is the
		 * square root of 2, and the index is 1
		 */
		pt2.takeOneSideAndHyp(1, Math.sqrt(2), 1);
		
		/**
		 * instanciating a third PythTriple object
		 */
		ImpPythTripEx pt3 = new ImpPythTripEx();
		/**
		 * calling the takeTwoSides method where side A is 2, side B is 3, and the index
		 * is 2
		 */
		pt3.takeTwoSides(2, 3, 2);
		
		/**
		 * printing the 2D array
		 */
		for (int i = 0; i < ImpPythTripEx.triples.length; i++) {

			System.out.print("PythTriple [");

			for (int j = 0; j < ImpPythTripEx.triples.length; j++) {

				switch (j) {
				case 0:
					System.out.print("sideA=");
					break;
				case 1:
					System.out.print("sideB=");
					break;
				case 2:
					System.out.print("hyp=");
					break;
				}

				System.out.print((double) Math.round(ImpPythTripEx.triples[i][j] * 1000) / 1000);

				if (j == 0 | j == 1) {
					System.out.print(", ");
				}
			}

			System.out.println("]");
		}
	}
}