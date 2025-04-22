

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Ebenezer Ayo-Meti - 22021699 - x7e30
 */
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Dictionary
{
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
        String[] tempStringArray = fileString.split("\n");
        
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
        //  to get processed String as array...
        //  then returns it
        return processStringToArray(new String(charBuffer));
    }
}
