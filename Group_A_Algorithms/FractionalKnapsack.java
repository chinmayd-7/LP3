
import java.util.*;

public class FractionalKnapsack {

    static class Item {
        double value, weight, ratio;

        Item(double value, double weight) {
            this.value = value;
            this.weight = weight;
            this.ratio = value / weight;
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Number of items: ");
        int n = sc.nextInt();

        Item[] items = new Item[n];

        // Input items
        for (int i = 0; i < n; i++) {
            System.out.print("Enter value and weight of item "
                             + (i + 1) + ": ");

            double value = sc.nextDouble();
            double weight = sc.nextDouble();

            if (weight <= 0 || value < 0) {
                System.out.println("Invalid value or weight.");
                sc.close();
                return;
            }

            items[i] = new Item(value, weight);
        }

        System.out.print("Knapsack capacity: ");
        double capacity = sc.nextDouble();

        if (capacity < 0) {
            System.out.println("Invalid capacity.");
            sc.close();
            return;
        }

        // Sort by value/weight ratio (descending)
        Arrays.sort(items,
            (a, b) -> Double.compare(b.ratio, a.ratio));

        double totalValue = 0;

        // Select items using greedy method
        for (Item item : items) {

            if (capacity <= 0)
                break;

            double take = Math.min(capacity, item.weight);

            double valueTaken = take * item.ratio;

            totalValue += valueTaken;
            capacity -= take;

            System.out.println("Taken weight: " + take
                    + ", Value: " + valueTaken);
        }

        System.out.printf("Maximum value = %.2f%n", totalValue);

        sc.close();
    }
}
