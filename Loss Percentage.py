import java.util.Scanner;
public class LossPercentage {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double cp = scanner.nextDouble();
        double sp = scanner.nextDouble();
        double loss = cp - sp;
        double lossPercentage = (loss / cp) * 100;
        System.out.printf("%.2f\n", lossPercentage);
        scanner.close();
    }
}
