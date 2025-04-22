/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Ebenezer Ayo-Meti - 22021699 - x7e30
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Utils
{
    public static void printText(String text, boolean newLine)
    {
        if (newLine)
        {
            System.out.println(text);
    
        }
        else
        {
            System.out.print(text);
        }
    }
    
    
    public static boolean isArrayFull(String[] array)
    {
        boolean isFull = false;
        if (array[array.length-1] != null)
        {
            isFull = true;
        }
        
        return isFull;
    }
    
    public static String[] resizeArray(String[] array)
    {
        String[] tempArray = array;
        
        array = new String[array.length + 3];
        
        for (int i = 0; i < tempArray.length; ++ i)
        {
            array[i] = tempArray[i];
        }
        
        return array;
    }
    
    public static void printEnteredWords(String[] wordsEntered)
    {
        Utils.printText("You've entered: ", true);
        for (int i = 0; i < wordsEntered.length; ++i)
        {
            if (wordsEntered[i] != null)
            {
                Utils.printText(wordsEntered[i] + " ", false);
            }
            else
            {
                break;
            }
            
            if (((i % 5) == 0 ) && (i != 0))
            {
                Utils.printText("\n", false);
            }
        }
        Utils.printText("\n", false);
    }
    
    
    public static boolean askRetry()
    {
        String response = null;
        boolean boolResponse = false;
        boolean ask = true;
        
        String yes = "yY";
        String no = "Nn";
        
        try
        {
            Utils.printText("Do you want to play again? (type Y or y, n or N, yes, or no)", true);
            
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            
            while (ask)
            {
                response = br.readLine();
                
                if (yes.contains(response) || response.equals("yes") || response.equals("Yes"))
                {
                    boolResponse = true;
                    ask = false;
                }
                else if(no.contains(response) || response.equals("No") || response.equals("no"))
                {
                    Utils.printText("You do not want to play again.", true);
                    boolResponse = false;
                    ask = false;
                }
                else
                {
                    Utils.printText("You entered something invalid. Please, try again", true);
                    ask = true;
                }
            }
        }
        catch(IOException ioExcp)
        {
            System.out.println("There was an error in getting the input: " + ioExcp.toString());
        }
        
        return boolResponse;
    }
    
    public static String ask(String question)
    {
        String answer = null;
        boolean ask = true;
        
        try
        {
            Utils.printText(question, true);
            
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            
            while (ask)
            {
                answer = br.readLine();
                
                if (answer.equals("") || answer.equals(" "))
                {
                    Utils.printText("You entered something invalid. Please, try again", true);
                    ask = true;
                }
                else
                {
                    ask = false;
                }
            }
        }
        catch(IOException ioExcp)
        {
            System.out.println("There was an error in getting the input: " + ioExcp.toString());
        }
        
        return answer;
    }
}

