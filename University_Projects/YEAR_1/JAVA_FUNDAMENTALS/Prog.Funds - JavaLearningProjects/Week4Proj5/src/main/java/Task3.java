/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author x7e30
 */

import java.io.*;

public class Task3 {
    public int readNum() throws IOException //  not static
    {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
        
        System.out.println("Enter a number: ");
        String stringNum = br.readLine();
        int number = Integer.parseInt(stringNum);
        
        return number;
    }
}
