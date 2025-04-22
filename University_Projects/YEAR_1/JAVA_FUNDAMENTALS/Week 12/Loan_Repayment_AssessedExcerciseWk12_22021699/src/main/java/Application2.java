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


public class Application2 {
    
    public static void John()
    {
        BankClient John = new BankClient("John", 2600, 1300, 500);
        
        John.setLoanAccount(22000);
        John.setCurrentAccount();
        
        boolean finishedPay = false;
        float remainingAmount = 0;
        int month = 0;
        
        while (!finishedPay)
        {
            ++month;
            
            remainingAmount += John.monthlyIncome;
            remainingAmount -= John.monthlyOutgoings;
            remainingAmount -= John.annualLoanPay;
            
            John.getLoanAccount().makePayment(John.annualLoanPay);
            John.getCurrentAccount().makeDeposit(remainingAmount);
            remainingAmount = 0;
            
            John.getLoanAccount().addInterest();
            John.getCurrentAccount().addInterest();
            
            if (John.getLoanAccount().getDebt() <= 0)
            {
                finishedPay = true;
            }
            //Utils.printText(Float.toString(John.LA.getDebt()), true);
        }
        Utils.printText(John.name + " repaid his loan after " + month + " months. ", false);
        Utils.printText("His current account balance at that time was " + John.getCurrentAccount().getBalance() + "£.", true);
    }
    
    
    public static void Mary()
    {
        BankClient Mary = new BankClient("Mary", 2800, 1400, 350);
        
        Mary.setLoanAccount(18000);
        Mary.setSavingsAccount(200);
        
        boolean finishedPay = false;
        float remainingAmount = 0;
        int month = 0;
        
        while (!finishedPay)
        {
            ++month;
            
            remainingAmount += Mary.monthlyIncome;
            remainingAmount -= Mary.monthlyOutgoings;
            remainingAmount -= Mary.annualLoanPay;
            
            Mary.getLoanAccount().makePayment(Mary.annualLoanPay);
            Mary.getSavingsAccount().makeDeposit(remainingAmount);
            remainingAmount = 0;
            
            Mary.getLoanAccount().addInterest();
            Mary.getSavingsAccount().addInterest();
            
            if (Mary.getLoanAccount().getDebt() <= 0)
            {
                finishedPay = true;
            }
            //Utils.printText(Float.toString(jLA.getDebt()), true);
        }
        
        //Utils.printText(Float.toString(jLA.getDebt()), true);
        Utils.printText(Mary.name + " repaid her loan after " + month + " months. ", false);
        Utils.printText("Her current account balance at that time was " + Mary.getSavingsAccount().getBalance() + "£.", true);
    }
    
    public static void main(String[] args)
    {
        John();
        Mary();
    }
}
