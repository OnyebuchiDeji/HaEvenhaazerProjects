/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author x7e30
 */

import java.io.*;
//mport java.lang.Math;

public class Players
{
    Dice dice = new Dice(); //  All players use the same die
    int numOfDie = 0;       //  numOfDie the same for all players
    
    Players(int numberOfDie)
    {
        numOfDie = numberOfDie;
    }
    
    public void display_players_scores(Human p1, CPU cpu)
    {
        p1.display_score();
        System.out.println(" ");
        cpu.display_score();
    }
    
    public void ResetAll(Human p1, CPU cpu)
    {
        p1.score = 0;
        p1.roll = false;
        
        cpu.score = 0;
        cpu.roll = false;  
    }
    
    private int highestPossibleScore()
    {
        double HPS = 0;
        
        //  expDecr is exponent decrement: how much I will be reducing the exponent...
        //  each loop
        for (int expDecr = 0; expDecr < numOfDie; ++expDecr)
        {
            int decr = (numOfDie - expDecr) - 1;
            
            HPS = HPS + (9 * Math.pow(10, decr));
        }
        
        return (int)HPS;
    }
    
    private String getScore()
    {
        String unsortedScore = null;
        
        for (int time = 0; time < numOfDie; ++time)
        {
            int digit = dice.roll_die();

            if (unsortedScore == null)
            {
                unsortedScore = String.valueOf(digit);
            }
            else
            {
                unsortedScore = unsortedScore + String.valueOf(digit);
            }
        }
        
        return unsortedScore;
    }
    
    private String sort_score(String strScore)   //  Sorting in descending order, bigger to smaller
    {
        char[] charScore = strScore.toCharArray();
        int arrayLimit = strScore.length() - 1;
        
        for (int counter = 0; counter < strScore.length(); ++counter)
        {
            
            // Pointer is intitialized by counter and incremented by 1

            int pointer = (counter + 1);  //  made pointer the index of next value.
            if (pointer > arrayLimit)    //  pointer cannot be greater than 4 because it is used to index presentValue
            {
                break;  // Because the maximum index is 5 due to the number of die.
            }
            
            //  The maximum index for charScore is 4
            int presentValue = Integer.parseInt(String.valueOf(charScore[pointer]));    // the value ahead, that the pointer is pointing to
            int previousValue = Integer.parseInt(String.valueOf(charScore[pointer - 1]));   //  the value before
            

            
            if ( (pointer <= arrayLimit) && (previousValue < presentValue) )
            {
                do
                {
                    presentValue = Integer.parseInt(String.valueOf(charScore[pointer]));    // the value ahead
                    previousValue = Integer.parseInt(String.valueOf(charScore[pointer - 1]));   //  the value before
                    char temp = charScore[pointer - 1]; // Holds the smaller previous value
                    charScore[pointer - 1] = charScore[pointer]; //  Chanegs the previous value to the bigger next value
                    charScore[pointer] = temp;  //  Changes the bigger next value to the smaller;
                    
                    --pointer;
                }
                while ((previousValue < presentValue) && pointer > 0); // It does this loop when the condition is met and the pointer is higher than zero, still withi the array
            }                                                    //  This is so that it can move back and compare previous values for if the still obe
        }
        
        return String.valueOf(charScore);
    }
    
    //  THE HUMAN'S CLASS
    public class Human
    {
        String name = null;
        int score = 0;
        boolean roll = false;   //  If not roll, pass
 
        
        Human() //  Constructor that asks for name
        {
            prompt_name();  //  Constructor calls the prompt_name to ask for name
        }
        
        public void display_score()
        {
            System.out.print(name + "'s score is " + score);
        }
        
        public void taunt(String oponentName)
        {
            System.out.println("Beat that " + oponentName + "!");
        }
        
        private void prompt_name()  //  By setting this as private, it removes the warning of overridable method call in constructor
        {
            boolean ask = true;
            while (ask)
            {
                System.out.print("What is your name: ");
                try
                {
                    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
                    name = br.readLine();
                    ask = false;
                }
                catch(IOException ioexcp)
                {
                    System.out.println("Try again.");
                }     
            }
        }
        
        private void roll_or_pass()
        {
            boolean ask = true;
            
            while (ask)
            {
                System.out.print("Do you want to roll or pass? (type r or p or roll or pass) ");
                try
                {
                    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
                    String decision = br.readLine();
                    
                    switch(decision)
                    {
                        case "R":
                        case "r":
                        case "roll":
                        case "Roll":
                        case "ROLL":
                            System.out.println(name + " has rolled!");
                            roll = true;
                            ask = false;
                            break;
                            
                        case "P":
                        case "p":
                        case "pass":
                        case "Pass":
                        case "PASS":
                            System.out.println(name + " chose to pass!");
                            roll = false;
                            ask = false;
                            break;
                            
                        default:
                            System.out.println(name + " entered invalid input. Try again");
                            ask = true;
                            roll = false;
                            break;
                    }
                    
                    
                }
                catch(IOException ioexcp)
                {
                    System.out.println("Try again.");
                }     
            }
        }
        
        
        
        public void roll_die()
        {
            
            roll_or_pass(); //    Ask whether to roll or pass            
            
            if (roll)
            {
                String unsortedStrScore = getScore();
                //  Used to debug
                //System.out.println("The unsorted score is: " + unsortedStrScore);

                score = Integer.parseInt(sort_score(unsortedStrScore));
            }
            else
            {
                System.out.println(name + " passed!");
            }
            
        }
    }
    
    //  THE CPU'S CLASS
    public class CPU
    {
        String name = "CPU";
        int score = 0;
        boolean roll = false;
        int lowestCpuScore = 0;
        
        public void display_score()
        {
            System.out.print(name + "'s score is " + score);
        }
        
        public void taunt(String oponentName)
        {
            System.out.println("Beat that " + oponentName + "!");
        }
        
        private void randomLowestScore()
        {
            
            double x = Math.random();   //  returns a random value btw 0 - 1
            x = 1.0 + (x * highestPossibleScore()); //  x is a random value gotten form highest possible score
        
            lowestCpuScore = (int)Math.floor(x);
            
        }
        
        private void roll_or_pass(int oponentScore)
        {
            randomLowestScore(); // This calculates a random lowest score that the cpu is deciding on
            
            if (oponentScore < score || score <= lowestCpuScore)
            {
                System.out.println(name + " has rolled!");
                roll = true;
            }
            else
            {
                roll = false;
            }
        }
        
        public void roll_die(int oponentScore)
        {
            roll_or_pass(oponentScore);
           
            if (roll)
            {
                String unsortedStrScore = getScore();
                score = Integer.parseInt(sort_score(unsortedStrScore));
            }
            else
            {
                System.out.println("CPU passed!");
            }
        }
    }
}
