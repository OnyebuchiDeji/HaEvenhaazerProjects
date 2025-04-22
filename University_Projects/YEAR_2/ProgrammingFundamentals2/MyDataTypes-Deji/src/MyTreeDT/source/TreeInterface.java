/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Interface.java to edit this template
 */
package MyTreeDT.source;

/**
 *
 * @author Ebenezer Ayo-Meti
 * created: Thurs-25-10-2024
 * @param <T>
 *
 */


        
public interface TreeInterface<T>
{
    public void updateTreeHeight();
    public int getTreeHeight();
    public boolean isEmpty();
    public boolean isFull();
    public void preOrderTraversal(TreeNodeInterface<T> thisNode);
    public void inOrderTraversal(TreeNodeInterface<T> thisNode);
    public void postOrderTraversal(TreeNodeInterface<T> thisNode);
    public void addNode(T datum);
    public void addNodes(T[] data);
    public int addNodesRecursive(T[] data, TreeNodeInterface<T> thisNode, int pointer);
    public int updateNodeKeys(TreeNodeInterface<T> thisNode, int count);
    public void deleteNode(String targetId);
}
