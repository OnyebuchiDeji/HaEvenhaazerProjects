/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Ebenezer Ayo-Meti 22021699
 */

import java.io.*;

public class App {
    /*
        When arrays are passed in, they are passed by reference, meaning the memory address of...
        that array is passed, not a copy of it.
        So the method can change the original array's values.
    */
    
    //  Default constructor
    App()
    {
    }
    
    /*
        This is to remove all newlines and whitespaces and empty literals...
        to make an array of just pure strings.
    */
    private String[] removeEmptyLiteral(String[] fileWordsArray)
    {
        int size = 0;
        String[] tempArray;
        
        //  To determine size of array when there is no empty literal character or space
        for (int i = 0; i < fileWordsArray.length; ++i)
        {
            if (!(fileWordsArray[i].equals("")) && !(fileWordsArray[i].equals(" ")))
            {
                ++size;
            }
        }
        
        tempArray = new String[size];   //  Initialized with gotten size
        
        //  To make temporary array that has no space or empty literal characteter with the size gotten
        for (int i = 0, j = 0; i < fileWordsArray.length; ++i)
        {
            if (!(fileWordsArray[i].equals("")) && !(fileWordsArray[i].equals(" ")))
            {
                tempArray[j++] = fileWordsArray[i]; //  j++ not ++j
            }
        }
        
        //  When you assign a new value to the whole array, it no more accesses the memory address
        //  of that array.
        //fileWordsArray = tempArray;
        
        //  So I have to return
        return tempArray;
    }
    
    /*
        This processes the String to give a pure array of just strings. But punctuation is not removed here.
    */
    private String[] processStringToArray(String fileString)
    {
        fileString = fileString.trim(); //  First trim;
        
        //  Initialize the array with string using .split()...
        //  to split at line spaces into individual words
        String[] tempStringArray = fileString.split(" ");
        
        //  Then trim each word in array.
        for (int index = 0; index < tempStringArray.length; ++index)
        {
            tempStringArray[index] = tempStringArray[index].trim();
        }
        
        //  Remove all spaces or empty literal characters
        tempStringArray = removeEmptyLiteral(tempStringArray);
        
        return tempStringArray;   //  Return processed string as array.
    }
    
    public String[] readFile(String fileName)
    {
        int bufferLength = (int)(new File(fileName).length());  //  Would normally return a long so I cast it.
        char[] charBuffer = new char[bufferLength]; //  Make a character array able to hold all file's word's characters
        try
        {
            BufferedReader br = new BufferedReader(new FileReader(fileName));
            br.read(charBuffer, 0, bufferLength);   //  Read from file into charBuffer
            br.close();
        }
        catch (IOException ioExcp)
        {
            System.out.println("There was an error reading file! Error: " + ioExcp.toString());
        }
        
        //  Make a new string from characters and pass into function...
        //  to get processed String as array
        String[] fileWordsArray = processStringToArray(new String(charBuffer));
        
        return fileWordsArray;
    }
    
    public void displayAllWords(String[] fileWordsArray, int start, int stop)
    {   
        if (stop > fileWordsArray.length)
        {
            System.out.println("Cannot have index greater than length!");
            stop = fileWordsArray.length;
        }
        for (int i = start; i < stop; ++i)
        {
            System.out.println("index " + i + " " + fileWordsArray[i]);
        }
    }
    
    //  Passes in array by reference so doesn't copy. Because I do not assign a new value to it.
    public void removePunctuation(String[] fileWordsArray) 
    {
        String punctuations = ";{}()[]!~`|#$\"%^&*-_+=\\,.:'";  //  All possible punctuation
        char[] punctuationsAsChar = punctuations.toCharArray();
        
        for (int index = 0; index < fileWordsArray.length; ++index) //  For all words in the array...
        {
            //  Look for index of any punctuation in the word
            for (int charIndex = 0; charIndex < punctuationsAsChar.length; ++charIndex)
            {
                int punctuationIndex = fileWordsArray[index].indexOf(punctuationsAsChar[charIndex]);
                
                if ( punctuationIndex != -1)    //  If there is a punctuatiom...
                {
                    //  Get a substring of all words until that punctuation; use it to change the value of the word.
                    fileWordsArray[index] = fileWordsArray[index].substring(0, punctuationIndex); 
                }
            }
        }
    }
    
    //  Passes in array by reference so doesn't copy. Because I do not assign to it a new value
    public void changeCase(String[] fileWordsArray, boolean upper)
    {
        if (upper)
        {
            for (int index = 0; index < fileWordsArray.length; ++index)
            {
                fileWordsArray[index] = fileWordsArray[index].toUpperCase();
            }
        }
        else
        {
            for (int index = 0; index < fileWordsArray.length; ++index)
            {
                fileWordsArray[index] = fileWordsArray[index].toLowerCase();
            }
        }
    }
    
    
    //  Checks if the word is in the array of words
    //  It returns the index of that word if it is in that array
    //  Else it returns -1
    private int wordIndexInArray(String[] wordsArray, String word)
    {
        //  It starts checking from the array the word is in
        for (int index = 0; index < wordsArray.length; ++index) //  Loopes through array
        {
            if (wordsArray[index] != null)
            {
                if (wordsArray[index].equals(word))
                {
                    return index;   //  Return index of word if in the wordsArray
                }
            }
            else
            {
                return -1;   // If encounter null, return -1
            }
        }
        
        return -1;  //  The same: if no word is identical to word, return -1
    }
    
    //  Word dictionary contains all words and the number of times they occur
    
    /*  //  OLD SOLUTION
    
    public Dictionary makeWordDictionary(String[] fileWordsArray)
    {
        
        int tempDictionarySize = fileWordsArray.length;
        String[] tempWordDictionary = new String[tempDictionarySize];
        int[] tempOccurrences = new int[tempDictionarySize];
        
        int wordCount = 0; //   It counts the number of words so that I can make new array
        int delta = 0;
        
        for (int index = 0; index < fileWordsArray.length; ++index)
        {
            int dictIndex = index - delta;
            int wordIndexInDict = wordIndexInArray(tempWordDictionary, fileWordsArray[index]);
            
            if (wordIndexInDict == -1)
            {
                tempWordDictionary[dictIndex] = fileWordsArray[index];
                ++tempOccurrences[dictIndex];
                ++wordCount;
            }
            else
            {
                ++tempOccurrences[wordIndexInDict];
                ++delta;
            }
            
        }
        
        Dictionary myDictionary = new Dictionary(wordCount, wordCount);
        
        /*  This loop is to initialize my new arrays with the values of the old...
            because they are the right size 
        */
    /*
        for (int index = 0; index < wordCount; index++)
        {
            myDictionary.setWordArrayVal(tempWordDictionary[index], index);
            myDictionary.setOccurrenceVal(tempOccurrences[index], index);
        }
        return myDictionary;
    }
    */
    
    //  SECOND SOLUTION
    public Dictionary makeWordDictionary(String[] fileWordsArray)
    {
        int dictSize = 0;   //  Size of the temporary arrays
        String[] tempWordDict;
        int[] tempOccurrences;
        
        boolean repeats = false;
        
        /*
            This is to count the number of unique words in the array to determine size of the  temporary arrays
        */
        //  For every word in the array
        for (int i = 0; i < fileWordsArray.length; ++i)
        {
            repeats = false;
            if (i == 0) //  Always count first word because it does not have any word before it.
            {
                ++dictSize;
            }
            else    //  Can only do this when i is not zero
            {   
                //  This checks all the values before the current word with index i to see if it is repeated
                for (int j = i - 1; j >= 0; --j)    //  j identifies those previous words, so it starts from the index before (j = i - 1)
                {
                    if (fileWordsArray[i].equals(fileWordsArray[j]))
                    {
                        repeats = true; //  If it repeats...
                        break;  //  exit loop immediately a repeat is found for next iteration of i
                    }
                    else    //  If not...
                    {
                        //  since not all the figures before will be equal...
                        //  keep searching until end or until a repeat is found
                        repeats = false;
                    }
                }
                if (repeats == false)   //  If no repeat is found for that word at i
                {
                    ++dictSize;
                }
            }
        }
        
        //System.out.println(dictSize);
        
        tempWordDict = new String[dictSize];    //  My temp array
        tempOccurrences = new int[dictSize];
        
        for (int i = 0, j = 0; i < fileWordsArray.length; ++i)
        {
            //  Checks if the word already is in the array, and returns its index in that array.
            int indexInArray = wordIndexInArray(tempWordDict, fileWordsArray[i]);
            if (indexInArray != -1) //  If it is in array...
            {
                //  I use its index in the occurrence array to count it.
                ++tempOccurrences[indexInArray];    //  Just increase its occurrence count...
            }
            else    //  If not in array...
            {
                tempWordDict[j] = fileWordsArray[i];  //  Add it to array.
                ++tempOccurrences[j];                 //  increase its occurrence
                ++j;                                  //    Increase j     
            }
        }
        
        Dictionary myDictionary = new Dictionary(dictSize, dictSize);
        
        myDictionary.setWordArrayVal(tempWordDict);
        myDictionary.setOccurrenceVal(tempOccurrences);

        return myDictionary;
    }
    
    public void run()
    {
        String[] fileWords = readFile("WordCloudWords.txt");
        System.out.println("Total number of words in text: " + fileWords.length);
        
        removePunctuation(fileWords);
        changeCase(fileWords, true);
        //displayAllWords(fileWords, 0, fileWords.length);
        
        Dictionary myBook = makeWordDictionary(fileWords);
        
        myBook.displayWordsOccurences(">=", 7);
        
        //myBook.displayWordsOccurencesRange(7, 15);
        
        System.out.println("Total number of words in dictionary: " + myBook.sizeOfDictionary());
        
        TextDisplayApp.wordCloud(myBook.getWordArray(), myBook.getOccurrenceArray());
        
    }
}
