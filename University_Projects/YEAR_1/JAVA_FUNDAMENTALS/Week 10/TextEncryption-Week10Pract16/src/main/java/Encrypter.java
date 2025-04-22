/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author x7e30
 */

import java.util.Random;

public class Encrypter {
    
    String cipherKey1 = "s5lHjqVV\"9H]lM9oflIHM99l99]lGhH95?X9Hh5MhHh5lHX?fYIHGllI9Hh?He" +
"MPlHoDHh?Hh5lHP5MYYlG4lH?eHPYZ]MhlHP5MG4luHMGIHh?HI?H9?HG?X\\";
    
    static final int defaultSize = 3;
    
    //static int numOfDecipheredText = 0;
    static String[] ogTextStore = new String[defaultSize];
    static int[] encryptedTextID = new int[defaultSize];
    
    public void shuffle(String text)
    {
        Random rGen = new Random();
        
        char[] sequenceAsArray = text.toCharArray();
        
        for (int i = 0; i < sequenceAsArray.length; ++i)
        {
            int randomPosition = rGen.nextInt(sequenceAsArray.length);
            char temp = sequenceAsArray[i];
            sequenceAsArray[i] = sequenceAsArray[randomPosition];
            sequenceAsArray[randomPosition] = temp;
        }
        
        System.out.println(new String(sequenceAsArray));
    }
    
    public String[] allocateSpace(String[] array)
    {
        //  It has to store previous values
        String[] tempStore = new String[array.length];
        
        //  To store previous values
        for (int i = 0; i < array.length; ++i)
        {
            tempStore[i] = array[i];
        }
        
        array = new String[array.length + 3];
        
        //  To put previous values back in array
        for (int i = 0; i < tempStore.length; ++i)
        {
            array[i] = tempStore[i];
        }
        
        return array;
    }
    private int[] allocateSpace(int[] array)
    {
        //  It has to store previous values
        int[] tempStore = new int[array.length];
        
        //  To store previous values
        for (int i = 0; i < array.length; ++i)
        {
            tempStore[i] = array[i];
        }
        
        array = new int[array.length + 3];
        
        //  To put previous values back in array
        for (int i = 0; i < tempStore.length; ++i)
        {
            array[i] = tempStore[i];
        }
        
        return array;
    }
    
    
    private boolean isArrayFull(String[] array)
    {
        boolean full = true;
        
        //  For every element
        for (int i = 0; i <array.length; ++i)
        {
            //  If any of the elements are null, it is not full
            if (array[i] != null)
            {
                full = false;
            }
        }
        
        return full;
    }
    
    private boolean isArrayFull(int[] array)
    {
        boolean full = true;
        
        //  For every element
        for (int i = 0; i <array.length; ++i)
        {
            //  If any of the elements are null, it is not full
            if (array[i] == 0)
            {
                full = false;
            }
        }
        
        return full;
    }
    
    public void addIdToArray(int id)
    {
        //  Checks if aray is full
        if (isArrayFull(encryptedTextID) == true)
        {
            encryptedTextID = allocateSpace(encryptedTextID); //  If yes, allocate space
        }
        //  Then adds ID into the textIDStore
        for (int i = 0; i < encryptedTextID.length; ++i)
        {
            //  If the value at that index is zero
            if (encryptedTextID[i] == 0)
            {
                encryptedTextID[i] = id;    //  assign the ids value
                break;  //  break immediately
            }
        }
    }
    
    public void addTextToArray(String text)
    {
        //  Checks if aray is full
        if (isArrayFull(ogTextStore) == true)
        {
            ogTextStore = allocateSpace(ogTextStore); //  If yes, allocate space
        }
        //  Then adds ID into the textIDStore
        for (int i = 0; i < ogTextStore.length; ++i)
        {
            //  If the value at that index is zero
            if (ogTextStore[i] == null)
            {
                ogTextStore[i] = text;    //  assign the ids value
                break;  //  break immediately
            }
        }
    }
    
    public int getIDIndex(int id)
    {
        //  Loops through whole idStore to match to passed in id
        for (int i = 0; i < encryptedTextID.length; ++i)
        {
            if (id == encryptedTextID[i])
            {
                    return i;   //  If found return index
            }
        }
        
        return -1;  //  If could not find index
    }
    
    public int encryptedTextID(String encryptedText)
    {
        int id = 0;
        for (int i = 0; i < encryptedText.length(); ++i)
        {
            id += encryptedText.charAt(i);
        }
        
        return id;
    }
    
    public String encrypt(String text)
    {
        Random rGen = new Random();
        
        char[] textAsArray = text.toCharArray();
        char[] cipherAsArray = cipherKey1.toCharArray();
        String encryptedText = null;
        
        for (int i = 0; i < textAsArray.length; ++i)
        {
            int randomPosition = rGen.nextInt(cipherAsArray.length);
            //char temp = textAsArray[i];
            textAsArray[i] = cipherAsArray[randomPosition];
            //textAsArray[randomPosition] = temp;
        }
        
        encryptedText = new String(textAsArray);
        
        System.out.println(encryptedText);
        
        addTextToArray(text);
        addIdToArray(encryptedTextID(encryptedText));
        
        return encryptedText;
    }
    
    public String encryptWithKey(String text, String cipherKey)
    {
        Random rGen = new Random();
        
        char[] textAsArray = text.toCharArray();
        char[] cipherAsArray = cipherKey.toCharArray();
        
        String encryptedText = null;
        
        for (int i = 0; i < textAsArray.length; ++i)
        {
            int randomPosition = rGen.nextInt(cipherAsArray.length);
            char temp = textAsArray[i];
            textAsArray[i] = cipherAsArray[randomPosition];
            //textAsArray[randomPosition] = temp;
        }
        
        encryptedText = new String(textAsArray);
        
        System.out.println(encryptedText);
        
        addTextToArray(text);
        addIdToArray(encryptedTextID(encryptedText));
        
        return encryptedText;
    }
    
    
    
    public String decipher(String encryptedText)
    {
        int ogTextIndex = getIDIndex(encryptedTextID(encryptedText));
        
        return ogTextStore[ogTextIndex];
    }

}
