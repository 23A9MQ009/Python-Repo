import java.util.Scanner;
public class Square {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int side = scanner.nextInt();
        int area = side * side;
        int perimeter = 4 * side;
        System.out.println(area + " " + perimeter);
        scanner.close();
    }
}
