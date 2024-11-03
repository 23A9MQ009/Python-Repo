import java.util.Scanner;

public class TriangleArea {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read the lengths of the triangle
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        int C = scanner.nextInt();
        
        // Calculate the semi-perimeter
        double s = (A + B + C) / 2.0;
        
        // Calculate the area using Heron's formula
        double area = Math.sqrt(s * (s - A) * (s - B) * (s - C));
        
        // Print the area with two decimal places
        System.out.printf("%.2f\n", area);
        
        scanner.close();
    }
}