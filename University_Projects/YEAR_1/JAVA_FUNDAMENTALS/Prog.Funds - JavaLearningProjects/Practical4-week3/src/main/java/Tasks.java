/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author x7e30
 */

//import java.lang.Math; // Not necessary but your program will still work.


public class Tasks {
    public static void main(String[] args)
    {
        Program.Task2();    //  Can be done this way because the method, Task2 is static
        Program.Task3();
        
    }
    
public class Program
{
    public static void Task2()
    {
        int a = 2;
        int b = 4;
        float c = 2.0F;
        float d = 4.0F;
        System.out.println("a/b = " + (a/b));   //  =0
        System.out.println("c/d = " + (c/d));   // =0.5
        System.out.println("a/d = " + (a/d));   // = 0.5
        System.out.println("c/b = " + (c/b));   // = 0.5
    }


    public static void Task3()
    {
        int a = -2;
        float b = 4.2F;
        System.out.println("The absolute value of a is " + Math.abs(a));
        System.out.println("The absolute value of b is " + Math.abs(b));
    }

}
/*    static void Task1a()
    {
        short a = 5; 
        short b = 8; 
        //byte c = (a + b); // Evaluates to int so needs narrowing cast
        //  So that it an initialize variable byte c
        byte c = (byte)(a + b);      
    }
    static void Task1b()
    {
        short a = 5; 
        short b = 8; 
        /* 
        Expression also evaluates to int so needs narrowing cast into a short
        so that it can initialize the variable c
        short c = (a + b);  
        System.out.println("Bytes" + a + '+' + b + '=' + c);
 */ /*  
    static void Task1c()
    {
        int a = 5; 
        int b = 8; 
        /* 
        Expression also evaluates to int so needs narrowing cast into a short
        so that it can initialize the variable c
        *//*
        int c = (a + b);  
        System.out.println("Bytes" + a + '+' + b + '=' + c);
    }
    static void Task1d()
    {
        double a = 5; 
        float b = 8; 
        /* 
        Expression also evaluates to int so needs narrowing cast into a short
        so that it can initialize the variable c
        *//*
        long c = (a + b);  
        System.out.println("Bytes" + a + '+' + b + '=' + c);
    }
*/
}
