
import BankAccounts.*;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Ebenezer Ayo-Meti - 22021699
 */

//  Used in Aoolication2.java
public class BankClient 
{
    String name;
    float monthlyIncome = 0;
    float monthlyOutgoings = 0;
    float annualLoanPay = 0;
    
    private LoanAccount LA = null;
    private SavingsAccount SA = null;
    private CurrentAccount CA = null;
    
    BankClient(String name, float annualIncome, float annualExpenses, float annualLoanPay)
    {
        this.name = name;
        monthlyIncome = annualIncome;
        monthlyOutgoings =annualExpenses;
        this.annualLoanPay = annualLoanPay;
    }
    
    public void setLoanAccount(float debtAmount)
    {
        this.LA = new LoanAccount(debtAmount);
    }
    
    //  When there is no starting amount
    public void setSavingsAccount()
    {
        this.SA = new SavingsAccount();
    }
    public void setSavingsAccount(float startingAmount)
    {
        this.SA = new SavingsAccount(startingAmount);
    }
    
    //  When there is no starting amount
    public void setCurrentAccount()
    {
        this.CA = new CurrentAccount();
    }
    public void setCurrentAccount(float startingAmount)
    {
        this.CA = new CurrentAccount(startingAmount);
    }
    
    /*  To provide access to these accounts */
    //  It returns the memory addresses of these objects
    //  So provides direct access
    public CurrentAccount getCurrentAccount()
    {
        if (this.CA == null)
        {
            System.out.println("Cannot access this because" + name + " does not have a" + CA.type + " account");
            return null;
        }

        return this.CA;
    }
    
    public SavingsAccount getSavingsAccount()
    {
        if (this.SA == null)
        {
            System.out.println("Cannot access this because" + name + " does not have a" + SA.type + " account");
            return null;
        }

        return this.SA;
    }
    
    public LoanAccount getLoanAccount()
    {
        if (this.LA == null)
        {
            System.out.println("Cannot access this because" + name + " does not have a" + LA.type + " account");
            return null;
        }

        return this.LA;
    }
    
}
