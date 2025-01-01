import java.util.Scanner;
public class InstantNoodles {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int X = scanner.nextInt();
        int Y = scanner.nextInt();
        int maxCustomers = X * Y;
        System.out.println(maxCustomers);
        scanner.close();
    }
}
