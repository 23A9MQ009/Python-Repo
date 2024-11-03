import java.util.Scanner;

public class ASCIICode {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read a single character input from the user
        char ch = scanner.next().charAt(0);

        // Print the ASCII value of the character
        int asciiValue = (int) ch;
        System.out.println(asciiValue);
        
        scanner.close();
    }
}