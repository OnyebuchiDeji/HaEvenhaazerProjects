package Advanced_Data_Structures;

import java.util.HashMap;

public class HashMaps
{
    public static void order_test()
    {
        HashMap<String, Integer> basket = new HashMap<>();
        basket.put("Beans", 2);
        basket.put("Orange", 12);
        basket.put("Apple", 5);
        basket.forEach((key, val)->
        {
            System.out.println("Key: " + key + ", Val: " + val);
        });
    }
    
    public static void main(String[] args)
    {
        HashMap<String, Integer> basket = new HashMap<>();
        basket.put("Orange", 4);
        System.out.println(basket.get("Orange"));
        basket.put("Orange", 5);
        System.out.println(basket.get("Orange"));

        //  Adds a new key-value pair, setting the value to 4
        //  But if the pair already exists, it adds 4 to the already existing value
        basket.merge("Apple", 4, Integer::sum);
        System.out.println("number of Apples: " + basket.get("Apple"));
        basket.merge("Apple", 4, Integer::sum);
        System.out.println("number of Apples: " + basket.get("Apple"));

        System.out.println("Previous number of oranges: " + basket.get("Orange"));
        basket.merge("Orange", 5, Integer::sum);
        System.out.println("number of Oranges: " + basket.get("Orange"));
        basket.forEach((key, val)->
        {
            System.out.println("Key: " + key + ", Val: " + val);
        });
        System.out.println("\n");
        order_test();
    }
}
