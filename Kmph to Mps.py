import java.util.Scanner;
public class KmphToMps {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int kmph = scanner.nextInt();
        double mps = kmph * 5.0 / 18.0;
        System.out.printf("%.2f\n", mps);
        scanner.close();
    }
}
