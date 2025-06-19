package Concurrency.Runnable_Interface;

public class Runnable_Interface
{
    public static void testMethod()
    {
        System.out.println("Thank God for today!");
    }
    public static void main(String[] args)
    {
        //  A runnable is just a method able to run on a thread...
        //  A Thread object automatically implements the runnable interface.
        /*
         * Using the runnable keyword is preferred to using an ordinary threa
         */
        Thread t1 = new Thread(new RunnableEg());
        //  This can be done because Runnable is a functional interface.
        //  And anywhere a functional interface is used, a lambda can be used in place...
        //  because a functional interface is generally just a method
        Thread t2 = new Thread(()-> System.out.println("Hello world from a lambda style runnable!"));
        //  A normal method cannot be used in place of where a functional interface or lambda method was to be.
        // Thread t3 = new Thread(testMethod());
        Thread t3 = new Thread(()->{testMethod();});
        
        t1.start();
        t2.start();
        t3.start();
    }
}
