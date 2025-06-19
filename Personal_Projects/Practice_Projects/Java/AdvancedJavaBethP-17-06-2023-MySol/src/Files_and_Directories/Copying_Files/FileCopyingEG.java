package Files_and_Directories.Copying_Files;

import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.io.IOException;

public class FileCopyingEG
{
    public static void main(String[] args)
    {
        String genPath = "src/Files_and_Directories/Copying_Files/";
        String oldPath = genPath+"A";
        String destPath = genPath+"B";
        copyFile("f1.txt", oldPath, destPath);
    }

    static void copyFile(String fileName, String oldPath, String destPath)
    {
        if (oldPath.charAt(oldPath.length()-1) != '/')
        {
            oldPath += '/';
        }
        if (destPath.charAt(destPath.length()-1) != '/')
        {
            destPath += '/';
        }
        System.out.println("Copying File " + fileName + "...");
        Path oldFilePath =  Paths.get(oldPath + fileName);
        Path newPath = Paths.get(destPath + fileName);

        try
        {
            if (Files.notExists(newPath))
            {
                Files.copy(oldFilePath, newPath);
            }
        }
        catch (IOException e) { e.printStackTrace(); }

        System.out.println("File Copied!!!");
    }
}
