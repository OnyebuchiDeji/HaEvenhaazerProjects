package Functional_Programming_Java.Lambdas;

public class Lambdas
{
    public static void main(String[] args)
    {
        //  The brackets take in arguments into the lambda functions
        Greeting yo = ()-> System.out.println("YO!!!");
        yo.printMessage();
        Greeting He = ()-> System.out.println("God is good");
        He.printMessage();
        Greeting goodDay = () -> System.out.println("Good day!!!");
        goodDay.printMessage();

        Greeting manyGreetings = ()->
        {
            System.out.println("\nGood day!");
            System.out.println("Good morning!");
            System.out.println("Good afternoon!");
            System.out.println("Good evening!");
            System.out.println("Good night!");
        };

        manyGreetings.printMessage();
    }


}
