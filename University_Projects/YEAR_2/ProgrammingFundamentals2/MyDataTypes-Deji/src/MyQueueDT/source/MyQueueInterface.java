package MyQueueDT.source;

public interface MyQueueInterface<T>
{
    public boolean isEmpty();

    public boolean isFull();

    public T serve();

    public T peek();

    //  Add to queue
    public void enQueue(T datum);

    public int queueLength();

}