import java.util.Scanner;

public class BinaryToOctalConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read the number of queries
        int Q = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character
        
        for (int i = 0; i < Q; i++) {
            String binaryNumber = scanner.nextLine(); // Read the binary number
            // Convert binary to octal
            String octalString = binaryToOctal(binaryNumber);
            // Print the octal string
            System.out.println(octalString);
        }
        
        scanner.close();
    }

    // Method to convert binary to octal
    private static String binaryToOctal(String binary) {
        // Convert the binary string to a decimal integer
        int decimal = Integer.parseInt(binary, 2);
        // Convert the decimal integer to an octal string
        return Integer.toOctalString(decimal);
    }
}
