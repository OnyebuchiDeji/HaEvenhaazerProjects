/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author x7e30
 */

class RandBDayGen 
{
    public int generateBDay()
    {
        int num = (int)(Math.floor(Math.random() * 365));
        
        
        return num;
    }
}

class someMath
{
    public void debugPower()
    {
        System.out.println("Power is: " + power(10, 1));
    }
    
    public double power(double mantissa, int exponent)
    {
        double result = 1;
        if (exponent > 0)
        {
            for (int exp = 1; exp <= exponent; ++exp)
            {
                result *= mantissa;
            }
        }
        else
        {
            return 1;
        }
        
        return result;
    }
}


class Task1 {
    static RandBDayGen randGen = new RandBDayGen();
    static someMath mth = new someMath();
    
    public static void debugRandGen()
    {
        for (int i =0; i < 10; i++)
        {
            System.out.println("Random ages btw 1 and 365: " + randGen.generateBDay());
        }
    }
    
    public static int mostOccurringBDay(int[] bDayArray, boolean returnAge)
    {
        int mostOccuringBDay = 0;
        int largestNumberOfOccurences = 0;
        int nextVal = 0;
        int currentVal = 0;
        
        for (int num = 0; num < bDayArray.length; num++)
        {
            currentVal = bDayArray[num];
            
            if (num + 1 <bDayArray.length)
            {
                nextVal = bDayArray[num + 1];
            }
            
            if (currentVal > nextVal && currentVal > largestNumberOfOccurences)   //  Need largest to test
            {
                largestNumberOfOccurences = currentVal;
                
                //  Initialize mostOccurringBDay with index because index represents age
                mostOccuringBDay = num;  
            }
            else if (nextVal > currentVal && nextVal > largestNumberOfOccurences) //  Need largest to test
            {
                largestNumberOfOccurences = nextVal;
                //  Initialize mostOccurringBDay with index because index represents age
                mostOccuringBDay = num + 1;
            }
        }
        
        mostOccuringBDay += 1; //   Because index starts form zero, BDays from 1
        
        int occurencesOfLargest = 0;
        
        
        if (!returnAge)
        {
            System.out.println("The largest occuring BDays are: "); 
            
            //  To check how many times the largest value occurs
            for (int num = 0; num < bDayArray.length; num++)
            {
               if (largestNumberOfOccurences == bDayArray[num] && bDayArray[num] != mostOccuringBDay)
               {
                   //   First, increase number of occurences of largest.
                   occurencesOfLargest += 1;


                   //   Second, store the birthdays that occur the most in an integer
                   //   So if 3, 4, 5 occur most, it will be stored as 345 if starting from 3

                   System.out.println("The BDays: " + (num + 1) + " occurs " + largestNumberOfOccurences + " times!"); 
               }
            }
            System.out.println("The number of occurences of the largest BDays are: " + occurencesOfLargest); 
        }
        
        
        if (occurencesOfLargest == 1)
        {
            if (returnAge)
            {
                return mostOccuringBDay;
            }
            else
            {
                return largestNumberOfOccurences;
            }
        }
        
        return 0;
    }
    
    //  To calculate probability of at least two people sharing same
    //  birhtday in a class of 40
    public static double calcProbability(int[] bDayArray, int totalStudentNum)
    {
        //  The sum of the number of the number of occurences of birthdays that occured
        //  more two or more times
        double sumOfFrequency = 0;
        double probability = 0.0d;
        
        for (int num = 0; num < bDayArray.length; num++)
        {
            if (bDayArray[num] >= 2)
            {
                sumOfFrequency+=bDayArray[num];
            }
        }
        
        probability = (double)(sumOfFrequency / totalStudentNum);
        
        return probability;
    }
    
    
    public static void task1()
    {
        int numOfClasses = 10000;
        int[] studentsPerClass = new int[40];
        
        //int totalStudentNum = numOfClasses * studentsPerClass.length;
        
        
        double probabilitySum = 0.0d;
    
        for (int classNum = 0; classNum < numOfClasses; ++classNum) //  For 100000 classes
        {
            //  For all 365 days of the year representing a birthday
            //  For each class, the bDayOccurences will be reset
            int[] bDayOccurrences = new int[365];   //0-364 represents 1 - 365
            
            for (int studentNum = 0; studentNum < studentsPerClass.length; ++studentNum)    //  For each student in the class...
            {
                // Generate random birthday
                studentsPerClass[studentNum] = randGen.generateBDay();   
                
                //  Use the age value of each student in studentsPerClass as the index for bDayOccurences
                //  And then increase the value at that index by one for that age value to count its occurences
                bDayOccurrences[studentsPerClass[studentNum]]++;
                //  Then loop
            }
            
            //  When finished loop
            System.out.println("For class " + (classNum + 1));
            
            
            //  To print the age occurences
            for (int num = 0; num < bDayOccurrences.length; ++num)
            {
                System.out.println("Birthday " + (num + 1) + " occurs " + bDayOccurrences[num] + " times.");
            }
            
            
            //  Print out which occurs most and how many times for that class
            int mostOccurringBDay = mostOccurringBDay(bDayOccurrences, true);
            int numberOfOccurences = mostOccurringBDay(bDayOccurrences, false);
            if (mostOccurringBDay != 0)
            {
                System.out.println("Birthday " + mostOccurringBDay + " occurs the most! " + numberOfOccurences + " times!"); 
            }
            
            //  Get probability and store it in probabilitySum because it will be averaged. It will be summed
            //  The probability is for the number of age occurences for that class
            //  The avergae gives the true probability indicating the probability that, in a class of...
            //  Two or more people can have the same age
            double probability = calcProbability(bDayOccurrences, 40);
            probabilitySum += probability;
            System.out.print("The probability of at least two people sharing the same");
            System.out.println( " birthday for class " + (classNum + 1)  + " of " + studentsPerClass.length + " students is " + probability);
            
        }
        
        double averageProbability = probabilitySum / numOfClasses;  //  because I added the probability for every class
        System.out.print("The probability of at least two people sharing the same ");
        System.out.println(" birthday in a class of " + studentsPerClass.length + " is " + averageProbability);
        
    }
}

public class Tasks {
    public static void main(String args[])
    {
//        Task1 tsk1 = new Task1();
//        Task1.debugrandGen();
        Task1.task1();
//        someMath mth = new someMath();
//        mth.debugPower();
    }
}
