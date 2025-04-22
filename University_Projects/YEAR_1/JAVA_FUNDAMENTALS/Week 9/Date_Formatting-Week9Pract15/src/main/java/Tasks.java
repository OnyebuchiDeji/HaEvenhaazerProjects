/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author x7e30
 */

import java.util.Date;


public class Tasks {
    
    public void newLine()
    {
        System.out.print("\n");
    }
    
    /*  Task 1  */
    //  Task1 returns the date tieme information which they all use
    public String dateStringTask1()
    {
        //  To test the Date class
        
        Date timeNow = new Date();
        String timeNowAsString = timeNow.toString();
        
        System.out.println(timeNowAsString);
        
        return timeNowAsString;
    }
    
    /*  For Task 2  */
    
    static String getDayString(String dateString)
    {
        String theString = dateString.substring(0, 3);

        switch(theString) 
         {
            case "Mon":
                return "Monday";
            case "Tue":
                return "Tuesday";
            case "Wed":
                return "Wednesday";
            case "Thu":
                return "Thursday";
            case "Fri":
                return "Friday";
            case "Sat":
                return "Saturday";
            case "Sun":
                return "Sunday";
            default:
                return "Invalid day";
        }
    }
    
    static String getMonthString(String dateString)
    {
        String theString = dateString.substring(4, 7);

        switch(theString) 
         {
            case "Jan":
                return "January";
            case "Feb":
                return "February";
            case "Mar":
                return "March";
            case "Apr":
                return "April";
            case "May":
                return "May";
            case "Jun":
                return "June";
            case "July":
                return "July";
            case "Aug":
                return "August";
            case "Sep":
                 return "September";
            case "Oct":
                 return "October";
            case "Nov":
                 return "November";
            case "Dec":
                 return "December";
            default:
                return "Invalid month";
        }
    }
   
    static int getDayInt(String dateString)
    {
        String theString = dateString.substring(8, 10);
        int stringAsNumber = Integer.parseInt(theString);
        
        return stringAsNumber;
    }
    
    public String dateSign(String dateString)
    {
        String theString = dateString.substring(8, 10);
        int lastDigitIndex = theString.length() - 1;
        
        switch (theString.charAt(lastDigitIndex))
        {
            case '1':
                return "st";
            case '2':
                return "nd";
            case '3':
                return "rd";
            default:
                return "th";
        }
    }

    static int[] getTimeComponents(String dateString)
    {
        String theTimeString = dateString.substring(11, 19);
        
        String[] theTimeStringAsArray = theTimeString.split(":");
        
        int[] timeComponents = new int[3];
        
        //  To convert the string array of the time components into int array
        //  By converting each value
        for (int index = 0; index < timeComponents.length; ++index)
        {
            timeComponents[index] = Integer.parseInt(theTimeStringAsArray[index]);
        }
        
        //  Printing out time components
        for (int index = 0; index < timeComponents.length; ++index)
        {
            System.out.println("Time components: " + timeComponents[index]);
        }
        
        //  returns the array
        return timeComponents;
    }

     static int getYear(String dateString)
    {
        String theString = dateString.substring(24, 28);
        
        System.out.println("The year: " + theString);
                
        return Integer.parseInt(theString);
    }
    
 
    public void task2()
    {
        System.out.println("Task 2. Day is " + getDayString(dateStringTask1()));
        
        newLine();
        
        System.out.println("Task 2. Month is " + getMonthString(dateStringTask1()));
        
        newLine();
        
        System.out.println("Task 2. Date is " + getDayInt(dateStringTask1()));
        
        newLine();
        
        getTimeComponents(dateStringTask1());
        
        newLine();
        
        getYear(dateStringTask1());
    }
    
    /*  For Task3   */

    public String formalDateString(String dateString)
    {
        //  Task1 returns the date tieme information which they all use
        
        String formalDate = getDayString(dateString) + ", " + getMonthString(dateString) + " " +
                getDayInt(dateString) + dateSign(dateString) + ", " + getYear(dateString);
        
        return formalDate;
    }
    
    public void task3()
    {
        System.out.println("The formal date: " + formalDateString(dateStringTask1()));
    }
    
    
    /*  Task 4   */
    
    public void task4()
    {
        //  365 days per year * 24 hrs per day * 60 minutes per hour * 60 seconds per minute
        //  ... * 1000 because of it is in milliseconds
        int yearFrom1970 = 1;
        long timeToNextYear = yearFrom1970 * 365 * 24 * 60 * 60 * 1000;
        
        int dayFromJan1 = 1;
        long timeToNextDay = dayFromJan1 * 24 * 60 * 60 * 1000;
        
        //  Takes in the time form January 1, 1970, 00:00:00 GMT;
        Date timeNow = new Date(timeToNextYear);
        
        String timeNowAsString = timeNow.toString();
        
        System.out.println(timeNowAsString);
        
        
    }
}
                                                                                              