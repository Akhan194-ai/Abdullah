package lab3task2;
import java.util.*;
public class RectangleTest {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
        Rectangle rectangle = new Rectangle();

        // Input and set length
        System.out.print("Enter length of the rectangle: ");
        double length = scanner.nextDouble();
        rectangle.setLength(length);

        // Input and set width
        System.out.print("Enter width of the rectangle: ");
        double width = scanner.nextDouble();
        rectangle.setWidth(width);

        // Display the rectangle's dimensions, area, and perimeter
        System.out.printf("Length: %.2f%n", rectangle.getLength());
        System.out.printf("Width: %.2f%n", rectangle.getWidth());
        System.out.printf("Area: %.2f%n", rectangle.area());
        System.out.printf("Perimeter: %.2f%n", rectangle.perimeter());

	}

}
