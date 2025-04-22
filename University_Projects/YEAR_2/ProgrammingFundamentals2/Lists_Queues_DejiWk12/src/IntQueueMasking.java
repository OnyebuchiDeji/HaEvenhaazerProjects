/**********************************************************
 * 
 * An implementation using cyclic-buffering with masking
 * 
 * 
 * ******************************************************/

public class IntQueueMasking implements QueueInterface {
  int arrayQueue[];
  int front, back;

  public IntQueueMasking(int queuesize)  {
    arrayQueue = new int[queuesize];
    front = 0;
    back = -1;
  }

  public boolean isFull(){
    return ( queueLength() == arrayQueue.length );
  } // end isFull

  public void enQueue( int element ){
    if ( isFull() )
      throw new QueueBoundaryException("Queue arrayQueue overflow");
    //  This is pre-incremented because when adding, the value needs to be added at the end
    arrayQueue[++back%arrayQueue.length] = element;
  } // end enQueue

  public int serve(){
    if ( isEmpty() )
      throw new QueueBoundaryException("Queue arrayQueue underflow");
    //  This is post-incremented because it removes the value at the current increments before incrementing...
    //  to make the pointer move to the next value.
    int val =  arrayQueue[front++%arrayQueue.length];
    arrayQueue[front-1] = 0;
    return val;
  } // end serve

  public boolean isEmpty() {
    return ( queueLength() == 0 );
  } // end isEmpty

  public int queueLength(){
      return (back - front + 1);
  } // end queueLength

  public int peek() {
    if ( isEmpty() )
      throw new QueueBoundaryException("Queue arrayQueue underflow");
    return arrayQueue[front];
  } // end peek

  public String displayQueue()  {
    int i = front;
    int printcount = 0;
    String buffer = "";
    
    while (printcount < queueLength())    {
      buffer = buffer + arrayQueue[i++%arrayQueue.length] + " ";
      printcount++;
    } // end while
    return buffer;
  } // end displayQueue
  
  public String displayArray()  {
    
    String buffer = "";
    
    for (int i=0; i < arrayQueue.length; i++)    {
      buffer = buffer + arrayQueue[i] + " ";
    } // end for i
    return buffer;
  } // end displayArray
  
} // end class IntQueueMasking
