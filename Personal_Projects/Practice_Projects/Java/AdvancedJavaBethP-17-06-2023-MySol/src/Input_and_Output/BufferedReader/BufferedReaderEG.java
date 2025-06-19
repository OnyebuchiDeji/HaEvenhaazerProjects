package Input_and_Output.BufferedReader;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;


public class BufferedReaderEG
{
    public static void main(String[] args)
    {
        try
        {
            BufferedReader br = new BufferedReader(new FileReader("src/Input_and_Output/BufferedReader/AFile.txt"));
            String firstLine = br.readLine();
            System.out.println("First Line: ");
            System.out.println(firstLine);

            //  To print the reamining lines in the file...
            //  Could use a normal for-loop that checks if the next line is null, which is...
            //  the end of the file.
            //  OR
            StringBuilder sB = new StringBuilder();
            //  This lines() method takes each line and makes it a Stream object...
            //  from the Stream class.
            //  Note!! Stream as in the type used with Collections...
            //  not IO Stream objects
            //  that is wht forEach is used on it
            br.lines().forEach((line)->sB.append(line + "\n"));
            System.out.println("Rest of the lines: ");
            System.out.println(sB);
            br.close(); //  Always close resource
        }
        catch(IOException ioExcp){ioExcp.printStackTrace();}

    }
}
