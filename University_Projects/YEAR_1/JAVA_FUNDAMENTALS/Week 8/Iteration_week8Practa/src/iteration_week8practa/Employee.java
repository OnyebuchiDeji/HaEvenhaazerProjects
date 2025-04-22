package iteration_week8practa;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author x7e30
 */
public class Employee {
    String name = null;
    
    char currency = '£';
    int currentAmountInSavings = 0;
    
    int startingAge = 0;
    int currentAge = 0;
    //int startingYear = 0;
    //int currentYear = 0;
    
    
    final int retirementAge = 65;
    
    int annualStartingSalary = 26000;
    int annualSalaryIncrease = 300;
    
    int monthlyMortgagePay = 900;
    int numberOfPayments = 480;
    int totalMortgageCost = 432000;
    
    int totalExpenses = 0;
    
    // prefixes s == starting and c == current
    Employee(String name, int sAge)//, int cAge, int cYear, int sYear)
    {
        this.name = name;
        this.startingAge = sAge;
        //this.currentAge = cAge;
        //this.startingYear = sYear;
        //this.currentYear = cYear;
    }
    
    public int whenFullPaudMortgage()
    {
        return (numberOfPayments/12);
    }
    
    /*
    public int getTotalExpensesAfter();
    {
        
    }
    
    public void interestSavingsAmount
    {
        
    }
*/
}
