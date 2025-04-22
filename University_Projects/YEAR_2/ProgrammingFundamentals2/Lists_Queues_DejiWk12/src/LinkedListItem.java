
/**********************************************************
 * A Linked List Item class.
 * 
 * @author Charles Day 
 * @version Feb 2003
 *********************************************************/
public class LinkedListItem {
  // instance variables
  private Object data;             // a "flexible" data area
  private LinkedListItem nextItem; // a reference to next item 

  // constructor: general items
  public LinkedListItem(Object dataObj, LinkedListItem restOfList) {
    data = dataObj;
    nextItem = restOfList;
  } // end constructor LinkedListItem

  // constructor: overloaded, ie used if 1st item in brand new list
  public LinkedListItem(Object dataObj) {
    this(dataObj, null); // invokes the general constructor above
  } // end constructor LinkedListItem

  public LinkedListItem getNext() {
    return nextItem;
  } // end getNext

  public void setNext(LinkedListItem nextOne) {
    nextItem = nextOne;
  } // end setNext

  public Object getValue() {
    return data;
  } // end getValue

  public void setValue(Object dataValue) {
    data = dataValue;
  } // end setValue

} // end class LinkedListItem
