/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package BankAccounts;

/**
 *
 * @author Ebenezer Ayo-Meti - 22021699
 */
public class LoanAccount
{
    public String type = "Loan";
    static private float interestRate = 0.012f;
    private float debt;
    

    
    public LoanAccount(float borrowedAmount)
    {
        this.debt = borrowedAmount;
    }
    
    public LoanAccount(float borrowedAmount, float interestRate)
    {
        this.debt = borrowedAmount;
        LoanAccount.interestRate = interestRate;
    }
    
    public float getDebt()
    {
        return debt;
    }
    
    public void addInterest()
    {
        debt += (interestRate * debt);
    }
    
    public void makePayment(float payment)
    {
        this.debt -= payment;
    }
}
