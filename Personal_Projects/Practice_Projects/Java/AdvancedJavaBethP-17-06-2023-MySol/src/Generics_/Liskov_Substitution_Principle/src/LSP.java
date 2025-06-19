package Generics_.Liskov_Substitution_Principle.src;

import java.util.ArrayList;
import java.util.List;

public class LSP
{
    public static void main(String[] args)
    {
        List<ClothingItem> items = new ArrayList<>();
        for (int i = 0; i < 2; i++)
        {
            items.add(new ShirtItem());
            items.add(new JacketItem());
        }

        checkOutAllItems(items);
    }

    public static void checkOutAllItems(List<ClothingItem> itemList)
    {
        ClothingSite cs = new ClothingSite();

        for (ClothingItem item: itemList)
        {
            cs.checkOutItem(item);
        }
    }

}


