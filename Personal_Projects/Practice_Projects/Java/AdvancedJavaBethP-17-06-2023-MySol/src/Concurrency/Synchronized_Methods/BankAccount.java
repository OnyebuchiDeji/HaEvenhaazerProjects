package Concurrency.Synchronized_Methods;

public class BankAccount
{
    private int balance = 100;

    public BankAccount(){}

    public BankAccount(int deposited)
    {
        balance = deposited;
    }

    public void debit(int amount)
    {
        balance -= amount;
    }

    public int getBalance()
    {
        return balance;
    }
}
