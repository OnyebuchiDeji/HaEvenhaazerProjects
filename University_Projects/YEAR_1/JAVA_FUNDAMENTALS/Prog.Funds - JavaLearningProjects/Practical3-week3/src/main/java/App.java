/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author X7E30
 */
public class App
{
    public static void main(String[] args)  //  The main function
    {
        Program_1 prog1 = new Program_1();
        Program_2 prog2 = new Program_2();
        Program_3 prog3 = new Program_3();
        
        
        prog1.prog1Func1();
        prog2.prog2Func1();
        Program_3.addThings1(); //  Can replace with class reference because methods are static
        prog3.addThings2();
        prog3.addThings3();
        prog3.addThings4();
        
        
    }
}


class Program_1
{
    public void prog1Func1()
    {
        //byte thisYear = 2008;   //  Can't work range: -128 to 127
    byte smallNum = -2; //  byte can be negative. A byte type is 8bits, a byte
    
    System.out.println("This is " + smallNum);
    System.out.println("This is " + (smallNum));
    }
}

class Program_2
{
    public static void prog2Func1()    //  Can be static
    {
        int a = 1; int b = 13;
        
        System.out.println("a and b is united as " + a + b);
        System.out.println("But a + b is:/t" + (a + b));
    }
}

class Program_3
{
    public static void addThings1()
    {
        int a = 1;
        float b = 3.2F;
        
        System.out.println("Result is " + (a + b));
        System.out.println("Result is " + (a + b));
    }
    
    public static void addThings2()
    {
        char a = 'A';
        float b = 3.2F;
        
        System.out.println("Result is " + (a + b));
        System.out.println("Result is " + (a + b));
    }
    
    public static void addThings3()
    {
        int a = 1;
        short b = 24;
        
        System.out.println("Result is " + (a + b));
        System.out.println("Result is " + (a + b));
    }
    
    public static void addThings4()
    {
        int a = 1;
        byte b = 32;
        
        System.out.println("Result is " + (a + b));
        System.out.println("Result is " + (a + b));
    }
}