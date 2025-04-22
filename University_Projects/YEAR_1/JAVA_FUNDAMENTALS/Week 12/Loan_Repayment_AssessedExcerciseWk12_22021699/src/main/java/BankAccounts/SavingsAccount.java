/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package BankAccounts;

/**
 *
 * @author Ebenezer Ayo-Meti - 22021699
 */
public class SavingsAccount
{
    public String type = "Savings";
    static private float interestRate = 0.008f;
    private float balance;
    
    public SavingsAccount()
    {
        this.balance = 0.0f;
    }
    
    public SavingsAccount(float startingBalance)
    {
        this.balance = startingBalance;
    }
    
    public SavingsAccount(float startingBalance, float interestRate)
    {
        this.balance = startingBalance;
        SavingsAccount.interestRate = interestRate;
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
