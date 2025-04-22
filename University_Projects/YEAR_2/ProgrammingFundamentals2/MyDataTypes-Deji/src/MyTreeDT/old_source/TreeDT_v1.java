/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package MyTreeDT.old_source;

/**
 *
 * @author Ebenezer Ayo-Meti
 */

class TreeNode
{
    private int m_datum;
    
    private final TreeNode m_parent;
    private TreeNode m_leftChild;
    private TreeNode m_rightChild;
    
    public TreeNode(int datum, TreeNode parent)
    {
        m_datum = datum;
        m_parent = parent;
    }
    
    public void setLeftChild(TreeNode newNode)
    {
        m_leftChild = newNode;
    }
    public void setRightChild(TreeNode newNode)
    {
        m_rightChild = newNode;
    }
    public TreeNode getParent()
    {
        return m_parent;
    }
    public TreeNode getLeftChild()
    {
        return m_leftChild;
    }
    public TreeNode getRightChild()
    {
        return m_rightChild;
    }
    public void changeDatum(int newDatum)
    {
        m_datum = newDatum;
    }
    public int getDatum()
    {
        return m_datum;
    }
    public void printDatum()
    {
        System.out.println(m_datum);
    }
    
}


class Tree
{
    public TreeNode root;
    private int binary_counter = 0;
    private int call_counter = 0;
    private TreeNode current_node = null;
    private TreeNode next_parent_node = null;
    private TreeNode current_parent_node = null;
//    private TreeNode previous_parent_node = null;
//    private TreeNode next_node;
    
    public Tree(int rootData)
    {
        root = new TreeNode(rootData, null);
        current_node = root;
        current_parent_node = root;
        next_parent_node = root;
    }
    
    public void addNode(int datum)
    {
        //  Every time this is called the binary_counter is incremented
        binary_counter += 1;
        if (binary_counter % 2 == 1)
            current_node.setLeftChild(new TreeNode(datum, current_parent_node));
        if (binary_counter % 2 == 0)
            current_node.setRightChild(new TreeNode(datum, current_parent_node));
        if (binary_counter == 2)
            binary_counter = 0;
    }
    
    private TreeNode getNextNode()
    {
        /*
            This is where the tree traversal really takes place
            Every iteration, the call_counter for the getNextNode method is incremented.
        */
        call_counter += 1;
        TreeNode nextNode = null;
        //  W
        for (int count = 1; count <= call_counter; count++)
        {
            
        }
        
        return nextNode;
    }
    
    public void addNodes(int[] data)
    {

        for (int datum : data)
        {
            if (current_node == root)
            {
                addNode(datum);
            }
            else
            {
                //  current_node is the node to set the left and right children of
                //  It returns the next node to be added.
                //  Only when every two data is added, because each node requires two data...
                //  is when the next node is gotten
                if (binary_counter == 2)
                {
                    //  getNextNode() should return a reference to the next node
                    current_node = getNextNode();
                    binary_counter = 0;
                }
                addNode(datum);
            }
        }
    }
    
}

public class TreeDT_v1 {
    
    public static void main(String[] args)
    {
        test2();
    }
    
    public static void test()
    {
        /*
            According to this test, I have found out that returning a member...
            from the getChild methods of the TreeNode returns a reference to it.
            So I did getLeftChild() and getRightChild and it gave me a reference to them...
            most likely because I did not assign it to a variable.
            But look at test2()
        */
        Tree myTree = new Tree(54);
        myTree.addNode(60);
        myTree.addNode(13);
        myTree.root.getLeftChild().printDatum();
        myTree.root.getRightChild().printDatum();
        myTree.root.getLeftChild().changeDatum(20);
        myTree.root.getRightChild().changeDatum(7);
        myTree.root.getLeftChild().printDatum();
        myTree.root.getRightChild().printDatum();
        
    }
    
    public static void test2()
    {   
        /*
            Indeed, you can assign the left and right children of a TreeNode to variables that reference it...
            rather than making a copy.
            So when I changed the Data in them, it indeed changed.
        */
        Tree myTree = new Tree(54);
        myTree.addNode(60);
        myTree.addNode(13);
        myTree.root.getLeftChild().printDatum();
        myTree.root.getRightChild().printDatum();
        TreeNode ref1 = myTree.root.getLeftChild();
        ref1.changeDatum(35);
        TreeNode ref2 = myTree.root.getLeftChild();
        ref2.changeDatum(77);
        myTree.root.getLeftChild().printDatum();
        myTree.root.getRightChild().printDatum();
    }

}
