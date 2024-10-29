package lab3task2;

public class Rectangle {

	    // Attributes with default values
	    private double length = 1.0;
	    private double width = 1.0;

	    // Getter for length
	    public double getLength() {
	        return length;
	    }

	    // Setter for length with validation
	    public void setLength(double length) {
	        if (isValidDimension(length)) {
	            this.length = length;
	        } else {
	            System.out.println("Length must be between 0.0 and 20.0.");
	        }
	    }

	    // Getter for width
	    public double getWidth() {
	        return width;
	    }

	    // Setter for width with validation
	    public void setWidth(double width) {
	        if (isValidDimension(width)) {
	            this.width = width;
	        } else {
	            System.out.println("Width must be between 0.0 and 20.0.");
	        }
	    }

	    // Method to validate dimensions
	    private boolean isValidDimension(double value) {
	        return value > 0.0 && value < 20.0;
	    }

	    // Method to calculate area
	    public double area() {
	        return length * width;
	    }

	    // Method to calculate perimeter
	    public double perimeter() {
	        return 2 * (length + width);
	    }
	}


