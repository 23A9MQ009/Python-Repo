import java.util.Scanner;
import java.text.DecimalFormat;

public class FloatMultiplication {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read two float numbers
        float num1 = scanner.nextFloat();
        float num2 = scanner.nextFloat();
        
        // Multiply the numbers
        float result = num1 * num2;
        
        // Format the result to two decimal places
        DecimalFormat df = new DecimalFormat("0.00");
        
        // Print the result
        System.out.println(df.format(result));
        
        scanner.close();
    }
}