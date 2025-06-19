package Files_and_Directories.Directories_In_Java;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;


public class DirectoriesCreationEG {
    public static void main(String[] args)
    {
        listAllInDirectory();

        listOnlyDirectories();

        listOnlyFilesInDirectory();

        createDirectory("pathB");

    }

    static void listAllInDirectory()
    {
        /*
          To list the contents of a directory.
          The .list() method returns a stream of String file paths
          The Paths.get(".") returns all the items in a directory
        */
        System.out.println("\nThis prints out both files and directories");
        try
        {
            Files.list(Paths.get("."))
                    .forEach(System.out::println);
        }
        catch(IOException e) {e.printStackTrace();}
    }

    static void listOnlyFilesInDirectory()
    {
        System.out.println("\nThis prints only files, not directories");
        try
        {
        Files.list(Paths.get("."))
                .filter((content) -> !Files.isDirectory(content))
                .forEach(System.out::println);
        }
        catch (IOException e) { e.printStackTrace();}
    }

    static void listOnlyDirectories()
    {
        System.out.println("\nThis prints only directories");
        try
        {
        Files.list(Paths.get("."))
                .filter((content) -> Files.isDirectory(content))
                .forEach(System.out::println);
        }
        catch (IOException e) { e.printStackTrace();}
    }

    static void createDirectory(String name)
    {
        System.out.println("\nCreating a New Directory...");
        String pathName = name;
        String pathStr = "src/Files_and_Directories/Directories_In_Java/" + pathName;
        Path dirPath = Paths.get(pathStr);
        try
        {
            if (Files.notExists(dirPath))   //  Checks if directory exists before redoing
            {
                Files.createDirectory(dirPath);
            }
        }
        catch(IOException e)    {e.printStackTrace();}

    }
}