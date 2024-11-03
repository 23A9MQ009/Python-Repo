import java.util.Scanner;

public class ModulusNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Reading the first number
        int num1 = scanner.nextInt();
        
        // Reading the second number
        int num2 = scanner.nextInt();
        
        // Calculating the modulus
        int result = num1 % num2;
        
        // Printing the result
        System.out.println(result);

        // Closing the scanner
        scanner.close();
    }
}
