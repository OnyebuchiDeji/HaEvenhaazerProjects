package Input_and_Output.The_Scanner;

import java.util.Scanner;

public class ScannerEG
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter your name please: ");
        String name = sc.nextLine();
        System.out.println(name);

        System.out.println("Enter thy age please: ");
        int age = sc.nextInt();
        System.out.println("Your age is: " + age);
        /*  NOTE!!!
        *   nextInt does not clear the newline character
        *   so when I try sc.nextLine() to get the user's input for occupation...
        *   The input stream takes in that lingering newline character...
        *   instead of waiting for and taking user input, which ought not to be...
        *
        *   The SOLS:
        *   1. Use nextLine() for the age, and convert value to an Integer.
        *   2. Use nextLine() after the nextInt for age that does not store the value the Scanner...
        *   returns. That is, it just removes the newline from the Stream.
        *   so that the .nextLine() for occupation actually waits to receive user input.
        */
        sc.nextLine();
        System.out.println("Enter thy occupation please: ");
        String occupation = sc.nextLine();
        System.out.println("Your occupation: " + occupation);
    }
}
