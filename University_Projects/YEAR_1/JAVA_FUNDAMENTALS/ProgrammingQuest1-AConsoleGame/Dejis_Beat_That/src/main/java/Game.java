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

public class Game {
    public static int roundLimit = 0;
    public static int roundCount = 1;
    public static int numOfDie = 0;
    
    
    
    private static void ResetGame(Players players, Players.Human p1, Players.CPU cpu)
    {
        players.ResetAll(p1, cpu);
        //roundLimit = askNumOfRounds();
        roundCount = 1;
    }
    
    private static void addNewLine()
    {
        System.out.println("\n");
    }
    private static boolean askToContinue()
    {
        boolean ask = true;
        boolean decision = false;
        
        while (ask)
        {
            System.out.print("Do you want to continue (type y or n or yes or no)? ");
            
            try
            {
                BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
                String strDecision = (br.readLine()).toLowerCase();
                
                switch (strDecision)
                {
                    case "y":
                    case "yes":
                        System.out.println("You chose to continue...");
                        decision = true;
                        ask = false;
                        break;
                        
                    case "n":
                    case "no":
                        System.out.println("You chose not to continue...");
                        decision = false;
                        ask = false;
                        break;
                        
                    default:
                        System.out.println("You entered something invalide. Try again.");
                        decision = false;
                        ask = true;
                        break;
                }
            }
            catch (IOException ioExcp)
            {
                System.out.println("Try again. " + ioExcp.toString());
            }
        }
        
        return decision;
    }
    
    private static int askNumOfRounds()
    {
        boolean ask = true;
        int numOfRounds = 0;
        
        while (ask)
        {
            System.out.print("How many rounds do you want to go? Highest ten, or zero to quit. ");
            try
            {
                BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
                numOfRounds = Integer.parseInt(br.readLine());
                
                if (numOfRounds < 0 || numOfRounds> 10)
                {
                    System.out.println("Enter number of rounds between one and ten.");
                }
                else if (numOfRounds == 0)
                {
                    System.out.println("You entered zero, don't want to play right?");
                    ask = false;
                }
                else
                {
                    ask = false;
                }
            }
            catch(IOException ioexcp)
            {
                System.out.println("Try again.");
            }
            catch (NumberFormatException nfeExcp)
            {
                System.out.println("That is not a number. Try again");
            }
        }
        
        return numOfRounds;
    }
    
    private static int askNumOfDie() //  Prevents entering number less than zero or greater than 5
    {
        boolean ask = true;
        int numOfDie = 0;
        
        while (ask)
        {
            System.out.print("How many die do you want to play with, highest 7 die? ");
            try
            {
                BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
                numOfDie = Integer.parseInt(br.readLine());
                
                if (numOfDie <= 0 || numOfDie > 7)
                {
                    System.out.println("Enter number of rounds between one and seven.");
                }
                else
                {
                    ask = false;
                }
            }
            catch(IOException ioexcp)
            {
                System.out.println("Try again.");
            }
            catch (NumberFormatException nfeExcp)
            {
                System.out.println("That is not a number. Try again");
            }
        }
        
        return numOfDie;
    }
    
    //  THE MAIN GAME
    public static void GAME()
    {
        System.out.println("WELCOME! To BEAT THAT!");

        boolean start = false;
        
        //roundCount = 1;
        //numOfDie = 0;
        Players players = null;
        Players.Human p1 = null;
        Players.CPU cpu = null;
        
        
        do
        {  
            
            roundLimit = askNumOfRounds();
            if (roundLimit > 0)
            {
                numOfDie = askNumOfDie();
                //  Make players first
                players = new Players(numOfDie);
                p1 = players.new Human(); //  How to access a sub class
                cpu = players.new CPU();
                
                //  Resets everything
                ResetGame(players, p1, cpu);

                start = true;


                addNewLine();
                
                System.out.println("New Game!");
            }
           
            while (roundCount <= roundLimit)
            {
                System.out.print("ROUND " + roundCount + "!");
                
                addNewLine();
                
                players.display_players_scores(p1, cpu);
                
                addNewLine();
                
                p1.roll_die();
                cpu.roll_die(p1.score);
                
                if (p1.score > cpu.score)
                {
                    System.out.println(p1.name + " you're winning!");
                    p1.taunt(cpu.name);
                }
                else
                {
                    System.out.println(cpu.name + " is winning!");
                    cpu.taunt(p1.name);
                }
                
                addNewLine();
                
                roundCount++;
            }
            
            addNewLine();
            
            players.display_players_scores(p1, cpu);
            
            addNewLine();
            
            if ((p1 != null) && (cpu != null))
            {
                if (p1.score > cpu.score)
                {   System.out.println("GAME HAS ENDED! " + (p1.name).toUpperCase() + " WINS!");    }
                else
                {   System.out.println(cpu.name + " WINS!" + " END OF GAME!");  }

                boolean continueGame = askToContinue();
                if (continueGame == false)  //  exit game if don't want to continue
                {
                    start = false;   
                }
            }
         
        }
        while (start);
        
    }
    
    //  MAIN FUNCTION
    public static void main(String args[])
    {
        //DEBUG
        /*
        int numOfDie = askNumOfDie();   //  numOfDie can never be zero or less
        
        Players players = new Players(numOfDie);
        Players.Human p1 = players.new Human(); //  How to access a sub class
        p1.roll_die();
        p1.display_score();
        */
        
        GAME();
    }
}
