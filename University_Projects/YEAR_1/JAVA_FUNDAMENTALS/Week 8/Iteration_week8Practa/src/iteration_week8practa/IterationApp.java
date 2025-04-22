package iteration_week8practa;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author x7e30
 */
public class IterationApp {
    static MoneyArithmetic ma = new MoneyArithmetic();
    
    
    private static void newLine()
    {
        System.out.print("\n");
    }
    
    private static void debug(int year, int month, double amount, String extraInfo)
    {
        System.out.println("In year " + year + ", month " + month + ", amount is: " + ma.roundOff(amount, 2) + ", " + extraInfo + '.');
    }
    
    private static void Task1()
    {
        //Employee bob = new Employee("Bob", 22);
        
        //  Task: Display his financial position, the amount of money he has saved and when...
        //  he finishes paying his debt by mortgage
        String name = "Bob";
        int retirementAge = 65;
        int startingAge = 22;
        int yearsTillRetirement = retirementAge - startingAge;
        
        int annualStartingSalary = 26000;
        int annualSalaryIncrease = 300;
        
        int monthlyMortgage = 900;
        int whenFinishedDebt = 480; //  Times before debt is fully paid
        int totalMortgageCost = monthlyMortgage * whenFinishedDebt;
        int yearsBeforeFinishedDebt = whenFinishedDebt/12; // It takes 40 years for him to pay all his debts
        
        int annualTotalExpensesXDebt = 750;
        
        int depositInterestRate = 0;
        
        int currentSavingsAmount = 0;
        int currentAmount = 0;
        
        for (int yr = 1; yr <= yearsTillRetirement; yr++)
        {
            currentAmount += annualStartingSalary;
            System.out.println("current amount is " + currentAmount);
            
            //System.out.println("current amount after annual increase is " + currentAmount);
            
            for (int month = 1; month <= 12; ++month)
            {
                if ((startingAge + yr) <= 62)
                {
                    currentAmount -= monthlyMortgage;
                    debug(yr, month, currentAmount, "after mortgage pay");
                }
                
                currentAmount -= annualTotalExpensesXDebt;
                debug(yr, month, currentAmount, "after expenses");
            }
            
            annualStartingSalary += annualSalaryIncrease;  //  Increases at end of each year
            
        }
        
        currentSavingsAmount = currentAmount;
        System.out.print(name + " will have repaid his mortgage in his " + (startingAge + yearsBeforeFinishedDebt) + "nd year of age." );
        System.out.println(" At the end of his 64th year of age (when he retires) he will have " + currentSavingsAmount + " in his savings account.");
        
    }
    
    public static void Task2()
    {
        //Employee bob = new Employee("Bob", 22);
        
        //  Task: Display his financial position, the amount of money he has saved and when...
        //  he finishes paying his debt by mortgage
        
        String name = "Bob";
        int retirementAge = 65;
        int startingAge = 22;
        int yearsTillRetirement = retirementAge - startingAge;
        
        double annualStartingSalary = 26000d;
        double annualSalaryIncrease = 300d; //  this keeps track of the real salary
        double actualSalaryIncome = 0d; //  This is the salary gained; it can be affected by tax
        
        double monthlyMortgage = 900d;
        int whenFinishedDebt = 480; //  Times before debt is fully paid
        double totalMortgageCost = monthlyMortgage * whenFinishedDebt;
        int yearsBeforeFinishedDebt = whenFinishedDebt/12; // It takes 40 years for him to pay all his debts
        
        double annualTotalExpenseXDebt = 750d;
        
        int depositInterestRate = 0;
        
        double currentSavingsAmount = 0;
        double currentAmount = 0;
        
        double tax = 0;
        
        for (int yr = 1; yr <= yearsTillRetirement; yr++)
        {
            newLine();
            
            debug(yr, 1, annualStartingSalary, "annual salary before applying tax");
            debug(yr, 1, actualSalaryIncome, "actual income salary before applying tax");
            
            if (annualStartingSalary > 35000)
            {
                tax = (35000d*0.2) + ((annualStartingSalary - 35000d) * 0.4);
                debug(yr, 1, tax, "the tax");
                actualSalaryIncome = annualStartingSalary;
                actualSalaryIncome -= tax;
            }
            /*
            if (annualStartingSalary > 35000)
            {
                tax = 35000d*0.2 + (annualStartingSalary - 35000d) * 0.4;
                debug(yr, 1, tax, "the tax");
                annualStartingSalary -= tax;
                actualSalaryIncome = annualStartingSalary;
            }
            */
            else
            {
                actualSalaryIncome = annualStartingSalary -(annualStartingSalary * 0.2);
            }
            
            debug(yr, 1, annualStartingSalary, "annual salary before applying tax");
            debug(yr, 1, actualSalaryIncome, "actual income salary before applying tax");
            
            //newLine();
            
            currentAmount += actualSalaryIncome;
            
            System.out.println("current amount is " + currentAmount);
            
            //System.out.println("current amount after annual increase is " + currentAmount);
            
            for (int month = 1; month <= 12; ++month)
            {
                if (totalMortgageCost > 0)
                {
                    currentAmount -= monthlyMortgage;
                    totalMortgageCost -= monthlyMortgage;
                    debug(yr, month, currentAmount, "after mortgage pay");
                }
                
                currentAmount -= annualTotalExpenseXDebt;
                
                debug(yr, month, currentAmount, "after expenses");
            } 
            
            annualStartingSalary += annualSalaryIncrease;  //  Increases at end of each year
            
        }
        
        newLine();
        currentSavingsAmount = currentAmount;
        System.out.print(name + " will have repaid his mortgage in his " + (startingAge + yearsBeforeFinishedDebt) + "nd year of age." );
        System.out.println(" At the end of his 64th year of age (when he retires) he will have " + currentSavingsAmount + " in his savings account.");
        
    }
    public static void Task3()
    {
        //Employee bob = new Employee("Bob", 22);
        
        //  Task: Display his financial position, the amount of money he has saved and when...
        //  he finishes paying his debt by mortgage
        
        String name = "Bob";
        int retirementAge = 65;
        int startingAge = 22;
        int yearsTillRetirement = retirementAge - startingAge;
        
        double annualStartingSalary = 26000d;
        double annualSalaryIncrease = 300d; //  this keeps track of the real salary
        double actualSalaryIncome = 0d; //  This is the salary gained; it can be affected by tax
        
        double monthlyMortgage = 900d;
        int whenFinishedDebt = 480; //  Times before debt is fully paid
        double totalMortgageCost = monthlyMortgage * whenFinishedDebt;
        int yearsBeforeFinishedDebt = whenFinishedDebt/12; // It takes 40 years for him to pay all his debts
        
        double annualTotalExpenseXDebt = 750d;
        
        int depositInterestRate = 0;
        
        double currentSavingsAmount = 0;
        double currentAmount = 0d;
        
        double tax = 0;
        
        for (int yr = 1; yr <= yearsTillRetirement; yr++)
        {
            newLine();
            
            debug(yr, 1, annualStartingSalary, "annual salary before applying tax");
            debug(yr, 1, actualSalaryIncome, "actual income salary before applying tax");
            
            if (annualStartingSalary > 35000)
            {
                tax = (35000d*0.2) + ((annualStartingSalary - 35000d) * 0.4);
                debug(yr, 1, tax, "the tax");
                actualSalaryIncome = annualStartingSalary;
                actualSalaryIncome -= tax;
            }
            else
            {
                actualSalaryIncome = (annualStartingSalary -(annualStartingSalary * 0.2));
            }
            
            debug(yr, 1, annualStartingSalary, "annual salary before applying tax");
            debug(yr, 1, actualSalaryIncome, "actual income salary before applying tax");
            
            //newLine();
            
            currentAmount += actualSalaryIncome;
            
            System.out.println("current amount is " + currentAmount);
            
            //System.out.println("current amount after annual increase is " + currentAmount);
            
            for (int month = 1; month <= 12; ++month)
            {
                if (totalMortgageCost > 0)
                {
                    currentAmount -= monthlyMortgage;
                    totalMortgageCost -= monthlyMortgage;
                    debug(yr, month, currentAmount, "after mortgage pay");
                }
                
                currentAmount -= annualTotalExpenseXDebt;
                currentAmount -= (currentAmount * 0.02d);
                
                debug(yr, month, currentAmount, "after expenses");
            } 
            
            annualStartingSalary += annualSalaryIncrease;  //  Increases at end of each year
            
        }
        
        newLine();
        currentSavingsAmount = currentAmount;
        System.out.print(name + " will have repaid his mortgage in his " + (startingAge + yearsBeforeFinishedDebt) + "nd year of age." );
        System.out.println(" At the end of his 64th year of age (when he retires) he will have " + currentSavingsAmount + " in his savings account.");
        
    }
    
    
    public static void main(String args[])
    {
        //Task1();
        //Task2();
        Task3();
    }
    
}
