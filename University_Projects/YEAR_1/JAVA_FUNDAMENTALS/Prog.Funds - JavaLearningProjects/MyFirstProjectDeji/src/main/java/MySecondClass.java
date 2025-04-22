/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author x7e30
 */
class MyThirdClass{
    void printManyTimes(int num, String name)
    {
        for (int i = 0; i < num; i++)
        {
            System.out.println("Yo!");
        }
        System.out.println(name + "!");
    }
}

public class MySecondClass {
       public void PrintThings()
    {
        String name;
        name = "Deji";
        System.out.println("My name is " + name);
        
        MyThirdClass Sth1 = new MyThirdClass();
        Sth1.printManyTimes(3, "Deji");
        
    }

}
