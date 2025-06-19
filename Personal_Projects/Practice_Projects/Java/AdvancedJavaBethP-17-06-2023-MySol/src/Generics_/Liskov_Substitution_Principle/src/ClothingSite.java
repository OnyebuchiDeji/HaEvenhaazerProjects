package Generics_.Liskov_Substitution_Principle.src;

public class ClothingSite
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

class JacketItem extends ClothingItem
{
    @Override
    int getPrice(){return 25;}

    @Override
    String getName(){return "Jacket";}
}