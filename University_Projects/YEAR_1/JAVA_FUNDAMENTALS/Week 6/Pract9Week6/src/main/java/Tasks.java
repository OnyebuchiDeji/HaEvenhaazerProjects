/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author X7E30
 */
import java.io.*;

public class Tasks {

    public static void main(String args[])
    {
        System.out.println("WELCOME! TO THE CLASS DISCERNER.");
        getScore();
    }
    
    public static void determineClass(int score)
    {
  
        System.out.print("Your class is: ");
        if (score >= 0 && score <= 39)
        {
            System.out.print("Fail!");
        }
        else if(score >= 40 && score <= 49)
        {
            System.out.print("Third class!");
        }
        else if(score >= 50 && score <= 59)
        {
            System.out.print("Second class, division 2, 2.2!");
        }
        else if(score >= 60 && score <= 69)
        {
            System.out.print("Second class, division 1, 2.1!");
        }
        else
        {
            System.out.print("First class!");
        }
        System.out.println(" with a score of " + score);
    }
    
    public static int changeToInt(String strNum)
    {
        int num = -1;
        try
        {
            num = Integer.parseInt(strNum);
            if (num < 0 || num > 100)
            {
                System.out.println("Yo! Enter a number between 0 to 100\n");
            }
        }
        catch(NumberFormatException nfExp)
        {
            System.out.println("Not a number! Enter a number please! Between 0 to 100. \n");// + nfExp.toString());
        }
        
        return num; //  returns -1 if strNum or mark is not within range
    }

    public static void getScore()
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        boolean startLoop = true;
        while(startLoop)
        {
            String mark = null;
            
            try
            {
                System.out.print("Enter your score between 0 to 100: ");
                mark = br.readLine();
                int markNum = changeToInt(mark);
                
                if (markNum >= 0 && markNum <= 100) //  Only runs when mark is within range
                {
                    determineClass(markNum);
                    startLoop = false;
                }
            }
            catch(IOException ioexcp)
            {
                System.out.println("Your score has to be between 0 to 100! Check it! " + ioexcp.toString());
            }

        }
    }
}
