/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */


/**
 *
 * @author Ebenezer Ayo-Meti
 * created: Thurs-25-10-2024
 * The stack datatype has been implemented and it is able to resize in capacity.
 */

import java.lang.reflect.Array;

/**
 * Date: Thurs-30-May-2024
 * 
 * Added other constructor, actually wanted to replace the old one as you can see below.
 * It affected my TreeDT.java
 * It affected the deleting. I think it has something
 * to do with the type info on constructing
 * Especially the copying, because part of the algorithm
 * involved adding to the stack and peeking at it.
 * It was meant to return the reference to the same object,
 * but it didn't work.
 * So I compared it with the Queue DT, which works. Hence
 * I considered that this changing the constructor to match that
 * of the queue was the right solution.
 * 
 * TURNS OUT THAT THIS SPECULATION WAS NOT CORRECT
 * because the recursive deletion method gave the same error as the
 * iterative method in which I employ this.
 * HENCE I LEAVE THE CONSTRUCTOR THE SAME
 */
class StackBoundaryException extends RuntimeException
{
    public StackBoundaryException(String msg)
    {
        super(msg);
    }
}

interface StackInterface<T> {
    
    public void push(T datum);
    public T pop();
    public T peek();
    public boolean isEmpty();
    public boolean isFull();
    public int get_size();
    public int get_capacity();
    

}



public class MyStackDT<T> implements StackInterface<T>
{
    private T[] m_buffer;
    private int m_size;
    private Class<T[]> type_info;

    public MyStackDT(Class<T[]> cls, int capacity)
    {
        m_buffer = cls.cast(Array.newInstance(cls.getComponentType(), capacity));
        m_size = 0;
        type_info = cls;
    }
    public MyStackDT(int capacity)
    {
        m_buffer = (T[]) new Object [capacity];
        m_size = 0;
    }
    
    @Override
    public void push(T datum)
    {
        if (isFull())
            resize_buffer();
        m_buffer[m_size] = datum;
        m_size++;
    }
    
    private void resize_buffer()
    {
        int new_capacity = get_capacity() * 2;
//        T[] tempBuffer = type_info.cast(Array.newInstance(type_info.getComponentType(), new_capacity));
        T[] newBuffer = (T[]) new Object[new_capacity];
        /*
            System.arraycopy(source_buffer, startIndexOfSource,
                destination_source, startIndexOfDestination, length_or_capacity_of_source)
        */
        System.arraycopy(m_buffer, 0, newBuffer, 0, get_capacity());
        //  Finally
        m_buffer = newBuffer;
    }
    
    @Override
    public T pop()
    {
        //  This removes the top element, changing the stack
        //  and returning its value
        if (isEmpty())
            throw new StackBoundaryException("Stack is empty! Nothing to pop!");
        
        T val = m_buffer[m_size-1];
        m_buffer[m_size-1] = null;
        m_size--;
        return val;
    }
    
    @Override
    public T peek()
    {
        //  Just gets the value of tap element.
        //  does not change stack
        if (isEmpty())
            throw new StackBoundaryException("Stack is empty! Nothing to see!");
        
        return m_buffer[m_size-1];
    }
    
    @Override
    public boolean isEmpty()
    {
        return (m_size == 0);
    }
    
    @Override
    public boolean isFull()
    {
        return (m_size == get_capacity());
    }
    
    @Override
    public int get_size()
    {
        return m_size;
    }
    
    @Override
    public int get_capacity()
    {
        return m_buffer.length;
    }
    
    public void print_stack_items()
    {
        String str = "";
        for (int i=0; i < get_size(); i++)
        {
            if (i != get_size()-1)
                str += m_buffer[i] + " ";
            else
                str += m_buffer[i];
        }
        System.out.println("The stack contains: " + str);
    }
}

/*
public class StackDT
{
    public static void main(String[] args)
    {
//        String[] arr = {"Cake", "Bread"}; 
//        arr[1] = "croissant";
        //  These don't work
//        MyStackDT<String> stackkun = new MyStackDT(arr.class, 5);
        //  These don't work
//        MyStackDT<String> stackkun = new MyStackDT(arr[0].class, 5);
        //  This works
        MyStackDT<String> stackkun = new MyStackDT(String[].class, 5);
        
        stackkun.push("Eye");
        stackkun.push("Nose");
        stackkun.push("Ear");
        stackkun.push("Elbow");
        stackkun.push("Mouth");
        stackkun.print_stack_items();
        System.out.println("Current size, capacity: " + stackkun.get_size() + ", " + stackkun.get_capacity());
        stackkun.pop();
        stackkun.print_stack_items();
        System.out.println("Current size, capacity: " + stackkun.get_size() + ", " + stackkun.get_capacity());
        stackkun.push("ayin");
        stackkun.push("Praise");
        stackkun.push("God");
        stackkun.push("Pe");
        stackkun.push("Shalom");
        stackkun.print_stack_items();
        System.out.println("Current size, capacity: " + stackkun.get_size() + ", " + stackkun.get_capacity());
    }
}
*/