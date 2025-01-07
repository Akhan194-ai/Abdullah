package lab09;

import java.util.Arrays;

public class GenericReverseArray {
	 // Generic method to reverse and print an array
    public static <T> void reverseAndPrintArray(T[] array) {
        if (array == null || array.length == 0) {
            System.out.println("Array is empty or null.");
            return;
        }
        
        System.out.print("Original Array: ");
        System.out.println(Arrays.toString(array));

        System.out.print("Reversed Array: ");
        for (int i = array.length - 1; i >= 0; i--) {
            System.out.print(array[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // Integer array
        Integer[] intArray = {1, 2, 3, 4, 5};
        reverseAndPrintArray(intArray);

        // Double array
        Double[] doubleArray = {1.1, 2.2, 3.3, 4.4};
        reverseAndPrintArray(doubleArray);

        // Character array
        Character[] charArray = {'A', 'B', 'C', 'D'};
        reverseAndPrintArray(charArray);
    }
}

