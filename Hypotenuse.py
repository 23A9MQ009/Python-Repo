import java.util.Scanner;
public class Hypotenuse {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int X = scanner.nextInt();
        int Y = scanner.nextInt();
        double hypotenuse = Math.sqrt(X * X + Y * Y);
        System.out.printf("%.2f\n", hypotenuse);
        scanner.close();
    }
}
