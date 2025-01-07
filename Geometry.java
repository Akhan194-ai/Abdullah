package lab10;

public class Geometry {
    private double radius;

    // Constructor to initialize the radius
    public Geometry(double radius) {
        this.radius = radius;
    }

    // Getter for radius
    public double getRadius() {
        return radius;
    }

    // Setter for radius
    public void setRadius(double radius) {
        this.radius = radius;
    }

    // Method to calculate Circumference of a circle: C = 2 * π * r
    public double calculateCircumference() {
        return 2 * Pi.VALUE * radius;
    }

    // Method to calculate Area of a circle: A = π * r²
    public double calculateAreaOfCircle() {
        return Pi.VALUE * radius * radius;
    }

    // Method to calculate Volume of a sphere: V = (4/3) * π * r³
    public double calculateVolumeOfSphere() {
        return (4.0 / 3.0) * Pi.VALUE * Math.pow(radius, 3);
    }

    // Method to calculate Surface Area of a sphere: A = 4 * π * r²
    public double calculateSurfaceAreaOfSphere() {
        return 4 * Pi.VALUE * radius * radius;
    }
}

