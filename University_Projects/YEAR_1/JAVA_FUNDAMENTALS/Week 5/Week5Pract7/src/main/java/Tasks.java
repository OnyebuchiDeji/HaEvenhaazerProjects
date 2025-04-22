/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author x7e30
 */
import java.io.*;

public class Tasks {
    public void task1()
    {
        int num1 = 0;
        int num2 = 3;
        try
        {
            System.out.println(num2 + " divided by " + num1 + " is " + (num2 / num1));    //  An error, can't divide by zero
        }
        catch(ArithmeticException exp)
        {
            //  This catches the exception or error, terminates the program after printng a useful message
            //  It returns a normal status code to operating system telling it of good exit status
            System.out.println("Cannot divide " + num2 + " by zero! Error: " + exp.toString());
        }
    }
    
    public void task2()
    {
        float floatingNum = 7.0f;
        try
        {
            System.out.println(floatingNum + " divided by zero = " + (floatingNum / 0));    //  An error, can't divide by zero
        }
        catch(ArithmeticException exp)
        {
            //  This catches the exception or error, terminates the program after printng a useful message
            //  It returns a normal status code to operating system telling it of good exit status
            System.out.println("Cannot divide by zero! Error: " + exp.toString());
        }
    } 
    
    public float stringToFloat(String strFloatNum)
    {
        float floatNum = 0.0f;
        try
        {
            floatNum = Float.parseFloat(strFloatNum);
        }
        catch (NumberFormatException nfeExp)
        {
            System.out.println("Yo! Check the format!" + nfeExp.toString());
        }
        
        return floatNum;
    }
    
    public void task3()
    {
        //float f_num1; float f_num2; //  These will never be read int the try-catch block
        //  They must be initializd before hand to be read
        float f_num1 = 0.0f;
        float f_num2 = 0.0f;
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        try
        {
            System.out.println("Enter a fractional type number: ");
            
            String strFloatNum = br.readLine(); //  first input
            f_num1 = stringToFloat(strFloatNum);
            
            System.out.println("Enter a second fractional type number: ");
            strFloatNum = br.readLine();        //  second input
            f_num2 = stringToFloat(strFloatNum);
        }
        catch(IOException ioexp)
        {
            System.out.println("Yo! there was an io error/exception! Check it! " + ioexp.toString());
        }
        
        System.out.println(f_num1 + " + " + f_num2 + " = " + (f_num1 + f_num2));
    }
   
    
}
