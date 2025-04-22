/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Ebenezer Ayo-Meti - 22021699 - x7e30
 */

import java.io.*;

class player
{
    String name = null;
    String word = null;
    int wordStatus = 0; //  A flag to determine whether the word agrees to any rule or not.
    int score = 0;
    
    player()
    {
        this.name = Utils.ask("Enter your name: ");
    }
}

public class wordGame 
{
    String[] wordsEntered = new String[3];
    boolean gameOver = false;
    boolean terminate = false;
    player p1 = new player();
    
    gameRulesApp gra = new gameRulesApp("dictionary.txt");
    
    wordGame()
    { 
    }
    
    public void gameRestart()
    {
        Utils.printText("Game is restarting...", true);
        //  Re-initializes everything
        wordsEntered = new String[3];
        gameOver = false;
        terminate = false;
        p1.score = 0;
    }
    
    public int wordValidate(String word)
    {
        int outcome = -2;
        
        //  If pure, agrees with rules, and exists...
        if (gra.checkNextWordCharacter(word, wordsEntered) == true && gra.isWordPure(word) == true && gra.exists(word) == true)
        {
            outcome = 1;
        }
        //  If repeated, game over!
        if (gra.repeated(word, wordsEntered))
        {
            outcome = 0;
        }
        //  If empty, restart
        if (gra.isWordEmpty(word))
        {   
            outcome = -1;
        }
        
        return outcome;
    }
    
    public void addToWordStore(String word)
    {   
        if (Utils.isArrayFull(wordsEntered))
        {
            wordsEntered = Utils.resizeArray(wordsEntered);
        }
        
        for (int i = 0; i < wordsEntered.length; ++i)
        {
            if (wordsEntered[i] == null)
            {
                wordsEntered[i] = word;
                break;  //  Immediately break once word is added
            }
        }
    }
    
    public void askWordInput()
    {
       
        boolean ask = true;
        try 
        {
            Utils.printText("Enter next word (caseSensitive) to play: ", true);
            
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            
            while (ask)
            {
                p1.word = br.readLine().trim();
                p1.wordStatus = wordValidate(p1.word);
                switch (p1.wordStatus)
                {
                    case 1:
                    
                        ask = false;
                        //  Only adds a completely valid word
                        addToWordStore(p1.word);
                        break;
                    case 0 :
                    
                        ask = false;
                        Utils.printText("Entered word is repeated.", true);
                        break;
                    case -1 :
                    
                        ask = false;
                        Utils.printText("Entered word is empty.", true);
                        break;
                    default :
                    
                        ask = true;
                        Utils.printText("Entered word is invalid or does not exist in the dictionary. Please try again", true);
                        break;
                }
            }
        }
        catch(IOException ioExcp)
        {
            System.out.println("There was an error in getting the input: " + ioExcp.toString());
        }
    }
    
    public void gameStart(String startingWord)
    {
        startingWord = startingWord.toLowerCase();
        
        Utils.printText("Welcome! To the Word Game!", true);
        
        Utils.printText("""
                        Your word must not have any numbers or any other characters apart from letters.
                        The word you enter must start with the last character of the previous word you entered.
                        If you enter nothing, the game will restart.
                        Also, no words are to be repeated.
                        Let's go!""", true);
        
        //  Checks if starting word is valid
        if (wordValidate(startingWord) == -2)
        {
            Utils.printText("Your word is invalid. Please, start with a new word.", true);
            terminate = true;
        }
        
        while (terminate == false)
        {
            
            Utils.printText("Starting word is " + startingWord, true);
            addToWordStore(startingWord);
            
            boolean reset = false;
            
            while (!gameOver)
            {
                askWordInput();
                switch(p1.wordStatus)
                {
                    case 0 -> 
                    {
                        gameOver = true;
                    }
                    case -1 ->
                    {
                        gameOver = true;
                        reset = true;
                    }
                    case 1 ->
                    {
                        ++p1.score;
                        Utils.printText("Your score is " + Integer.toString(p1.score), true);
                    }
                }
                
                Utils.printEnteredWords(this.wordsEntered);
            }
            
            Utils.printText("Game Over!", true);
            Utils.printText(p1.name + "'s score is: " + Integer.toString(p1.score), true);
            
            //Utils.printText("Size of store = " + Integer.toString(wordsEntered.length), true);
            
            if (!reset)
            {
                if (Utils.askRetry() == false)
                {
                    terminate = true;
                }
                else
                {
                    //  Resets all
                    gameRestart();
                }
            }
            else
            {
                //  Resets all
                gameRestart();
            }
        }
    }
}
