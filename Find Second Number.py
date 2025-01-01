import java.util.Scanner;
public class FindSecondNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int X = scanner.nextInt();
        int Y = scanner.nextInt();
        int secondNumber = 2 * X - Y;
        System.out.println(secondNumber);
        scanner.close();
    }
}
