/* Example of creating own exceptions for ADT */

class QueueBoundaryException extends RuntimeException {
    
  public QueueBoundaryException(String message) {
    super(message);
  } // end constructor
  
} // end QueueBoundaryException
