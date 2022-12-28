package Lab2;

import java.text.DecimalFormat;

public class employeeData {

	public static String empName[] = new String[5];
	public static double empWage[] = new double[5];
	public static double empHours[] = new double[5];

	public static int arrIndex = 0;

	public static int numOfEmps = 0;
	
	private static final DecimalFormat df = new DecimalFormat("0.00");

	public static void addEmployee(String name, double hourlyWage, double hoursWorked) {

		empName[arrIndex] = name;
		empWage[arrIndex] = hourlyWage;
		empHours[arrIndex] = hoursWorked;
		
		arrIndex++;
		numOfEmps++;

	}
	
	public static void calcPaychecks() {
		
		double empCheck = 0;
		double avgCheck = 0;
		
		for (int i = 0; i < numOfEmps; i++) {
			
			empCheck = empWage[i] * empHours[i];
			
			System.out.println
            ("Employee Data: " + empName[i]+ ", Wage: $" + empWage[i] 
            + ", Hours: " +  empHours[i] + ", Total pay: $" + df.format(empCheck) + "\n");
			
			avgCheck += empCheck;
		}
		
		System.out.println("Average paycheck:$" + (avgCheck / numOfEmps));
		
	}
	
}
