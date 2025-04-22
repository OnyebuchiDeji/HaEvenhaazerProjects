import java.io.*;

public class Game
{
    public static void main(String[] args) throws IOException
    {
        
        int userScore = 0;
        int computerScore = 0;
        
        Die die1 = new Die(); 
        Die die2 = new Die(); 

        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
        
        String userInput;
                
        int rounds = 1;

        System.out.println("\n\nNEW GAME\n");
        
        do {
            
            System.out.println("Round " + rounds + ": User's score: " + userScore + ", Computer's score: " + computerScore + "\n"); 

            
            // User's turn
            
            
            // Computer's turn
            
            
            rounds++;
            
        } while(rounds <= 10);
        
        // Announce the winner here

        
    }
}
