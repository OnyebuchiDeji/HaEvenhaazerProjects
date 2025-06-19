package Functional_Programming_Java.Method_References;

import java.util.List;
import java.util.Arrays;

public class MethodReferences
{
    public static void main(String[] args)
    {
        List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9);

        System.out.println("Using normal lambda function: ");
        //  forEach iterates over each value in list, passing it into the lambda function...
        //  as an argument. The lambda function then passes the value as an argument into...
        //  the NumberUtils.evenOrOdd() method
        nums.forEach((num)->NumberUtils.evenOrOdd(num));

        System.out.println("\nUsing Method Reference");
        //  I can Use a MethodReference to do the same.
        //  It is more concise
        nums.forEach(NumberUtils::evenOrOdd);
    }
}
