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
        System.out.println("Welcome! To the class discerner.");
        getScore();
        //validateScoreRange();
       // printClass();
    }
    
    public static int changeToInt(String strNum)
    {
        int num = -1;
        try
        {
            num = Integer.parseInt(strNum);
            if (num >= 0 && num <= 100)
            {
                System.out.println("Your score is: " + num);
            }
            else
            {
                System.out.println("Yo! Enter a number between 0 to 100");
            }
        }
        catch(NumberFormatException nfExp)
        {
            System.out.println("Not a number! Enter a number please! Between 0 to 100. ");// + nfExp.toString());
        }
        
        return num;
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
                System.out.println("Enter your score between 0 to 100: ");
                mark = br.readLine();
                int intMark = changeToInt(mark);
                if (intMark >= 0 && intMark <= 100)
                {
                    startLoop = false;
                }
            }
            catch(IOException ioexcp)
            {
                System.out.println("Enter your score between 0 to 100. Check it! " + ioexcp.toString());
            }

        }
    }
}
