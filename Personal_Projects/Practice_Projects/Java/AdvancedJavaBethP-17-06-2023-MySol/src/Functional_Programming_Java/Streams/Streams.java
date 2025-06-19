package Functional_Programming_Java.Streams;

import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;
import java.util.stream.Collectors;

public class Streams
{
    public static void main(String[] args)
    {
        List<String> animalList = Arrays.asList("porcupine", "pigeon", "skink", "longhorn", "slug", "armadillo");

        System.out.println("Processed Without Streams: ");
        List<String> processedList1 = processWithoutStreams(animalList);
        System.out.println(processedList1);
        //  Using the streams api is better, as it uses more concise code.
        //  to perform an operation, and it uses fewer lines of code and typing...
        //  To achieve the same result
        System.out.println("Processed With Streams");
        List<String> processedList2 = processWithStreams(animalList);
        System.out.println(processedList2);
    }

    static List<String> processWithoutStreams(List<String> list)
    {
        List<String> tempList = new ArrayList<>();
        for (String item : list)
        {
            item = item.toUpperCase();
            if (item.startsWith("P"))
            {
                tempList.add(item);
            }
        }

        Collections.sort(tempList);
        return tempList;
    }

    static List<String> processWithStreams(List<String> list)
    {
        /*  .stream() turns it to a stream.

            .map() takes a lambda expression as an argument...
            so a method reference can be used...
            A map method is an intermediate method and so returns a stream with values...
            that have been processed by the lambda expression or method_reference

            .filter is another intermediate method that takes a lambda expression as an argument...

            .collect() takes in a method as an argument
            the method Collectors.toList() turns the stream to a list...
            it then returns this new list
        */

        return list.stream().map(String::toUpperCase)
                .filter(item->item.startsWith("P")) //  Only returns a stream of items that start with P
                .sorted()   //  To sort in alphabetical
                .collect(Collectors.toList());
    }
}
