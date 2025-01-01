import java.util.Scanner;
public class DiskCapacity {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        int S = scanner.nextInt();
        int B = scanner.nextInt();
        long totalBytes = 2 * T * S * B * 512;
        long capacityKB = totalBytes / 1024;
        System.out.println(capacityKB + " KB");
        scanner.close();
    }
}
