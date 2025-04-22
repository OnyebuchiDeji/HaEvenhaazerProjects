/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Interface.java to edit this template
 */
package MyStackDT.source;

/**
 *
 * @author Ebenezer Ayo-Meti
 * @param <T>
 */
public interface StackInterface<T> {
    
    public void push(T datum);
    public void pop();
    public T peek();
    public boolean isEmpty();
    public boolean isFull();
    public int get_size();
    public int get_capacity();
    

}
