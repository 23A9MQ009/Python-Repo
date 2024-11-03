import java.util.Scanner;

public class MultiplyNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Reading the first number
        int num1 = scanner.nextInt();
        
        // Reading the second number
        int num2 = scanner.nextInt();
        
        // Calculating the multiplication
        int result = num1 * num2;
        System.out.println(result);
        scanner.close();
    }
}
