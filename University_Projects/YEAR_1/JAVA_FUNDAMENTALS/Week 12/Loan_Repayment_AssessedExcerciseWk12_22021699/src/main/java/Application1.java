/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Ebenezer Ayo-Meti - 22021699
 */

import BankAccounts.*;


class Utils
{
    public static void printText(String text, boolean newLine)
    {
        if (newLine)
        {
            System.out.println(text);
        }
        else
        {
            System.out.print(text);
        }
    }
}


public class Application1 {
    
    public static void John()
    {
        LoanAccount jLA = new LoanAccount(22000f);
        CurrentAccount jCA = new CurrentAccount();
        
        float monthlyIncome = 2600f;
        float monthlyOutgoings = 1300f;
        float annualLoanPay = 500f;
        boolean finishedPay = false;
        
        float remainingAmount = 0;
        
        int month = 0;
        
        while (!finishedPay)
        {
            ++month;
            
            remainingAmount += monthlyIncome;
            remainingAmount -= monthlyOutgoings;
            remainingAmount -= annualLoanPay;
            jLA.makePayment(annualLoanPay);
            jCA.makeDeposit(remainingAmount);
            remainingAmount = 0;
            
            jLA.addInterest();
            jCA.addInterest();
            
            if (jLA.getDebt() <= 0)
            {
                finishedPay = true;
            }
            //Utils.printText(Float.toString(jLA.getDebt()), true);
        }
        
        //Utils.printText(Float.toString(jLA.getDebt()), true);
        Utils.printText("John repaid his loan after " + month + " months. ", false);
        Utils.printText("His current account balance at that time was " + jCA.getBalance() + "£.", true);
    }
    
    public static void Mary()
    {
        LoanAccount mLA = new LoanAccount(18000f);
        SavingsAccount mSA = new SavingsAccount(200f);
        
        float monthlyIncome = 2800f;
        float monthlyOutgoings = 1400f;
        float annualLoanPay = 350f;
        boolean finishedPay = false;
        
        float remainingAmount = 0;
        
        int month = 0;
        
        while (!finishedPay)
        {
            ++month;
            
            remainingAmount += monthlyIncome;
            remainingAmount -= monthlyOutgoings;
            remainingAmount -= annualLoanPay;
            mLA.makePayment(annualLoanPay);
            mSA.makeDeposit(remainingAmount);
            remainingAmount = 0;
            
            mLA.addInterest();
            mSA.addInterest();
            
            if (mLA.getDebt() <= 0)
            {
                finishedPay = true;
            }
            //Utils.printText(Float.toString(mLA.getDebt()), true);
        }
        
        //Utils.printText(Float.toString(mLA.getDebt()), true);
        Utils.printText("Mary repaid her loan after " + month + " months. ", false);
        Utils.printText("Her current account balance at that time was " + mSA.getBalance() + "£.", true);

    }
    
    public static void main(String[] args)
    {
        John();
        Mary();
    }
}
