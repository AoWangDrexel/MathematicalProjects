/**
 * 
 * @author aowang
 *
 */

public class PiApprox {

	public static void main(String[] args) {
		double inCircle = 0;
		double total = 0;

		// circle x^2 + y^2 = r^2
		// square is 1 by 1
		// circle radius = 1/2

		double recordAccurate = 0;
		while (true) {

			// random x and y coordinates, - 0.5 <= x < 0.5, -0.5 <= y < 0.5
			double randX = Math.random() - 0.5;
			double randY = Math.random() - 0.5;

			// testing if random coordinates are on or inside the circle of radius 1/2
			boolean r = Math.sqrt(Math.pow(randX, 2) + Math.pow(randY, 2)) <= 0.5;

			if (r) {
				inCircle++;
			}
			total++;

			// caluation of 4 * pi/4
			double currentPi = 4 * inCircle / total;

			double functionPi = Math.PI;
			double recordDiff = Math.abs(recordAccurate - functionPi);

			double diff = Math.abs(currentPi - functionPi);

			// finding smallest difference of approximation and java's math library of pi
			if (diff < recordDiff) {
				recordAccurate = currentPi;
				System.out.println(recordAccurate);
			}
		}

	}

}
