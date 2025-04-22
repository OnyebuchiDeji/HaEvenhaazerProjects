package iteration_week8practa;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author x7e30
 */
public class MoneyArithmetic {
    private double powerOf(double base, int exponent)
    {
        double result = base;
                
        for (int i = 1; i != exponent; ++i)
        {
            result *= base;
        }
        
        return result;
    }
    
    public double roundOff(double num, int decimalPlace)  //  to two dp
    {
        num = Math.round(num*powerOf(10, decimalPlace)) / (powerOf(10, decimalPlace));
        
        return num;
    }
    
    public double calcTax(double amount)
    {
        double tax = 0;
        if (amount > 35000)
        {
            tax = 35000 * 0.2 + (amount - 35000) * 0.4;
        }
        return tax;
    }
}
