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

class QueueBoundaryException extends RuntimeException
{
    public QueueBoundaryException(String msg)
    {
        super(msg);
    }
}

interface QueueInterfaceTInt
{
    public boolean isEmpty();
    public boolean isFull();
    public int serve();
    public int peek();
    public void enQueue(int datum);
    public int queueLength();
}

public class Queue implements QueueInterfaceTInt{
 
    private int[] queue_buffer = null;
    private int frontPointer = 0;
    private int backPointer = 0;
    
    public Queue(int initialSize)
    {
        this.queue_buffer = new int[initialSize];
        frontPointer= 0;
        backPointer = -1;
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
    public int peek()
    {
        if (isEmpty())
            throw new QueueBoundaryException("Queue is empty; there is not data to peek at!");
        return this.queue_buffer[frontPointer];
    }
    
    @Override
    public int serve()
    {
        if (isEmpty())
            throw new QueueBoundaryException("Queue is empty; there is no data to serve!");
        //  Store value to be served
        int val = this.queue_buffer[(frontPointer++)%queue_buffer.length];
        //  Remove the served value from array. Basically, give it value 0
        this.queue_buffer[frontPointer - 1] = 0;
        //  Return the value
        return val;
    }
    
    @Override
    public void enQueue(int datum)
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
        int[] newBuffer = new int[queueLength() * 2];
        System.arraycopy(this.queue_buffer, 0, newBuffer, 0, this.queue_buffer.length);
//        String buffer = "";
//        for (int i : newBuffer)
//        {
//            buffer += i + " ";
//        }
//        System.out.println(buffer);
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
    
    public static void main(String[] args)
    {
        Queue myQueue = new Queue(10);
//        this.queue_buffer(10)
        for (int i = 0; i < 10; i++)
            myQueue.enQueue(i);
        
        System.out.println("Queue Array Display before expanding: " + myQueue.displayArray());
        System.out.println("Actual Elements of queue before expanding: " + myQueue.displayQueue());
        System.out.println("Size of my Queue before expanding: " + myQueue.queueLength());
        System.out.println("Capacity of my Queue before expanding: " + myQueue.queueCapacity());
        myQueue.expand();
                System.out.println("Queue Array Display after expanding: " + myQueue.displayArray());
        System.out.println("Actual Elements in my Queue after expanding: " + myQueue.displayQueue());
        System.out.println("Size of my Queue after expanding: " + myQueue.queueLength());
        System.out.println("Capacity of my Queue after expanding: " + myQueue.queueCapacity());
        
    }
}
