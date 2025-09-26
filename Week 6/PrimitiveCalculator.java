/*
 * Name: PrimitiveCalculator.java
 * Author: Noel Onate
 * Created: 9/25/25
 * Purpose: Calculate addition, subtraction,
 * multiplication, and division of two numbers
 */

 // Import TimeUnit and Scanner
 import java.util.concurrent.TimeUnit;
 import java.util.Scanner;

 public class PrimitiveCalculator {
    public static void main(String[] args) {
        // Create scanner object
        Scanner keyboard = new Scanner(System.in);

        // Create variables needed for program
        double num1;
        double num2;
        int operation;
        double result = 0;
        int time = 0;
        char menu;

        // Print title
        System.out.println("+---------------------------+");
        System.out.println("/         Primitive         \\");
        System.out.println("\\         Calculator        /");
        System.out.println("*---------------------------*");

        // Start menu loop
        while (true) {
            // Ask user for first number
            System.out.print("\nEnter the first number: ");
            num1 = keyboard.nextDouble();

            // Ask user for second number
            System.out.print("Enter the second number: ");
            num2 = keyboard.nextDouble();

            // Ask user for what operation to perform
            System.out.println("\nAddition (1)\nSubtraction (2)\nMultiplication (3)\nDivision (4)\n");
            System.out.print("Enter an operation: ");
            operation = keyboard.nextInt();

            // Perform chosen operation on the two numbers, set time value
            // More complicated operations means a higher time value
            switch (operation) {
                case 1:
                    result = num1 + num2;
                    time = 1;
                    break;
                case 2:
                    result = num1 - num2;
                    time = 2;
                    break;
                case 3:
                    result = num1 * num2;
                    time = 4;
                    break;
                case 4:
                    result = num1 / num2;
                    time = 5;
                    break;
            }

            // Sleep for time seconds then display result
            try {
                System.out.println("Calculating...");
                TimeUnit.SECONDS.sleep(time);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }

            System.out.printf("\nResult: %.2f\n", result);

            // Ask user if they want to run another calculation
            System.out.print("\nCalculate again (Y/N)? ");
            keyboard.nextLine();
            menu = keyboard.next().charAt(0);

            // Set user input to uppercase then do one of the following
            if (menu == 'y') {
                // If it was y, calculate again
                continue;
            } else {
                // Otherwise, say goodbye and exit loop
                System.out.println("Goodbye!");
                break;
            }
        }

        // Close Scanner object
        keyboard.close();
    }
 }

 