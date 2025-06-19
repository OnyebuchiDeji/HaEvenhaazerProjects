import java.util.*;



public class test
{
    static List<HashMap<String, Integer>> myList;
    /*
     * The goal of this test is to see if returning this local hashmap object...
     * to the list will copy its values into a separate memory area on the list...
     * which is what I hope it does...
     * or if when ------wait
     * 
     * Of course, retrning it will make a copy of the object values.
     * 
     * new test: make the myList object a class member variable and make the doSth() method...
     * void. When I add the local HashMap to the myList object, will it copy the values?
     * Probably yes.
     * 
     */
    public static HashMap<String, Integer> doSth(String key, int number)
    {
        HashMap<String, Integer> localMap = new HashMap<String, Integer>();
        localMap.put(key, number);
        return localMap;
    }

    public static void doSth2(String key, int number)
    {
        HashMap<String, Integer> localMap = new HashMap<String, Integer>();
        localMap.put(key, number);
        myList.add(localMap);
    }

    public static int addTwo(int num)
    {
        return num + 2;
    }
    public static void main(String[] args)
    {
        myList = new ArrayList<>();

        doSth2("Val_1", 1);
        int valOfListHashMap = myList.get(0).get("Val_1");

        System.out.println("The value is " + valOfListHashMap);
        System.out.println("The value is " + myList.get(0));
        
        // List<Integer> listKun = new ArrayList<>();
        // listKun.add(1);
        // listKun.add(44);
        // listKun.add(203);
        // listKun.add(2023);
        // listKun.
        // listKun.forEach((num)->{
        //     System.out.println(addTwo(num));
        // });


        // LinkedHashMap<String, Integer> myMap = new LinkedHashMap<>();
        // myMap.put("First", 1);
        // myMap.put("Second", 2);
        // myMap.put("Third", 3);
        // myMap.entrySet()
        // for (LinkedHashMap.Entry<String, Integer> entry)
        // System.out.println(myMap.values());


        
        // Collection<Integer> mapVals = myMap.values();
        // Integer[] mapValsArray = mapVals.toArray(Integer[] mapValsArray);
        // System.out.println();

        Dog dog1 = new Dog("German Sherperd");
        dog1.doSth();
    }
}

abstract class Entity
{
    static int count = 0;
    private String name;
    private int id;

    public Entity(){}

    public Entity(String name)
    {
        this.name = "Dog: " + name;
        count += 1;
        this.id = count;
    }

    public String  getName()
    {
        return this.name;
    }
    public int  getId()
    {
        return this.id;
    }

    abstract void doSth();

} 

class Dog extends Entity
{
    public Dog(String name)
    {
        super(name);
    }

    @Override
    public void doSth()
    {
        System.out.printf("I am a %s, my id is %s. \n", this.getName(), this.getId());
        System.out.println("Bark! I see spirits because I have no soul, I move and understand just by instinct!\n");
    }

}