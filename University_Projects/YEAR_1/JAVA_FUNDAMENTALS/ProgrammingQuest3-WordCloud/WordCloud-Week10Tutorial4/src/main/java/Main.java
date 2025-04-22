/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Ebenezer Ayo-Meti 22021699
 */

import java.io.*;

public class Main {
    private static void debug1()
    {
        String words = "My  Strength  is  God";
        String[] wordsArr1 = words.split(" ");
        //String[] wordsArr1 = words.split(" ");
        for (int i =0; i < wordsArr1.length; ++i)
        {
            System.out.println(wordsArr1[i]);
        }
    }
    private static void debug2()
    {
        String ps = "'\"\\";
        System.out.println(ps);
        //char[] charArr = {'1', '2', ''};
    }
    
    private static void debug3()
    {
        
        String[] fileWords = {"be", "kake", " ", "bread","kake", "bread", "fine"};
        String[] newWords = {"be", "kake", "turt", "bread","kake", " ", "fine", "douse", "bread", "chips"};
        
        newWords = fileWords;
        
        System.out.println("Size of old: " + fileWords.length);
        System.out.println("Size of new: " + newWords.length);
    }
    
    public static void main(String args[]) throws IOException
    {   
        App app = new App();
        app.run();
    }
}
