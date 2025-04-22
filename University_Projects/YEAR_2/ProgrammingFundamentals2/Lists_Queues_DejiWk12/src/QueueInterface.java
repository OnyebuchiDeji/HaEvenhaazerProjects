public interface QueueInterface {
 
/*  This interface defines a simple queue of integer elements.
    The queue is intended to have a FIFO operation. */

  public boolean isFull();
    /* post: if the size of the queue has not reached its upper bound,
             then returns false, else returns true */

  public boolean isEmpty();
    /* post: if the queue has no elements returns true, else false */

  public void enQueue(int element);
    /* pre:  the size of the queue has not reached an upper bound
       post: the queue includes the new element as its most recently
       arrived element  */

  public int serve();
    /* pre:  the queue is not empty
       post: the least recently arrived element is returned and that
             element is removed from the queue, with its successor
             element (if any) being the least recently arrived element */

  public int peek();
    /* pre:  the queue is not empty
       post: the value of the element at the head of the queue is
             returned, and the queue is unchanged   */

  public int queueLength();
    /* post: the number of elements in the queue is returned */

}
