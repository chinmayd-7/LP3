import java.util.*;

public class Huffman_prac {
    static class Node{
        char ch;
        int freq;
        Node left, right;

        Node(char ch, int freq){
            this.ch = ch;
            this.freq = freq;
        }
    }

    static void generateCodes(Node root, String code, Map<Character, String> codes){
        if(root==null)
            return;

        if(root.left==null && root.right==null){
            codes.put(root.ch, code.isEmpty() ? "0" : code);
            return;
        }

        generateCodes(root.left, code + "0", codes);
        generateCodes(root.right, code + "1", codes);
    }

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter text: ");
        String text = sc.nextLine();

        Map<Character, Integer> freq = new HashMap<>();
        for(char c: text.toCharArray()){
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        PriorityQueue<Node> pq= new PriorityQueue<>((a, b) -> Integer.compare(a.freq, b.freq));
        for(char c: freq.keySet()){
            pq.add(new Node(c, freq.get(c)));
        }

        while(pq.size() > 1){
            Node left = pq.poll();
            Node right = pq.poll();
            Node newNode = new Node('\0', left.freq + right.freq);
            newNode.left = left;
            newNode.right = right;
            pq.add(newNode);
        }

        Node root = pq.poll();
        Map<Character, String> codes = new HashMap<>();
        generateCodes(root, "", codes);

        System.out.println("Huffman Codes:");
        System.out.println(codes);

        String encodedText = "";
        for(char c: text.toCharArray()){
            encodedText += codes.get(c);
        }
        System.out.println("Encoded Text: " + encodedText);
    }
}
