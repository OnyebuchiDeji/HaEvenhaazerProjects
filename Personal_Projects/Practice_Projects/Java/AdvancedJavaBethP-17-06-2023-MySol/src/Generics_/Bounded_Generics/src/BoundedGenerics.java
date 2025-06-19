package Generics_.Bounded_Generics.src;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;



public class BoundedGenerics
{
    /*  Bounded Generics
    *
    *   These are a way to restrict the types a method can return
    *   For example, a method can be restricted to only return a type that is the...
    *   subtype of a super type or class, or vise-versa, to return every type that...
    *   is the super or parent type of the derived type.
    *
    */

    public static void main(String[] args)
    {
        BoundedGenericsEG1();

        Shapes square = new Shapes("Square");
        Shapes triangle = new Shapes("Triangle");
        Shapes circle = new Shapes("Circle");
        square.speak();
        square.sayId();
        triangle.speak();
        triangle.sayId();
        circle.speak();
        circle.sayId();

    }

    /*
    *   The <T extends Number> part is called the return type boundary specifier
    *   This prevents one to pass in any array that does not extend the Number base class.
    */
    private static <T extends Number> List<T> convNumArrayToList(T[] array)
    {
        return Arrays.asList(array);
    }

    private static void BoundedGenericsEG1() {
        //  EG:
        Double[] doubleNums = {2.4, 3.9, 15.0};
        Integer[] intNums = {83, 21, 8, 0};
        String[] someStrs = {"Yh", "Fact", "True", "Amen"};

        List<Double> doubleList = convNumArrayToList(doubleNums);
        List<Integer> intList = convNumArrayToList(intNums);
        //  This gives an error because whatever type is passed in will cause T to be that type...
        //  But the convNumArrayToList method makes sure that T must extend the Number class...
        //  this causes an error:
        //List<String> someStrsList = convNumArrayToList(someStrs);

        for (Number num : doubleList) {
            System.out.println("Double array: " + num);
        }

        for (Number num : intList) {
            System.out.println("Integer array: " + num);
        }

    }
}


class Entity
{
    static int id = 0;
    private int entityNum = 0;
    private String name;

    Entity(){}

    Entity(String name)
    {
        id++;
        entityNum = id;
        this.name = name;

    }

    void speak()
    {
        System.out.println("I am a " + name);
    }

    void sayId()
    {
        System.out.println("Entity " + this.entityNum);
    }
}

class Shapes extends Entity
{
    /*@Override
    protected Object clone() throws CloneNotSupportedException {
        return super.clone();
    }*/

    Shapes()
    {}

    Shapes(String name)
    {
        super(name);    //  super refers to Entity(String name)
    }

}

