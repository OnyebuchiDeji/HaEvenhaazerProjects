/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Ebenezer Ayo-Meti - 22021699 - x7e30
 */
public class gameRulesApp
{
    static String[] dictionary;
    
    gameRulesApp(String fileName)
    {
        dictionary = new Dictionary().readFile(fileName);
    }
    
     //  Checks if word only has alphabets
    public boolean isWordPure(String word)
    {
        boolean pure = true;
        String numbers = "0123456789 -:<>?\\;,./'\"+=_!@#$%^&*(){}[]~`";

        if (word.contains(numbers))
        {
            pure = false;
        }
        
        return pure;
    }
    
    public boolean isWordEmpty(String word)
    {
        boolean empty = false;
        
        if ((word.equals("")|| word.equals(" ") || word.length() == 0))
        {
            empty = true;
        }
        
        return empty;
    }
    
    public boolean exists(String word)
    {
        boolean exists = false;
        for (int i = 0; i < dictionary.length; ++i)
        {
            if (word.equals(dictionary[i]))
            {
                exists = true;
            }
        }
        
        return exists;
    }
    
    /*
        Returns a word's index if present
        Else will return -1
    */
    private int getMostRecentWordIndex(String[] wordsArray)
    {
        //  Check for most recent word entered before this current one, nextWord
        //  So check index of latest word
        int index = -1;
        
        for (int i = 0; i < wordsArray.length; ++i)
        {
            if (wordsArray[i] != null)
            {
                index = i;
            }
            else
            {
                break;  //  Immediately a null value is encountered
            }
        }
        
        return index;
    }
            
    public boolean checkNextWordCharacter(String nextWord, String[] enteredWords)
    {
        boolean valid = false;
        
        //  Because if the first word is null, then nothing has been entered
        if (enteredWords[0] == null)
        {
            //  So the entered word does not need to be checked...
            //  It is valid
            valid = true;   
        }
        else
        {
            String previousWord = enteredWords[getMostRecentWordIndex(enteredWords)];

            if (previousWord.charAt(previousWord.length()-1) == nextWord.charAt(0))
            {
                valid = true;
            }
        }
        
        return valid;
    }
    
    public boolean repeated(String word, String[] enteredWords)
    {
        boolean repeats = false;
        
        //  If first value is null, then array is empty
        //  So no need to loop through
        if (enteredWords[0] != null)
        {
            for (int i = 0; i < enteredWords.length; ++i)
            {
                //  If any is found repeated...
                if (word.equals(enteredWords[i]))
                {
                    repeats = true;
                    break;
                }
                //  If any word after the first is null, break
                else if (enteredWords[i] == null)
                {
                    break;
                }
                else
                {
                    //  When neither equal nor null, it is valid.
                    repeats = false;

                }
            }
        }
        
        return repeats;
    }
    
//    public static void main(String[] args)
//    {
//        gameRulesApp gRA = new gameRulesApp();
//        
//        System.out.println(gRA.isWordPure("ses"));
//    }
}
