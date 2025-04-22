package MyQueueDT.source;

//  For Generic Class Stuff
import java.lang.reflect.Array;
import java.util.Arrays;
import java.lang.SuppressWarnings;

/**
 *
 * @author Ebenezer Ayo-Meti
 * created: Thurs-25-10-2023
 * The stack datatype has been implemented and it is able to resize in capacity.
 * 
 * Revisited: Sun-26-May-2024
 */

class MyQueueArrayBased<T> implements MyQueueInterface<T>
{

    private T[] queueArray;
    // List<T> array;
    int front, back;
    
    /**
     * Date: Sun-26-May-2024
     * Three different ways of making the constructor of generice
     * data types/classes:
     */
    
    /*_______________1______________*/
    private <E> E[] newArray(int length, E[] array)
    {
        return Arrays.copyOf(array, length);
    }
    
    @SuppressWarnings("unchecked") 
    public MyQueueArrayBased()
    {
        front = 0;
        back = -1;
        // this.array = new ArrayList<>(10);

        this.queueArray =  newArray(10, (T[]) new Object[10]);
    }
    /*###########################################*/
    
    /*______________2________________*/
    @SuppressWarnings("unchecked") 
    public MyQueueArrayBased(int initialSize)
    {
        front = 0;
        back = -1;
        // this.array = new ArrayList<>(10);

        this.queueArray =  (T[]) new Object[initialSize];
    }
    /*#####################################*/
    
    /*__________________3_____________________*/
//    @SuppressWarnings("unchecked") 
    public MyQueueArrayBased(Class<T> cls, int initialSize)
    {
        front = 0;
        back = -1;
        // this.array = new ArrayList<>(10);

        this.queueArray =  (T[]) Array.newInstance(cls, initialSize);
    }
    /*#########################################*/

    @Override
    public boolean isEmpty()
    {
        return (queueLength() == 0);
    }

    @Override
    public boolean isFull()
    {
        return (queueLength() == queueArray.length);
    }

    @Override
    public T serve()
    {
        if (isEmpty())
            throw new QueueBoundaryException("Queue is empty; there is no data to serve!");
        return this.queueArray[front++%queueArray.length];
    }

    
    @Override
    public void enQueue(T datum)
    {
        if (isFull())
            throw new QueueBoundaryException("Queue is full! Can't add anymore!");
        this.queueArray[(++back)%queueArray.length] = datum;
    }

    @Override
    public T peek()
    {
        if (isEmpty())
            throw new QueueBoundaryException("Queue is empty; there is no data to peek at!");
        return this.queueArray[front];   
    }


    @Override
    public int queueLength()
    {
        return back - front + 1;
    }

    public String displayQueue()
    {
        int i = front;
        int printcount = 0;
        String buffer = "";

        while (printcount < queueLength())
        {
            buffer = buffer + queueArray[i++%queueArray.length] + " ";
            printcount++;
        }
        return buffer;
    }

    public String displayArray()
    {
        String buffer = "";

        for (int i=0; i<queueArray.length; i++)
        {
            if (i!=queueArray.length -1)
                buffer = buffer + queueArray[i] + " ";
            else
                buffer = buffer + queueArray[i] + "";
        } 
        return buffer;
    }
}

class Entity<T>
{
    private T[] m_store;
    int m_size = 0;
    
    public Entity(Class<T[]> cls, int size)
    {
        m_store = cls.cast(Array.newInstance(cls.getComponentType(), size));
        
    }
    
    public void push(T datum)
    {
        m_store[m_size] = datum;
        m_size++;
    }
    
    public void pop()
    {
        m_store[m_size - 1] = null;
        m_size--;
    }
    
    public void print_store()
    {
        String str = "";
        for (int  i = 0; i < m_store.length; i++)
        {
            if (m_store[i] != null)
            {
                if (i != m_store.length-1)
                    str += m_store[i] + " ";
                else
                    str += m_store[i] + "";
            }
        }
        System.out.println("The Entity's store: " + str);
    }
}

public class QueueImplementation
{
    public static void main(String[] args)
    {
        // Class<String> mc = new Class<String>();

        MyQueueArrayBased<String> queue1 = new MyQueueArrayBased<>(10);
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
            It is that Entity class.
        */
        MyQueueArrayBased<String> queue2 = new MyQueueArrayBased<>(String.class, 10);
        queue2.enQueue("Bread");
        System.out.println(queue1.peek());
        
        Entity<String> ent= new Entity<>(String[].class, 10);
        ent.push("Cake");
        ent.push("Bread");
        ent.push("Cookies");
        ent.push("Flapjack");
        ent.print_store();
    }
}