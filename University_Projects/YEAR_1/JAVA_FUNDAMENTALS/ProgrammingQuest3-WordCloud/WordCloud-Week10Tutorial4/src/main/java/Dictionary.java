/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Ebenezer Ayo-Meti 22021699
 */

//  Each file can only have one public class
//  Any other class will be private

public class Dictionary    //  Classes are implicitely private to file so I need to declare as public
{
    private String[] wordsArray;
    private int[] occurrenceCount;

    Dictionary()
    {
        System.out.println("Dictionary created!");
    }
    
    public int sizeOfDictionary()
    {
        return wordsArray.length;
    }
    
    Dictionary(int strArrSize, int intArrSize)
    {
        this.wordsArray = new String[strArrSize];
        this.occurrenceCount = new int[intArrSize];
    }
    
    //  Changes the value of the owrd at a certain index
    public void setWordArrayVal(String word, int index)
    {
        this.wordsArray[index] = word;
    }
    
    //  Changes the value of the occurence at a specific index
    public void setOccurrenceVal(int num, int index)
    {
        this.occurrenceCount[index] = num;
    }
    
    //  Initializes the wordArray with a new array
    public void setWordArrayVal(String[] wordArray)
    {
        this.wordsArray = wordArray;
    }
    
    //  Initializes the occurence array with a new array
    public void setOccurrenceVal(int[] intArray)
    {
        this.occurrenceCount = intArray;
    }

    public String getWord(int atIndex)
    {
        return wordsArray[atIndex];
    }

    public int getOccurrenceVal(int atIndex)
    {
        return occurrenceCount[atIndex];
    }
    
    public String[] getWordArray()
    {
        return wordsArray;
    }

    public int[] getOccurrenceArray()
    {
        return occurrenceCount;
    }

    public void displayWordsOccurences()
    {
        for (int index = 0; index < wordsArray.length; ++index)
        {
            System.out.println(wordsArray[index] + " : " + occurrenceCount[index]);
        }
    }
    
    public void displayWordsOccurences(String conditionSign, int occurence)
    {
        System.out.println("Words with occurences " + conditionSign + " " + occurence + ": ");
        switch(conditionSign)
        {
            case ">" -> 
            {
                for (int index = 0; index < wordsArray.length; ++index)
                {
                    if (occurrenceCount[index] > occurence)
                    {
                        System.out.println(wordsArray[index] + " : " + occurrenceCount[index]);
                    }
                }
            }
            case "<" ->
            {
                for (int index = 0; index < wordsArray.length; ++index)
                {
                    if (occurrenceCount[index] < occurence)
                    {
                        System.out.println(wordsArray[index] + " : " + occurrenceCount[index]);
                    }
                }
            }
            case "<=" ->
            {
                for (int index = 0; index < wordsArray.length; ++index)
                {
                    if (occurrenceCount[index] <= occurence)
                    {
                        System.out.println(wordsArray[index] + " : " + occurrenceCount[index]);
                    }
                }
            }
            case ">=" ->
            {
                for (int index = 0; index < wordsArray.length; ++index)
                {
                    if (occurrenceCount[index] >= occurence)
                    {
                        System.out.println(wordsArray[index] + " : " + occurrenceCount[index]);
                    }
                }
            }
            case "==" ->
            {
                for (int index = 0; index < wordsArray.length; ++index)
                {
                    if (occurrenceCount[index] == occurence)
                    {
                        System.out.println(wordsArray[index] + " : " + occurrenceCount[index]);
                    }
                }
            }
        }
        
    }
    
    public void displayWordsOccurencesRange(int lowest, int highest)
    {
        System.out.println("Words with occurences between " + lowest + " and " + highest + ": ");
        for (int index = 0; index < wordsArray.length; ++index)
                {
                    if ((occurrenceCount[index] >= lowest) && (occurrenceCount[index] <= highest))
                    {
                        System.out.println(wordsArray[index] + " : " + occurrenceCount[index]);
                    }
                }
    }
}
