/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author x7e30
 */
public class Pract6Tasks {
    public static void main(String args[])
    {
       // Task2a prct6Tsk = new Task2a("myTaskFile.txt");
        
        //prct6Tsk.createMyFile();
        //prct6Tsk
        
        Task2a file2 = new Task2a("myfile2.txt");
        file2.createMyFile();
        file2.clearFile();
        file2.appendText("God is Salvation!");
        file2.appendText("The Lord is clothed with honour and majesty!");
        file2.appendText("The Lord is very great!");
        file2.appendText("The LORD God is amazing!");
        file2.appendText("Jesus is exalted!");
        file2.appendText("Blessed be the God and Father of The Lord Jesus Christ my King!");
        
        file2.dispayAllWords();

        
    }
    
}
