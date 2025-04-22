/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package BankAccounts;

/**
 *
 * @author Ebenezer Ayo-Meti - 22021699
 */
public class CurrentAccount
{
    public String type = "Current";
    static private float interestRate = 0.0006f;
    private float balance;
    
    public CurrentAccount()
    {
        this.balance = 0.0f;
    }
    
    public CurrentAccount(float startingBalance)
    {
        this.balance = startingBalance;
    }
    
    public CurrentAccount(float startingBalance, float interestRate)
    {
        this.balance = startingBalance;
        CurrentAccount.interestRate = interestRate;
    }
    
    public float getBalance()
    {
        return balance;
    }
    
    public void addInterest()
    {
        balance += (interestRate * balance);
    }
    
    public void makeDeposit(float deposit)
    {
        this.balance += deposit;
    }
    
}
