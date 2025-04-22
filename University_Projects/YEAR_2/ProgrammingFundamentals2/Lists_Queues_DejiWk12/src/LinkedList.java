/**********************************************************
 * A Linked List class.
 * 
 * @author Charles Day 
 * @version Feb 2003
 *********************************************************/
public class LinkedList {
    
  // instance variable for the list
  private LinkedListItem head;  

  // constructor List
  public LinkedList(){
    head = null;
  } // end constructor 

  // Count the number of items in the list
  public int size() {
    int count = 0;
    LinkedListItem currItem = head;
    while (currItem != null) {
      count++;
      currItem = currItem.getNext();
    } // end while
    return count;
  } // end size
  
  public int rSize() {
    return ( recursiveSize(head) );
  } // end rSize
  public int recursiveSize(LinkedListItem ci) {
    if (ci == null) return 0;
    else return ( 1 + recursiveSize(ci.getNext()) );
  } // end recursiveSize
  
  // Bad, bad, bad! Utility method - just for testing.
  public void displayList() {
    
    LinkedListItem currItem = head;
    while (currItem != null) {
      System.out.println("item contains = " + currItem.getValue() );
      currItem = currItem.getNext();
    } // end while
    
  } // end displayList
  
  // Add newData to the tail 
  public void addToTail(Object newData) {
    
    LinkedListItem prevItem = null, currItem = head;
    while (currItem != null) {
      /* Missing Line 1 Added: Fri-19-Jan-2024*/ 
      prevItem = currItem;
      currItem = currItem.getNext();
      /*
        How it works is this:
        the loop keeps hoing forward, traversing the linked list...
        it sets the prevItem to be the currentItem and the currentItem changes to the nextItem...
        this it does so that when the prevItem is one Item before the end of the list...
        it gives the prevItem its value, and then on calling.getNext() becomes null...
        and before the following iteration can occur, since currItem becomes null, it stops
      */
    } // end while
    
    //  This part of the code was added because the above implementation was not made...
    //  It was so that if prevItem remains null, it just calls the addToHead() method...
    //  which is almost like this addToTail method
    if (prevItem == null) addToHead(newData);
    else {
      LinkedListItem temp = new LinkedListItem(newData);
      prevItem.setNext(temp);
      }
    
  } // end addToTail
  
  // Assumes list is not empty to start with
  public Object removeFromTail() {
    
    LinkedListItem prevItem = null, currItem = head;
    while (currItem.getNext() != null) {
      prevItem = currItem;
      currItem = currItem.getNext();
    } // end while
    
    if (prevItem == null) removeFromHead();
    else {
      prevItem.setNext(null);
    } // end else
    
    return currItem.getValue();
    
  } // end removeFromTail
  
  // Assumes list has at least itemNo elements
  public Object removeItem( int itemNo) {
    
    int count = 1;
    LinkedListItem prevItem = null, currItem = head;
    while (count < itemNo) {
      count++;
      prevItem = currItem;
      currItem = currItem.getNext();
    } // end while
    
    prevItem.setNext( currItem.getNext() );
    
    return currItem.getValue();
    
  } // end removeItem
  
  // Assumes list has at least itemNo elements
  public void insertItem(Object newData, int itemNo) {
    
    int count = 1;
    LinkedListItem prevItem = null, currItem = head;
    
    while (count < itemNo) {
      count++;
      prevItem = currItem;
      currItem = currItem.getNext();
    } // end while
    
    prevItem.setNext( new LinkedListItem(newData, currItem) );
  
  } // end insertItem

  public boolean isEmpty() {
    return ( size() == 0 );
  } // end isEmpty

  public void addToHead(Object data) {
    /*
      Deji Comments
      This implementation utilized the LinkedListItems' function...
      to be able to store the next item of data in their netItem member variable.
      That is why the below code is enough to store all the data
    */
    head = new LinkedListItem(data, head);
  } // end addToHead

  public Object removeFromHead() {
    LinkedListItem tempItem = head;
    head = head.getNext();
    return tempItem.getValue();
  } // removeFromHead


} // end class LinkedList
