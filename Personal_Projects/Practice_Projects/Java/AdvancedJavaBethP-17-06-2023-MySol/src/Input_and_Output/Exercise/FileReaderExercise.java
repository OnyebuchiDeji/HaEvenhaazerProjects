package Input_and_Output.Exercise;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class FileReaderExercise {

    // This method should return the first line of BufferedReaderVsScanner.txt.
    public String getFirstLine() {
        String firstLine = "";

        try
        {
            BufferedReader br = new BufferedReader(new FileReader("src/Input_and_Output/Exercise/BufferedReaderVsScanner.txt"));
            firstLine = br.readLine();
            br.close();
        }
        catch(IOException ioExcep) {ioExcep.printStackTrace();}

        return firstLine;
    }

    // This method should return all the content of BufferedReaderVsScanner.txt
    // as a single String.
    public String getWholeFile() {
        String wholeFile = "";

        try
        {
            BufferedReader br = new BufferedReader(new FileReader("src/Input_and_Output/Exercise/BufferedReaderVsScanner.txt"));
            StringBuilder sB = new StringBuilder();
            String exFirstLine = br.readLine();

            //  Doing sB.append(line + "\n") would be better
            br.lines().forEach((line)->sB.append(line + ""));
            wholeFile = sB.toString();

            br.close();
        }
        catch(IOException ioExcep){ioExcep.printStackTrace();}

        return wholeFile;
    }

}
