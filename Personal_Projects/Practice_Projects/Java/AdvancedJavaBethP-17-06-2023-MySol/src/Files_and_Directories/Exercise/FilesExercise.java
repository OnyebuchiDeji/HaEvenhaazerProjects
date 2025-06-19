package Files_and_Directories.Exercise;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class FilesExercise {

    public static void main(String[] args)
    {
        String currentDir = "src/Files_and_Directories/Exercise/";
        String newFolder = "folderB";

        // Create a new empty file called example.txt inside folderA
        createFile("example.txt", currentDir);

        createDirectory(newFolder, currentDir);


        // Copy the file to folderB

        //  The copyFile method automatically adds a backslash('/') at the end if it is not there
        String destDir = currentDir + newFolder;
        copyFile("example.txt", currentDir, destDir);

        // List the contents of folderB to check that your file is in there
        listDirectoryContents();

        /*
         // Just testing the addBackSlash method
         String test = "Deji";
        System.out.println(addBackSlash(test));*/

        /*
        //  Me testing how to use streams on arrays and then turn back that stream into an array...
        //  that still has the same type.
        //  Doing toArray on the stream returns an array of type Object[]
        //  But turning the Stream first to a List and then to an array Object...
        //  Preserves the type information

        String[] testArr = {"Yo", "cake", "Beard"};
        //  The List:
        List<String> Arr = Arrays.stream(testArr).map((str)->addBackSlash(str)).toList();
        //  Re assigning the array:
        testArr = Arr.toArray(testArr);
        //  Can be done without making the List, Arr:
        testArr = Arrays.stream(testArr).map((str)->addBackSlash(str)).toList().toArray(testArr);
        //  Printing the items of the array using the streams() method
        Arrays.stream(testArr).forEach(System.out::println);
        //  Printing using the lsie
        Arr.stream().forEach(System.out::println);
        */
    }

    static String addBackSlash(String str)
    {
        if (str.charAt(str.length() - 1) != '/')
            str += '/';

        return str;
    }

    static void createFile(String fileName, String destination)
    {
        System.out.println("\nCreating file " + fileName + "...");

        destination = addBackSlash(destination);

        Path filePath = Paths.get(destination + fileName);

        try
        {
            if (Files.notExists(filePath))
            {
                Files.createFile(filePath);
            }
        }
        catch(IOException e) {e.printStackTrace();}

        System.out.println(fileName + " Created!!!");
    }

    static void createDirectory(String dirName, String dirPath)
    {
        System.out.println("\nCreating Directory " + dirName + "...");
        dirPath = addBackSlash(dirPath);

        Path path = Paths.get(dirPath + dirName);

        try
        {
            if (Files.notExists(path))
            {
                Files.createDirectory(path);
            }
        }
        catch(IOException e) { e.printStackTrace();}

        System.out.println(dirName + " Created!!!");
    }

    static void copyFile(String fileName, String currentPath, String destPath)
    {
        System.out.println("\nCopying " + fileName + " to " + destPath);
        String[] pathArgs= {currentPath, destPath};
        //  First turns the String[] array to a stream...
        //  then use the .map mehtod to perform tha operation on all the String elements
        //  then turn the stream object into a List preserving the type as String...
        //  Then to an Array
        pathArgs = (Arrays.stream(pathArgs).map((str)->addBackSlash(str)).toList()).toArray(pathArgs);

        Path current = Paths.get(pathArgs[0] + fileName);
        Path destination = Paths.get(pathArgs[1] + fileName);

        try
        {
            if (Files.notExists(destination))
                Files.copy(current, destination);
        }
        catch(IOException e) {e.printStackTrace();}
        System.out.println("Copied!!!");
    }

    static void listDirectoryContents()
    {
        System.out.println("\nList of Items in Directory: ");
        try
        {
            Files.list(Paths.get("."))
                    .forEach(System.out::println);
        }
        catch(IOException e) {e.printStackTrace();}

        System.out.println("Done Printing");
    }

}
