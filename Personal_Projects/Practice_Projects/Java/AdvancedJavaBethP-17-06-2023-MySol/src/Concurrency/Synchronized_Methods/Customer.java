package Concurrency.Synchronized_Methods;

import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;

public class Customer
{
    public static void main(String[] args)
    {
        ATM atm = new ATM();
        BankAccount account = new BankAccount();

        //  An ExecutorService is like a thread manager object.
        //  It manages the thread and is used to call methods to run on that thread.
        //  It can give info on the thread, and destroys the thread when it is done.
        ExecutorService eS = Executors.newFixedThreadPool(2);
        //  First Call
        eS.submit(()->atm.withdraw(account, 100));
        //  Second Call
        eS.submit(()->atm.withdraw(account, 100));
        //  Because of the synchronized keyword for the withdraw() method...
        //  The first call must finish before the next can continue -- Synchronization.

        eS.shutdown();
    }
}
