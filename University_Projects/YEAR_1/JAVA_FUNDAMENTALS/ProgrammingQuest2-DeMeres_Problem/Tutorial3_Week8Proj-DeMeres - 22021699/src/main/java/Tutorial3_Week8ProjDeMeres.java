/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */



/**
 *
 * @author Ebenezer Ayo-Meti
 */

class someMath
{
    public void debugPower()
    {
        System.out.println("result of power: " + power(0, 0));
    }
    public void debugRound()
    {
        System.out.println(round(10.234f, 2));
    }
    private double power(double base, int exponent)
    {
        double result = 1d;
        
        if (exponent != 0)
        {
            for (int exp = 0; exp < exponent; ++exp)
            {
                result *= base;
            }   
        }
        else if (base == 0 && exponent == 0)
        {
            System.out.println("You cannot raise zero to the power of zero!");
            return -1;
        }
        
        return result;
    }
    public float round(float number, int decimalPlaces)
    {
        number = Math.round(number * (float)power(10, decimalPlaces)) / (float)(power(10, decimalPlaces));
        
        return number;
    }
}

public class Tutorial3_Week8ProjDeMeres {
    public static void newLine()
    {
        System.out.print("\n");
    }
    public static float task2a()
    {
        Die die = new Die();
        
        long experiments = 100000;
        
        int numberOfThrows = 4; //  per experiment
        
        
        int experiment6sCount = 0;  //  Sums up all the sixes gotten for every experiment
        float probabilitySum = 0;   //  For all experiments
        
        for (int tries = 0; tries < experiments; ++tries)
        {
            int countOfSixes = 0;
            for (int num = 0; num < numberOfThrows; ++num)
            {
                die.roll();

                if (die.outcome == 6)
                {
                    countOfSixes++;
                    experiment6sCount++;
                }
            }
            
            System.out.print("In experiment " + (tries + 1) + " ");
            System.out.println("In " + numberOfThrows + " throws of a single die, the number of sixes gotten were " + countOfSixes);
            float probability = (float)countOfSixes / numberOfThrows;
            probabilitySum += probability;
            System.out.println("The probability of at least one six in four throws is: " + probability);
            newLine();
        }
        
        System.out.print("In " + experiments + " tries of " + numberOfThrows + " throws of a single die");
        System.out.println(" the number of sixes gotten were " + experiment6sCount);
        float probabilityAvg = (float)probabilitySum / experiments;   //    This doesnt work!
        float probabilityGot = (float)experiment6sCount / experiments;
        System.out.println("The probability of at least one six in four throws when all is averaged is: " + probabilityAvg);
        System.out.println("The probability of at least one six in four throws when calculated by number of sixes is: " + probabilityGot);
        
        return probabilityGot;
    }
    
    public static float task2b()
    {
        Die die1 = new Die();
        Die die2 = new Die();
        
        long experiments = 100000;
        
        int numberOfThrows = 24; //  per experiment
        
        
        int experimentDouble6sCount = 0;  //  Sums up all the sixes gotten for every experiment
        
        
        for (int tries = 0; tries < experiments; ++tries)
        {
            int countOfDoubleSixes = 0;
            for (int num = 0; num < numberOfThrows; ++num)
            {
                die1.roll();
                die2.roll();
                        
                if (die1.outcome == 6 && die2.outcome == 6)
                {
                    countOfDoubleSixes++;
                    experimentDouble6sCount++;
                }
            }
            
            System.out.print("In experiment " + (tries + 1) + " ");
            System.out.println("In " + numberOfThrows + " throws of a two die, the number of double sixes gotten were " + countOfDoubleSixes);
            float probability = (float)countOfDoubleSixes / numberOfThrows;
            System.out.println("The probability of at least one six in four throws is: " + probability);
            newLine();
        }
        
        System.out.print("In " + experiments + " tries of " + numberOfThrows + " throws of a single die");
        System.out.println(" the number of sixes gotten were " + experimentDouble6sCount);
        float probabilityGot = (float)experimentDouble6sCount / experiments;
        System.out.println("The probability of at least one six in four throws when calculated by number of sixes is: " + probabilityGot);
        
        return probabilityGot;
    }
    
    public static void main(String[] args) {
        someMath ma = new someMath();
        
        float task2aProbability = task2a();
        newLine();
        float task2bProbability = task2b();
        newLine();
        
        System.out.println("The probability gotten from task2a without rounding is " + task2aProbability +
                " and that of task2b is " + task2bProbability);
        newLine();
        
        System.out.println("The probability gotten from task2a with rounding is " + ma.round(task2bProbability, 2) +
                " and that of task2b is " + ma.round(task2bProbability, 2));
        
    }
    
}
