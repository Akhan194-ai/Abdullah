

import java.util.Scanner; 

	public class Lab3Task1 {
		    // Constants for grading
		    private static final double GPA_SCALE = 4.0;
		    private static final double GRADE_A = 90;
		    private static final double GRADE_B = 80;
		    private static final double GRADE_C = 70;
		    private static final double GRADE_D = 60;

		    public static void main(String[] args) {
		        Scanner scanner = new Scanner(System.in);

		        // Taking input
		        System.out.print("Enter Student Name: ");
		        String studentName = scanner.nextLine();

		        System.out.print("Enter Total Marks: ");
		        double totalMarks = scanner.nextDouble();

		        System.out.print("Enter Obtained Marks: ");
		        double obtainedMarks = scanner.nextDouble();

		        // Calculating percentage, grade, and GPA
		        double percentage = calculatePercentage(obtainedMarks, totalMarks);
		        String grade = determineGrade(percentage);
		        double gpa = calculateGPA(percentage);

		        // Displaying the results
		        displayMarkSheet(studentName, totalMarks, obtainedMarks, percentage, grade, gpa);
		    }

		    // Method to calculate percentage
		    private static double calculatePercentage(double obtained, double total) {
		        return (obtained / total) * 100;
		    }

		    // Method to determine grade based on percentage
		    private static String determineGrade(double percentage) {
		        if (percentage >= GRADE_A) {
		            return "A";
		        } else if (percentage >= GRADE_B) {
		            return "B";
		        } else if (percentage >= GRADE_C) {
		            return "C";
		        } else if (percentage >= GRADE_D) {
		            return "D";
		        } else {
		            return "F";
		        }
		    }

		    // Method to calculate GPA based on percentage
		    private static double calculateGPA(double percentage) {
		        if (percentage >= GRADE_A) {
		            return GPA_SCALE;
		        } else if (percentage >= GRADE_B) {
		            return GPA_SCALE * 3.0 / 4.0;
		        } else if (percentage >= GRADE_C) {
		            return GPA_SCALE * 2.0 / 4.0;
		        } else if (percentage >= GRADE_D) {
		            return GPA_SCALE * 1.0 / 4.0;
		        } else {
		            return 0.0;
		        }
		    }

		    // Method to display the mark sheet
		    private static void displayMarkSheet(String name, double total, double obtained, double percentage, String grade, double gpa) {
		        System.out.println("\nMark Sheet");
		        System.out.println("-------------------------------------------------");
		        System.out.printf("Student Name: %s%n", name);
		        System.out.printf("Total Marks: %.2f%n", total);
		        System.out.printf("Obtained Marks: %.2f%n", obtained);
		        System.out.printf("Percentage: %.2f%%%n", percentage);
		        System.out.printf("Grade: %s%n", grade);
		        System.out.printf("GPA: %.2f%n", gpa);
		        System.out.println("-------------------------------------------------");
		    }
		

	}
