/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package MyTreeDT.source;

/**
 *
 * @author Ebenezer Ayo-Meti
 * Written: Wed-21-Feb-2024
 */

//import java.lang;
//  For Generic Class Stuff
import java.lang.reflect.Array;
import java.util.Arrays;
import java.lang.SuppressWarnings;

class QueueBoundaryException extends RuntimeException
{
    public QueueBoundaryException(String msg)
    {
        super(msg);
    }
}

interface QueueInterface<T>
{
    public boolean isEmpty();
    public boolean isFull();
    public T serve();
    public T peek();
    public void enQueue(T datum);
    public int queueLength();
}

public class QueueGeneric<T> implements QueueInterface<T>{
 
    private T[] queue_buffer;
    private int frontPointer;
    private int backPointer;
    
    /**
     * Date: Sun-26-May-2024
     * Three different ways of making the constructor of generice
     * data types/classes:
    */
    
    /*______@1______DEFAULT CONSTRUCTOR_____*/
    private <T> T[] newArray(int length, T[] array)
    {
        return Arrays.copyOf(array, length);
    }
    
    @SuppressWarnings("unchecked")
    public QueueGeneric()
    {
        frontPointer = 0;
        backPointer = -1;
        this.queue_buffer = newArray(10, (T[]) new Object[10]);
    }
    
    /*################################################*/
    
    /*______@2_SECOND_CONSTRUCTOR___________*/
    @SuppressWarnings("unchecked")
    public QueueGeneric(int initialSize)
    {
        this.queue_buffer = (T[]) new Object[initialSize];
        this.frontPointer = 0;
        this.backPointer = -1;
    }
    /*#################################*/
    
    /*________@3____THIRD CONSTRUCTOR_____*/
    @SuppressWarnings("unchecked")
    public QueueGeneric(Class<T> cls, int initialSize)
    {
        frontPointer = 0;
        backPointer = -1;
        
        this.queue_buffer = (T[]) Array.newInstance(cls, initialSize);
    }
    
    @Override
    public boolean isEmpty()
    {
        return (queueLength() == 0);
    }
    
    @Override
    public boolean isFull()
    {
        return queueLength() == queue_buffer.length;
    }
    
    @Override
    public T peek()
    {
        if (isEmpty())
            throw new QueueBoundaryException("Queue is empty; there is not data to peek at!");
        return this.queue_buffer[frontPointer];
    }
    
    @Override
    public T serve()
    {
        if (isEmpty())
            throw new QueueBoundaryException("Queue is empty; there is no data to serve!");
        //  Store value to be served
        T val = this.queue_buffer[frontPointer++%queue_buffer.length];
        //  Remove the served value from array. Basically, give it value 0
        this.queue_buffer[frontPointer - 1] = null;
        //  Return the value
        return val;
    }
    
    @Override
    public void enQueue(T datum)
    {
        if (isFull())
            expand();
        this.queue_buffer[(++backPointer)%queue_buffer.length] = datum;
    }
    
    @Override
    public int queueLength()
    {
        return (backPointer - frontPointer) + 1;
    }
    
    public int queueCapacity()
    {
        return this.queue_buffer.length;
    }
    private void expand()
    {
        T[] newBuffer = (T[]) new Object[queueLength() * 2];
        System.arraycopy(this.queue_buffer, 0, newBuffer, 0, this.queue_buffer.length);
        this.queue_buffer = newBuffer;
    }
    
    
    private String displayQueue()
    {
        int i = frontPointer;
        int printCount = 0;
        String buffer = "";
        while (printCount < queueLength())
        {
            buffer = buffer + queue_buffer[(i++)%queue_buffer.length] + " ";
            printCount++;
        }
        return buffer;
    }
    
    private String displayArray()
    {
        String buffer = "";
        for (int i = 0; i < queue_buffer.length; i++)
        {
            if (i != queue_buffer.length - 1)
                buffer = buffer + queue_buffer[i] + " ";
            else
                buffer = buffer + queue_buffer[i] + "";
        }
        return buffer;
    }
    
    private static void test1()
    {
        QueueGeneric<Integer> myQueue = new QueueGeneric<>(10);
//        this.queue_buffer(10)
        for (int i = 0; i < 10; i++)
            myQueue.enQueue(i);
        
        System.out.println("Queue Array Display before expanding: " + myQueue.displayArray());
        System.out.println("Actual Elements of queue before expanding: " + myQueue.displayQueue());
        System.out.println("Size of my Queue before expanding: " + myQueue.queueLength());
        System.out.println("Capacity of my Queue before expanding: " + myQueue.queueCapacity());
//        myQueue.expand();
        System.out.println("Queue Array Display after expanding: " + myQueue.displayArray());
        System.out.println("Actual Elements in my Queue after expanding: " + myQueue.displayQueue());
        System.out.println("Size of my Queue after expanding: " + myQueue.queueLength());
        System.out.println("Capacity of my Queue after expanding: " + myQueue.queueCapacity());
        
    }
    
    private static void test2()
    {
        QueueGeneric<String> queue1 = new QueueGeneric<>(10);
        queue1.enQueue("Bread");
        System.out.println(queue1.peek());

        /*
            This form is the checked form of it.
            because it takes a Class<T> type parameter, it enforces type check.
            Whereas, the latter since it takes just Object[], it doesn't enforce any type...
            checking, so it is not type safe since anythng can be passed to it.
            
            Yet, there is a better way that enables you to remove the...
            unchecked cast warning by the compiler.
            I make a random class to show the implementation.
        */
        QueueGeneric<String> queue2 = new QueueGeneric<>(String.class, 10);
        queue2.enQueue("Bread");
        System.out.println(queue1.peek());
        
       
        queue2.enQueue("Cake");
        queue2.enQueue("Bread");
        queue2.enQueue("Cookies");
        queue2.enQueue("Flapjack");
        queue2.displayQueue();
        
    }
 
    public static void main(String[] args)
    {
        test1();
    }
}

