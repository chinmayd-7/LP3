
import java.util.*;

public class HuffmanEncoding {

    // Node of Huffman Tree
    static class Node {
        char ch;
        int freq;
        Node left, right;

        Node(char ch, int freq) {
            this.ch = ch;
            this.freq = freq;
        }
    }

    // Generate Huffman Codes
    static void generateCodes(Node root, String code,
                              Map<Character, String> codes) {

        if (root == null)
            return;

        // Leaf node
        if (root.left == null && root.right == null) {
            codes.put(root.ch, code.isEmpty() ? "0" : code);
            return;
        }

        generateCodes(root.left, code + "0", codes);
        generateCodes(root.right, code + "1", codes);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter text: ");
        String text = sc.nextLine();

        if (text.isEmpty()) {
            System.out.println("Empty input.");
            return;
        }

        // Step 1: Calculate frequency
        Map<Character, Integer> freq = new HashMap<>();

        for (char c : text.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        // Step 2: Create Min Priority Queue
        PriorityQueue<Node> pq = new PriorityQueue<>(
            (a, b) -> Integer.compare(a.freq, b.freq)
        );

        // Step 3: Insert characters into queue
        for (char c : freq.keySet()) {
            pq.add(new Node(c, freq.get(c)));
        }

        // Step 4: Build Huffman Tree
        while (pq.size() > 1) {

            Node left = pq.poll();
            Node right = pq.poll();

            Node parent = new Node(
                '\0', left.freq + right.freq
            );

            parent.left = left;
            parent.right = right;

            pq.add(parent);
        }

        // Step 5: Generate Huffman Codes
        Node root = pq.poll();

        Map<Character, String> codes = new HashMap<>();

        generateCodes(root, "", codes);

        // Step 6: Display Huffman Codes
        System.out.println("\nHuffman Codes:");

        for (char c : freq.keySet()) {
            System.out.println(c + " : " + codes.get(c));
        }

        // Step 7: Encode text
        StringBuilder encoded = new StringBuilder();

        for (char c : text.toCharArray()) {
            encoded.append(codes.get(c));
        }

        System.out.println("\nEncoded Text: " + encoded);

        sc.close();
    }
}
