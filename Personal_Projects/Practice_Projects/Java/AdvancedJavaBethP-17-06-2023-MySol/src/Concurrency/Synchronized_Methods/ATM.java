package Concurrency.Synchronized_Methods;

public class ATM
{
    /*
     *   If not for this synchronized keyword, these would happen:
     *   both threads created in this customer account would access the ATM method...
     *   at the same time, causing them both to withdraw a 100, although the amount in...
     *   the bank account is initially 100, and the ATM method prevents withdrawal when...
     *   the balance in the account is less than 0
     *   but because both threads access at the same time, they bypass that if statement.
     *   This causes the amount remaining after they both withdraw to be -100.
     *   In conclusion, the synchronized keyword ensures that regardless of how many times...
     *   the method is called, the first called method is executed before the next...
     *   this prevents the above mentioned error of two methods in different threads trying to access the same resource...
     *   when the synchronise method is not used, Java tries to cope with it by giving the two routines, the method called...
     *   ...on different threads and thus acting almost parallel, a copy of that resource, so they both can have it.
     *   So synchronize ensures the first called thread finishes before the next continues.
     * */
    public synchronized void withdraw(BankAccount account, int amount)
    {
        int balance = account.getBalance();
        if ((balance - amount) < 0)
        {
            System.out.println("Transaction Denied! Insufficient Balance in Account!");
        }
        else
        {
            System.out.println("Handling transaction...");
            account.debit(amount);
            System.out.println("$" + amount + " withdrawn.");
        }
        System.out.println("Current Balance: " + account.getBalance());
    }
}
