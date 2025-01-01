import java.util.Scanner;
public class InchesToCentimeters {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int inches = scanner.nextInt();
        double centimeters = inches * 2.54;
        System.out.printf("%.2f\n", centimeters);
        scanner.close();
    }
}
