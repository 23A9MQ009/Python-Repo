import java.util.Scanner;

public class OctalToBinaryConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read the number of queries
        int Q = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character
        
        for (int i = 0; i < Q; i++) {
            String octalNumber = scanner.nextLine(); // Read the octal number
            // Convert octal to binary
            String binaryString = octalToBinary(octalNumber);
            // Print the binary string
            System.out.println(binaryString);
        }
        
        scanner.close();
    }

    // Method to convert octal to binary
    private static String octalToBinary(String octal) {
        // Convert the octal string to a decimal integer
        int decimal = Integer.parseInt(octal, 8);
        // Convert the decimal integer to a binary string
        return Integer.toBinaryString(decimal);
    }
}
