package Files_and_Directories.Exercise;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;

public class FilesExerciseB {

    public static void main(String[] args)
    {
        String currentDir = "src/Files_and_Directories/Exercise/";
        String newFolder = "folderC";

        try {


            // Create a new empty file called example.txt inside folderA
            createFile("example2.txt", currentDir);

            createDirectory(newFolder, currentDir);


            // Copy the file to folderB

            //  The copyFile method automatically adds a backslash('/') at the end if it is not there
            String destDir = currentDir + newFolder;
            copyFile("example2.txt", currentDir, destDir);

            // List the contents of folderB to check that your file is in there
            listDirectoryContents();
        }
        catch (IOException e) {e.printStackTrace();}
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

    static void createFile(String fileName, String destination) throws IOException
    {
        System.out.println("\nCreating file " + fileName + "...");

        destination = addBackSlash(destination);

        Path filePath = Paths.get(destination + fileName);


        if (Files.notExists(filePath))
        {
            Files.createFile(filePath);
        }


        System.out.println(fileName + " Created!!!");
    }

    static void createDirectory(String dirName, String dirPath) throws IOException
    {
        System.out.println("\nCreating Directory " + dirName + "...");
        dirPath = addBackSlash(dirPath);

        Path path = Paths.get(dirPath + dirName);

        if (Files.notExists(path))
        {
            Files.createDirectory(path);
        }

        System.out.println(dirName + " Created!!!");
    }

    static void copyFile(String fileName, String currentPath, String destPath) throws IOException
    {
        System.out.println("\nCopying " + fileName + " to " + destPath);
        String[] pathArgs= {currentPath, destPath};
        //  First turns the String[] array to a stream...
        //  then use the .map mehtod to perform tha operation on all the String elements
        //  then turn the stream object into a List preserving the type as String...
        //  Then to an Array
        //  The method, FilesExerciseB::addBackSlash is a method reference
        pathArgs = (Arrays.stream(pathArgs).map(FilesExerciseB::addBackSlash).toList()).toArray(pathArgs);

        Path current = Paths.get(pathArgs[0] + fileName);
        Path destination = Paths.get(pathArgs[1] + fileName);

        if (Files.notExists(destination))
            Files.copy(current, destination);

        System.out.println("Copied!!!");
    }

    static void listDirectoryContents() throws IOException
    {
        System.out.println("\nList of Items in Directory: ");

        Files.list(Paths.get("."))
                .forEach(System.out::println);

        System.out.println("Done Printing");
    }

}
