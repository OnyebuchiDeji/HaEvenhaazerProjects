package Concurrency.Thread_Class_Java;

public class Concurrency
{
    public static void main(String[] args)
    {
        /*
            The Below does not work because the run() method used...
            In the ThreadEg class is not abstract
            ThreadEg t1 = new ThreadEg(()->
                System.out.println("God is good!")
            );
         */
        ThreadEg t1 = new ThreadEg();
        ThreadEg t2 = new ThreadEg();

        t1.setName("T1");
        t2.setName("T2");
        t1.start();
        t2.start();

    }
}
