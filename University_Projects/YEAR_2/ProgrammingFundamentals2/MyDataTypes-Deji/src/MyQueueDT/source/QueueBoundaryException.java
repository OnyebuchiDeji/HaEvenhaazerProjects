package MyQueueDT.source;

import java.lang.RuntimeException;

public class QueueBoundaryException extends RuntimeException{
    public QueueBoundaryException(String msg)
    {
        super(msg);
    }
}
