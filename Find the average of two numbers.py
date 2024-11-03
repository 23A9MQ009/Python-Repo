import java.util.Scanner;

public class AverageOfTwoNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read the two decimal numbers
        double N = scanner.nextDouble();
        double M = scanner.nextDouble();
        
        // Calculate the average
        double average = (N + M) / 2.0;
        
        // Print the average with 4 decimal places
        System.out.printf("%.4f\n", average);
        
        scanner.close();
    }
}