package Concurrency.Thread_Class_Java;

public class ThreadEg extends Thread
{
    ThreadEg()
    {
    }
    ThreadEg(Runnable func)
    {
        super(func);
    }
    @Override
    public void run()   //  This method is an abstract one from the Thread class
    {
        System.out.println("Yo!! from thread " + this.getName());
    }

}
