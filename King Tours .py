import java.util.Scanner;
public class KingTours {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt(); 
        int M = scanner.nextInt();  
        int totalPeople = (N * 5) + (M * 7);
        System.out.println(totalPeople);
        scanner.close();
    }
}
