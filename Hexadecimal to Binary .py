import java.util.Scanner;

public class HexToBinaryConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read the number of queries
        int Q = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character
        
        for (int i = 0; i < Q; i++) {
            String hexNumber = scanner.nextLine(); // Read the hexadecimal number
            // Convert hex to binary
            String binaryString = hexToBinary(hexNumber);
            // Print the binary string
            System.out.println(binaryString);
        }
        
        scanner.close();
    }

    // Method to convert hexadecimal to binary
    private static String hexToBinary(String hex) {
        // Parse the hex number to an integer
        int decimal = Integer.parseInt(hex, 16);
        // Convert the integer to a binary string
        String binary = Integer.toBinaryString(decimal);
        // Pad with leading zeros to make it 8 bits for each hex digit
        StringBuilder paddedBinary = new StringBuilder();
        
        // Each hex digit represents 4 binary digits
        for (char hexChar : hex.toCharArray()) {
            // Convert each hex character to a 4-bit binary representation
            String binarySegment = String.format("%4s", Integer.toBinaryString(Integer.parseInt(String.valueOf(hexChar), 16))).replace(' ', '0');
            paddedBinary.append(binarySegment);
        }

        return paddedBinary.toString();
    }
}
