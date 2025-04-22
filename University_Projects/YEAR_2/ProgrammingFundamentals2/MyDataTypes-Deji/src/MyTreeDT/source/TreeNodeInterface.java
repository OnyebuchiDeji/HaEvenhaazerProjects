/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Interface.java to edit this template
 */
package MyTreeDT.source;

/**
 *
 * @author Ebenezer Ayo-Meti
 * @param <T>
 */

public interface TreeNodeInterface<T>
{ 
    public String getId();
    public void updateKey(int newValue);
    public String getKey();
    public int getKeyVal();
    public void setParent(TreeNodeInterface<T> newParent);
    public void setLeftChild(TreeNodeInterface<T> newNode);
    public void setRightChild(TreeNodeInterface<T> newNode);
    public boolean childrenAreSet();
    public TreeNodeInterface<T> getParent();
    public TreeNodeInterface<T> getLeftChild();
    public TreeNodeInterface<T> getRightChild();
    public void changeDatum(T newDatum);
    public T getDatum();
    public boolean isSet();
    public boolean isFull();
    public void printDatum();
    public boolean equals(TreeNodeInterface<T> other);
    public boolean isLeaf();
    public void delete();
    public void supplant(TreeNodeInterface<T> targetNode);
    public void whatAmI();
}
