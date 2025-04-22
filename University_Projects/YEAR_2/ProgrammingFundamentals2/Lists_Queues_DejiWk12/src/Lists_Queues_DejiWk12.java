/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

/**
 *
 * @author Ebenezer Ayo-Meti
 */

//import src.*;


public class Lists_Queues_DejiWk12 {
    
    public static void Task1()
    {
        LinkedList myLL = new LinkedList();

        String[] myObjects = {"First", "Second", "Third", "Fourth", "Fifth"};
        for (String str : myObjects)
        {
            myLL.addToHead(str);
        }
        myLL.displayList();
    }
    
    public static void Task2()
    {
        LinkedList myLL = new LinkedList();
        String[] myObjects = {"First", "Second", "Third", "Fourth", "Fifth"};
        for (String str : myObjects)
        {
            myLL.addToTail(str);
        }
        myLL.displayList();
    }
    
    public static void Task3()
    {
        IntQueueMasking intQueue = new IntQueueMasking(10);
        for (int i=0; i<10; ++i)
        {
            intQueue.enQueue(i);
        }
        
        System.out.println("Normal Printing");
        for (int num : intQueue.arrayQueue)
        {
            if (num!=intQueue.arrayQueue.length)
                System.out.print(num + " ");
            else
                System.out.print(num + "\n");
        }
        
        System.out.println("\nDisplay Array:");
        System.out.println(intQueue.displayArray());
        
        System.out.println("Display Queue:");
        System.out.println(intQueue.displayQueue());
        
        System.out.println("Served "+ intQueue.serve());
        System.out.println("Display Queue:");
        System.out.println(intQueue.displayQueue());
        
        System.out.println("Display Array:");
        System.out.println(intQueue.displayArray());
    
        System.out.println("Served "+ intQueue.serve());
        System.out.println("Display Queue:");
        System.out.println(intQueue.displayQueue());
        
        System.out.println("Display Array:");
        System.out.println(intQueue.displayArray());
        
        System.out.println("""
            Note the difference between printing the queue and printing the...
            array. Printing the queue prints the right thing, but printing the array...
            displays the same thing even when some data have been served.
                           """);
    }

    public static void main(String[] args) {
        Task3();
    }
    
}
