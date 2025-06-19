package Functional_Programming_Java.Functional_Interfaces;

public class Functional_Interfaces {
    public static void main(String[] args)
    {
        GreetingImpl g1 = new GreetingImpl();
        g1.printMessage();
        Greeting2 g2 = new Greeting2();
        g2.printMessage();

        //  So the issue with this is that a new class is made anytime...
        //  I want to use the same interface to do another thing.
        //  Though, more abstract functions can be added to the interface...
        //  For different greetings.
    }
}
