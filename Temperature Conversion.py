import java.util.Scanner;

public class CelsiusToFahrenheit {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int celsius = scanner.nextInt();
        
        double fahrenheit = (celsius * 9.0 / 5.0) + 32;
        
        System.out.printf("%.2f%n", fahrenheit);
        
        scanner.close();
    }
}