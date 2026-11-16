
import java.util.Scanner;

public class NQueens {

    static int n, solutions = 0;

    // Check whether placing queen is safe
    static boolean safe(int[][] board, int row, int col) {

        // Check column above
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 1)
                return false;
        }

        // Check upper-left diagonal
        for (int i = row - 1, j = col - 1;
             i >= 0 && j >= 0; i--, j--) {

            if (board[i][j] == 1)
                return false;
        }

        // Check upper-right diagonal
        for (int i = row - 1, j = col + 1;
             i >= 0 && j < n; i--, j++) {

            if (board[i][j] == 1)
                return false;
        }

        return true;
    }

    // Backtracking function
    static void place(int[][] board, int row) {

        // All queens successfully placed
        if (row == n) {
            solutions++;

            System.out.println("Solution " + solutions + ":");

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    System.out.print(
                        board[i][j] == 1 ? "Q " : ". "
                    );
                }
                System.out.println();
            }

            System.out.println();
            return;
        }

        // Try each column
        for (int col = 0; col < n; col++) {

            if (safe(board, row, col)) {

                // Place queen
                board[row][col] = 1;

                // Move to next row
                place(board, row + 1);

                // Backtrack: remove queen
                board[row][col] = 0;
            }
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter N (1 to 15): ");
        n = sc.nextInt();

        if (n < 1 || n > 15) {
            System.out.println("Invalid N.");
            sc.close();
            return;
        }

        int[][] board = new int[n][n];

        // Place first queen at (0, 0)
        board[0][0] = 1;

        // Start placing remaining queens
        place(board, 1);

        System.out.println("Total solutions = " + solutions);

        sc.close();
    }
}
