/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author x7e30
 */

import java.io.*;

public class Task2 {
    public class myFileClass    //  Task 2
    {
        String myFileName;
        
        myFileClass(String name)    //  My constructor!!!
        {
            this.myFileName = name;
        }
        
    public void createMyFile()
    {
       File fileInstance = new File(myFileName);

       if (fileInstance.exists())
        {
            System.out.println("File is open!!");
        }
        else
        {
            try 
            {
                PrintWriter fh = new PrintWriter(new FileWriter(myFileName, false));  //  flag is false which indicates to write
                fh.close();
                System.out.println(myFileName + " has been created");
            } 
            catch (IOException e) 
            {
                System.out.println("An IO Exception was thrown!\nMore details:\n" + e.toString());
            }
        }
    }
        
        public void appendText(String lineWords)
        {
            File fileInstance = new File(myFileName);
            
            if (fileInstance.exists())
            {
               try
               {
                   PrintWriter pwr = new PrintWriter(new FileWriter(myFileName, true));
                   pwr.print(Task3.date_time() + "/t" + lineWords);
                   pwr.close();
               }
               catch(IOException exp)
               {
                   System.out.println("There was ane error! Check it: " + exp.toString());
               }
            }
            else
            {
                System.out.println("File does not exist!");
                System.exit(0);
            }
        }
        
        public void dispayAllWords()
        {
            File fileInstance = new File(myFileName);
            
            boolean endOFile = false;
            int lineCount = 0;
            
            if (fileInstance.exists())
            {
                try
                {
                    BufferedReader br = new BufferedReader(new FileReader(myFileName));
                    
                    while(!endOFile)
                    {
                        ++lineCount;
                        
                        String words = br.readLine();
                        
                        if (words == null)
                        {
                            endOFile = true;
                        }
                        else
                        {
                        System.out.println("Line " + lineCount + " : " + words);   
                        }
                    }
                    br.close();
                }
                catch(IOException exp)
                {
                    System.out.println("An Error! Check it! " + exp.toString());
                }
            }
            else
            {
                System.out.println("File does not exist!");
                System.exit(0);
            }
        }
        
    }

}
