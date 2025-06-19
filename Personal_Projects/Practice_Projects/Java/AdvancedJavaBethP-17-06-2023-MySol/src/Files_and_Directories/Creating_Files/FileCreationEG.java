package Files_and_Directories.Creating_Files;

import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.io.IOException;

public class FileCreationEG
{
    public static void main(String[] args)
    {
        String name = "myFile1.txt";

        try
        {
            Path path = Paths.get("src/Files_and_Directories/Creating_Files/" + name);
            if (Files.notExists(path)) {
                Files.createFile(path);
            }
        }
        catch(IOException e)
        {
            e.printStackTrace();
        }
    }

}
