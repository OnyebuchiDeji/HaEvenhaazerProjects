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
    static void task4() throws IOException
    {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
        
        String floatString = br.readLine();
        float floatNum = Float.parseFloat(floatString);
        
        System.out.println("Your number is " + floatNum);
        System.out.println("Your number + 3.14 is" + (floatNum + 3.14));
    }
    
    static void task5() throws IOException
    {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
        
        System.out.println("What is your first name? ");
        String firstName = br.readLine();
        System.out.println("What is your second name? ");
        String secondName = br.readLine();
        System.out.println("When were you born? ");
        String yearOfBirth = br.readLine();
        int age = 2022 - Integer.parseInt(yearOfBirth);
        
        System.out.println("Your full name is " + firstName + ' ' + secondName + " /n You are " + age + " years old.");
    }
    public static void main(String[] args) throws IOException
    {
        //someTests tests = new someTests();
        
        /* //  From Task1:
        Task1 tsk1 = new Task1();
        tsk1.readString();   //  Since it is static, I can access it directly from the class.
        //Task1.readString();  //  Like this
        */
       Task1.doTask1();

        //  From Task3:
       Task3 tsk3 = new Task3();
       System.out.println(tsk3.readNum());
       
       task4();
        
    }

}

/*
class someTests
{
    void println(String text)   // methods are public by default
    {
        System.out.println(text);
        //printInt(2); // Caan't call non-static method from static method
    }
    
     public void printInt(int num)
    {
        System.out.println(num);
        //println("beans");   //  Can call static method from non-static method
    }
     
    void printChar(char sign)
    {
        System.out.println(sign);
    }
     
}
*/