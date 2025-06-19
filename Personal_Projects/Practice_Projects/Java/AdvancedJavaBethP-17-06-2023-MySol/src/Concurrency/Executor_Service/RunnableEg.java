package Concurrency.Executor_Service;

public class RunnableEg implements Runnable
{
    @Override
    public void run()   //  This method is an abstract one from the Thread class
    {
        System.out.println("Yo!! from a runnable");
    }

}
