package Advanced_Data_Structures;

import java.util.LinkedList;

public class LinkedLists
{
    public static void main(String[] args)
    {
        LinkedList<String> lList = new LinkedList<String>();
        lList.add("Likeness");
        lList.add("Glory");
        lList.add("similitude");

        System.out.println(lList);
        System.out.println(lList.getFirst());
        System.out.println(lList.getLast());

        System.out.println("Removed " + lList.pollLast());   //  Removed likeness, first value
        System.out.println(lList);          //  Prints remnant

        System.out.println("Removed " + lList.pop());    //  Removes Glory, new first value
        System.out.println(lList);

        System.out.println("Removed " + lList.pop());
        System.out.println("Empty: " + lList);

        // System.out.println("What occurs now " + lList.pop());
        // System.out.println("What occurs now " + lList.poll());

        lList.add("I");
        lList.add("am");
        lList.add("not");
        lList.add("alone");
        lList.add("The");
        lList.add("Father");
        lList.add("is");
        lList.add("with");
        lList.add("me");

        for (String str : lList)
        {
            System.out.println(str);
        }
    }


}
