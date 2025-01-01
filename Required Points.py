import java.util.Scanner;
public class SpecialAttacks {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        int specialAttacks = B / A;
        System.out.println(specialAttacks);
        scanner.close();
    }
}
