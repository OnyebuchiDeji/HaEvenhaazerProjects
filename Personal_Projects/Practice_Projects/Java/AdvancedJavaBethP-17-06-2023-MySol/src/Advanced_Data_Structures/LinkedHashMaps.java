package Advanced_Data_Structures;

import java.util.LinkedHashMap;
import java.util.HashMap;

public class LinkedHashMaps
{
    public static void main(String[] args)
    {
        HashMapEG();
        LinkedHashMapEG();
    }

    static void HashMapEG()
    {
        System.out.println("HashMap Example");
        HashMap<Character, Integer> hMap = new HashMap<>();
        hMap.put('A', 23);
        hMap.put('E', 15);
        hMap.put('K', 30);
        hMap.put('L', 1);

        //  It prints the values in an unodered way
        hMap.forEach((key, val)-> System.out.println(key + ": " + val));
    }

    static void LinkedHashMapEG()
    {
        System.out.println("\nLinkedHAshMape Example: ");
        //  Prints in order, according to how it was added
        LinkedHashMap<Character, Integer> lhMap = new LinkedHashMap<>();
        lhMap.put('A', 23);
        lhMap.put('E', 15);
        lhMap.put('K', 30);
        lhMap.put('L', 1);

        lhMap.forEach((key, val)-> System.out.println(key + ": " + val));

        System.out.println("\nAfter switching on access order");

        LinkedHashMap<Character, Integer> lhMap2 = new LinkedHashMap<>(10, 0.75f, true);
        lhMap2.put('A', 23);
        lhMap2.put('E', 15);
        lhMap2.put('K', 30);
        lhMap2.put('L', 1);

        lhMap2.replace('E', 300);   //  The most recently accessed will be last

        lhMap2.forEach((key, val)-> System.out.println(key + ": " + val));

        System.out.println(lhMap2.values());
    }
}
