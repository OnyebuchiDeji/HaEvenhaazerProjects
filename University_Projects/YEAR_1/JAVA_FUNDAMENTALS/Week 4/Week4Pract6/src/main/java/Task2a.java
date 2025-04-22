/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author x7e30
 */

import java.io.*;

public class Task2a {
   
    String myFileName;

    Task2a(String name)    //  My constructor!!!
    {
        this.myFileName = name;
    }
    
    public void clearFile()
    {
        /*
            Comment: Wed-21-Feb-2024
            Just like create files, but opens file in write mode...
            if that file exists, specifically targetting that file...
            so that on opening in write mode, previous content is erased!
        */
       File fileInstance = new File(myFileName);

       if (fileInstance.exists())
        {
            System.out.println("Clearing File!!");
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
        File fileInstance = new File(myFileName);   //  This is just an object that identifies a class...

        if (fileInstance.exists())  //  so that one can do this
        {
           try
           {
               //   The boolean true in FileWriter() means to append
               PrintWriter pwr = new PrintWriter(new FileWriter(myFileName, true)); //  This is the main input/output stream
               pwr.println(Task3.date_time() + ":  " + lineWords);                          //  The thing that makes the file and allows read and write
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
