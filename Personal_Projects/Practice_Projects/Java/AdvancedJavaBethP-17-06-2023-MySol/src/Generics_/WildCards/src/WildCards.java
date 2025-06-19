package Generics_.WildCards.src;
import java.util.ArrayList;
import java.util.List;

/*
*   Because a List of a class object ShirtItem is not the same with a List of the object, ClothingItem...
*   One cannot pass in a list of ShirtItem (List<ShirtItem>) as an argument for a method...
*   that takes a list of ClothingItem (List<ClothingItem>).
*   Therefore, wild cards are used in this way: List<? extend ClothingItem>, to allow...
*   any Object that is derived from or extends ClothingItem to be passed into the method...
*   that uses a parameter of type List<? extend ClothingItem> as an argument.
*   ... Vise versa, if used this way: List<? super ShirtItem>, this allows only the...
*   classes that are parents of ShirtItem to be passed into the method as an argument
* */
public class WildCards
{
    public static void main(String[] args)
    {
        List<ShirtItem> shirtList = new ArrayList<>();
        shirtList.add(new SweatShirt());
        shirtList.add(new ShirtItem());
        shirtList.add(new SweatShirt());

        List<JacketItem> jacketList = new ArrayList<>();
        //  Still, I can fill a list of JavketItem with SweatShirt and ShirtItem objects...
        //  because they all inherit from CLothingItem...
        //  This is the Liskov Substitution Principle
        shirtList.add(new SweatShirt());
        shirtList.add(new ShirtItem());
        shirtList.add(new SweatShirt());

        checkOutAllItems(shirtList);

        //  See, if uncommented, it is seen that a List of object JacketItem...
        //  Cannot be passed in because object SweatShirt never extends JacketItem.
        //checkOutAllItems(jacketList);
    }

    /*  The statement List<? extends ClothingItem> means that the parameter...
    *   can only receive Lists of types that extend ClothingItem
    *   Likewise if it was super, only types that are the parents of that type...
    *   Can be received.
    * */
    /*
    static void checkOutAllItems(List<? extends ClothingItem> items)
    {
        ClothingSite cs  = new ClothingSite();
        for (ClothingItem item : items)
        {
            cs.checkOutItem(item);
        }
    }
    */
    /*For Objects that Parents of SweatShirt, or from which SweatShirt inherits*/
    static void checkOutAllItems(List<? super SweatShirt> items)
    {
        ClothingSite cs  = new ClothingSite();
        for (Object item : items)
        {
            cs.checkOutItem((ClothingItem) item);
        }
    }
}


class ClothingSite
{
    /*
     *   Liskov Substitution Principle is what allows this method to also
     *   accept types derived from ClothingItem
     */

    void checkOutItem(ClothingItem item)
    {
        System.out.println("Item Purchased: " + item.getName() + ", price: " + item.getPrice());
    }
}


abstract class ClothingItem
{
    abstract int getPrice();
    abstract String getName();
}

class ShirtItem extends ClothingItem
{
    @Override
    int getPrice(){return 10;}

    @Override
    String getName(){return "Shirt";}
}

class SweatShirt extends ShirtItem
{
    @Override
    int getPrice(){return 7;}

    @Override
    String getName(){return "Sweat Shirt";}
}

class JacketItem extends ClothingItem
{
    @Override
    int getPrice(){return 25;}

    @Override
    String getName(){return "Jacket";}
}