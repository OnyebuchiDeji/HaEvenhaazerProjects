
import java.io.*;


/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author x7e30
 */
public class Task1 {
    //methods are public by default
    static void doTask1() throws IOException //  I made tgis static
    {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
        
        System.out.print("Enter some words: ");

        String words = br.readLine();

        System.out.println(words.length());
        System.out.println(words.toUpperCase());
        System.out.println(words.toLowerCase());
        System.out.println(words.charAt(2));
        System.out.println(words.charAt(words.length() - 1));
    }
}
