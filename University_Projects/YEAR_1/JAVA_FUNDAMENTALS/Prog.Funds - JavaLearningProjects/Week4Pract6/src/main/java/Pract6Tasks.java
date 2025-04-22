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
        file2.appendText("sddf");
        file2.appendText("YO! YO! YO! IT'S EBEN!");
        
        file2.dispayAllWords();

        
    }
    
}
