package Concurrency.Executor_Service;

import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;

public class ExecutorServiceEG
{
    public static void main(String[] args)
    {
        //  Using an Executable Service ES does not require a Threaf
        /*Thread t1 = new Thread(new RunnableEg());
        //  This can be done because Runnable is a functional interface
        Thread t2 = new Thread(()-> System.out.println("Hello world from a lambda style runnable!"));

        t1.start();
        t2.start();
*/
        ExecutorService eS = Executors.newFixedThreadPool(2);
        eS.submit(new RunnableEg());
        eS.submit(()-> System.out.println("Lambda function, a type of runnable, running in an Executable Service!!!"));

        eS.shutdown();
    }
}
