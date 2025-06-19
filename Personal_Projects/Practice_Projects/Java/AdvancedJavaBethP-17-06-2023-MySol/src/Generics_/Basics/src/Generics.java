package Generics_.Basics.src;


import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;


public class Generics
{
    public static void main(String[] args)
    {
        withoutGenericsEG();

        System.out.println('\n');

        usingGenerics();

        //  Generic method example
        String[] words = {"God", "is", "good"};
        Integer[] nums = {1, 23, 46};

        //  Using a Single Method to Convert Array to List:
        System.out.println("\n");
        GenericMethods ugm = new GenericMethods();
        List<String> lstArray = ugm.convertArrayToList(words);
        List<Integer> intArray = ugm.convertArrayToList(nums);

        for (String str : lstArray)
        {
            System.out.print(str + ' ');
        }
        System.out.println('\n');
        for (Integer num : intArray)
        {
            System.out.println(num + ' ');
        }

    }

    static void withoutGenericsEG()
    {

        System.out.println("Without Using Generics Example:\n");
        //  Lists can be created without specifying the generic type
        //  EG:
        List shapes = new ArrayList();
        //  Thus I can add any object into it
        shapes.add("Circle");   //  A string

        //  This doesn't work, because the compiler cannot tell that "Circle" is a String
        /*System.out.printf(shapes.get(0));*/
        //  So, it must be cast
        String circle = (String) shapes.get(0);
        System.out.printf(circle + "\n");

        shapes.add(new Rectangle());
        //  Also cannot print out because the compiler cannot distinguish, so
        Rectangle rectangleObj = (Rectangle) shapes.get(1);
        //  Downside about this is that each object has to be known so that...
        //  it can be cast to the appropriate type
        rectangleObj.giveDetails();

        //  Also allows an integer
        shapes.add(54);
        int shapeNum = (Integer)shapes.get(2);
        System.out.printf("%d\n", shapeNum);

    }



    static void usingGenerics()
    {
        System.out.println("Using Generics:\n");
        List<String> strShapes = new ArrayList();

        strShapes.add("Square");
        strShapes.add("Circle");
        strShapes.add("Triangle");
        strShapes.add("Rectangle");

        for (String str : strShapes)
        {
            System.out.println(str);
        }

    }

}


class GenericMethods
{
    //  The first <T> specifies the return type can be of any type.
    //  The second T means it returns a List that contains elements of the same type, but the type...
    //  can be any type T specified, T
    //
    public <T>List<T> convertArrayToList(T[] array)
    {
        return Arrays.asList(array);
    }
}

class Rectangle
{
    static int numOfInstantiations = 0;
    int id = 0;

    Rectangle()
    {
        numOfInstantiations += 1;
        id += numOfInstantiations;
    }

    public void giveDetails()
    {
        System.out.println("Rectangle " + id);
    }

}
