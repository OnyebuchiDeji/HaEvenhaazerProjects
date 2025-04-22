/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package week8pract13;

/**
 *
 * @author Ebenezer Ayo-Meti
 */

public class ArraysWeek8Pract13 {
    static Dice dice = new Dice();
    
    private static void debug() //  Was a test for why 1 was never an outcome
    {   //  It was simply because when two die are rolled, one can never be given. Lowes tis 2
        
        /*
            if (possibleOutcomes[dieThrows] == 1)
            {
                System.out.println(possibleOutcomes[dieThrows] + " has occured!");
            }
            */
    }
    private static int rollDie(int numOfDie)
    {
        int score = 0;
        
        for (int rolls = 0; rolls < numOfDie; ++rolls)
        {
            dice.roll();
            
            score += dice.outcome;
        }
        
        return score;
    }
    
    //private static void askNumOf
    
    public static void main(String[] args) {
        
        int numOfDie = 3;
        int numberOfThrows = 100000;
        int[] possibleOutcomes = new int[numberOfThrows];
        int[] occurences = new int[numOfDie * 6]; //  All are zero initialized
        int occurencesIndexLimit = occurences.length;
        
        
        for (int dieThrows = 0; dieThrows < numberOfThrows; ++dieThrows)
        {
            possibleOutcomes[dieThrows] = rollDie(numOfDie);
            
            //  It uses the indexes to count which occurs the most
            occurences[possibleOutcomes[dieThrows] - 1]++;  //  This counts the sum outcome that occurs the most
            
        }
        
        for (int index = 0; index < occurencesIndexLimit; ++index)
        {
            System.out.println((index + 1) + " occurs " + occurences[index] + " times!");
        }
        
        int largest = 0;
        int currentValue = 0;
        int nextValue = 0;
        
        for (int index = 0; index < occurencesIndexLimit; ++index)
        {
            currentValue = occurences[index];
            if ((index + 1) < occurencesIndexLimit)
            {
                nextValue = occurences[index + 1];
            }
            
            if (currentValue > nextValue & largest < currentValue )
            {
                largest = currentValue;
            }
            else if (nextValue > currentValue & largest < nextValue)
            {
                largest = nextValue;
            }
            
        }
        
        System.out.println("Largest, the most likely outcome was: " + largest);
    }
}
