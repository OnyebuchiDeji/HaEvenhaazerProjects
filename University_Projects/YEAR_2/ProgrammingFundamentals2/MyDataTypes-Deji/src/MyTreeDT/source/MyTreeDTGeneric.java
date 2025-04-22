/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package MyTreeDT.source;

/**
 *
 * @author Ebenezer Ayo-Meti
 * 
 * This work consists of the implementation of the tree data type...
 * specifically, binary trees. So though I don't call them binary trees...
 * or binary tree nodes, that is exactly what they are.
 */

/**
 * Date: Sun-26-May-2024
 * 
 * Note that the order in which the methods are defined in an 
 * interface being implemented need to be the same in the class that implements
 * it, lest it says it could not find that interface -- SIGNATURE IS IMPORTANT
 * 
 * DONE: Thurs-30-May-2024
 * 
 * Date: thurs-30-May-2024
 * 
 * 1.   Fixed addRecursive -- was issue with delete
 * 2.   Finished implementing deleting nodes -- Fri-31-May-2024
 * 
 */

import java.lang.reflect.Array;
import java.util.Arrays;
import java.lang.SuppressWarnings;

class TreeNodeStruct<T> implements TreeNodeInterface<T>
{
    private T m_datum;
    private String m_id;
    private int m_key;
    private boolean isSet = false;
    
    private TreeNodeInterface<T> m_parent;
    private TreeNodeInterface<T> m_leftChild;
    private TreeNodeInterface<T> m_rightChild;
    
    public TreeNodeStruct(T datum, TreeNodeInterface<T> parent, String id)
    {
        m_parent = parent;
        m_datum = datum;
        this.m_id = id;
        isSet = true;
    }
    
    @Override
    public String getId()
    {
        return m_id;
    }
    
    @Override
    public void updateKey(int newValue)
    {
        m_key = newValue;
    }
    
    @Override
    public String getKey()
    {
        return Integer.toString(m_key);
    }
    @Override
    public int getKeyVal()
    {
        return m_key;
    }
    
    @Override
    public void setParent(TreeNodeInterface<T> newParent)
    {
        m_parent = newParent;
    }
    
    @Override
    public void setLeftChild(TreeNodeInterface<T> newNode)
    {
        m_leftChild = newNode;
    }
    @Override
    public void setRightChild(TreeNodeInterface<T> newNode)
    {
        m_rightChild = newNode;
    }
    
    @Override
    public boolean childrenAreSet()
    {
        //  Checks if this node's children have been set.
        //  Important in addNodeRecursive!
        return (m_leftChild != null && m_rightChild != null);
    }
    
    @Override
    public TreeNodeInterface getParent()
    {
        return m_parent;
    }
    
    @Override
    public TreeNodeInterface getLeftChild()
    {
        return m_leftChild;
    }
    
    @Override
    public TreeNodeInterface getRightChild()
    {
        return m_rightChild;
    }
    
    @Override
    public void changeDatum(T newDatum)
    {
        m_datum = newDatum;
    }
    
    @Override
    public T getDatum()
    {
        return m_datum;
    }
    
    @Override
    public boolean isSet()
    {
        return isSet;
    }

    @Override
    public boolean isFull()
    {
        return (getRightChild() != null && getLeftChild() != null);
    }
    
    @Override
    public void printDatum()
    {
        System.out.println("Datum: " + m_datum + ", ID: " + m_id);
    }
    
    @Override
    public boolean equals(TreeNodeInterface<T> other)
    {
        boolean precon = this.m_datum == other.getDatum() && this.m_id.equals(other.getId());
        if (this.m_parent!=null)
            return precon && this.m_parent.equals(other.getParent());
        else
            return precon & this.m_parent==null && other.getParent()==null;
    }
    
    @Override
    public boolean isLeaf()
    {
        return (m_leftChild == null && m_rightChild == null);
    }

    @Override
    public void delete()
    {
        this.m_datum = null;
        this.m_key = 0;
        System.out.println("Node id " + m_id + " deleted.");
        this.m_leftChild = null;
        this.m_rightChild = null;
        this.m_parent = null;
        this.m_id = null;
    }
    
    @Override
    public void supplant(TreeNodeInterface<T> targetNode)
    {
        /**
         * Note, only parent, children and key value are changed!
         */
        
        //  This is for a supplanter node that is chosen because there is no right-most of the left sub tree, just left
        //  Since it's parent is the target, it's parent loses reference to it
        if (targetNode.getLeftChild().getId().equals(this.m_id))
        {
            //  Take target's right child since I'm the left child
            this.setRightChild(targetNode.getRightChild());
            //  Make it's parent make me it's left child
            targetNode.getParent().setLeftChild(this);
            //  Make it's right child make me it's parent
            targetNode.getRightChild().setParent(this);
            this.m_parent = targetNode.getParent();   //  replace this node's parent with that of the supplanted
        }
        //  For a right child, because target didn't have a left subtree
        //  this is for a supplanter node chosen because there is no right-most node of the right subtree, just the starting node.
        //  Note the target has no left subtree (which is not possible in my Binary Tree implementation (filling of nodes starts from left)
        //  ...unless deleted
        //  Also, since it's parent is the target, it's parent loses reference to it
        else if(targetNode.getRightChild().getId().equals(this.m_id))
        {
//            this.setLeftChild(targetNode.getLeftChild());
            targetNode.getParent().setRightChild(this); //  only this.
//            targetNode.getLeftChild().setParent(this);    // no need since it has no left tree
            this.m_parent = targetNode.getParent();   //  replace this node's parent with that of the supplanted
        }
        //  This is for supplanters which are the rightmost node of the left subtree of target
        //  hence the supplanter's key's value is less than the target's
        else if(targetNode.getKeyVal() > this.m_key)
        {
            this.setRightChild(targetNode.getRightChild());
            this.setLeftChild(targetNode.getLeftChild());
            targetNode.getParent().setLeftChild(this);
            targetNode.getRightChild().setParent(this);
            targetNode.getLeftChild().setParent(this);
            //  Remove it's parent's reference from it.
            //  Since it's always the right child
            this.m_parent.setRightChild(null);
            this.m_parent = targetNode.getParent();   //  replace this node's parent with that of the supplanted
        }
        //  This is for supplanters which are the rightmost node of the right subtree of target because there's no left subtree
        //  hence the supplanter's key's value is greater than the target's
        else if(targetNode.getKeyVal() < this.m_key)
        {
            this.setLeftChild(targetNode.getLeftChild());
            this.setRightChild(targetNode.getRightChild());
            targetNode.getParent().setRightChild(this);
            targetNode.getLeftChild().setParent(this);
            targetNode.getRightChild().setParent(this);
            //  Remove it's parent's reference from it.
            //  Since it's always the right child
            this.m_parent.setRightChild(null);
            this.m_parent = targetNode.getParent();   //  replace this node's parent with that of the supplanted
        }
    }
    @Override
    public void whatAmI()
    {
        System.out.println("ID: " + m_id);
        System.out.println("Key: " + m_key);
        System.out.println("Datum: " + m_datum);
        if (m_parent != null)
            System.out.println("\tParent: " + (Object)(m_parent.getId()));
        if (m_leftChild!= null)
            System.out.println("\tleftChild: " + (Object)m_leftChild.getId());
        if (m_rightChild!=null)
            System.out.println("\trightChild: " + (Object)m_rightChild.getId());
        if (m_parent == null && m_leftChild == null && m_rightChild == null)
        {
            System.out.println("\tParent: " + null);
            System.out.println("\tleftChild: " + null);
            System.out.println("\trightChild: " + null);
        }
    }
}

/**
 * Comment Date: Thurs-30-May-2024
 * Note that though the members' types is the
 * `TreeNodeInterface<T>` intergace, these members can be initialised
 * with TreeNodeStruct objects, because they implment this interface
 * 
 */
public class MyTreeDTGeneric<T> implements TreeInterface<T>
{
    private TreeNodeInterface<T> root;
    private TreeNodeInterface<T> current_node = null;
    private TreeNodeInterface<T> current_parent_node = null;
    private int binary_counter = 0;
    
    //  Stores the type of this object
//    private Class<T> type_info;
    
    private String[] ids = {"A", "B", "C", "D", "E", "F", "G", "H", "I",
                            "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                            "S", "T", "U", "V", "W", "X", "Y", "Z"};
    private int idPointerNCounter = 0;
    //  The maximum level
    private int TreeHeight = 0;
    private boolean balanced;
    
    public MyTreeDTGeneric(T rootData)
    {
        root = new TreeNodeStruct<>(rootData, null, ids[idPointerNCounter++]);
        current_node = root;
        current_parent_node = root;
        balanced = true;
        TreeHeight = 1;
//        type_info = root.class;
    }
    
    private int power(int base, int exponent)
    {
        if (exponent == 0)
            return 1;
        
        int res = 1;
        for (int i = 1; i <= exponent; ++i)
        {
            res *= base;
        }
        return res;
    }
    
    private void updateTreeBalance()
    {
        /**
         * Also uses the number of nodes added `idPointerNCounter`
         * It checks whether a Tree is balanced at its given height
         * by checking if the current number of nodes is equal or less than 
         * the max possible number of nodes at that height.
        */
        //  Basically, this is the max number of nodes
        //  that a balanced tree can have at that height
        int maxPossibleNumOfNodes = power(2, TreeHeight) - 1;
        balanced = idPointerNCounter == maxPossibleNumOfNodes;
    }
    
    @Override
    public void updateTreeHeight()
    {
        /**
         * It automatically takes into account whether a node was added or not
         * since it uses the `isPointerNCounter`
         */
        //  initial Height or level -- height is max level at that time
        int initialHeight = TreeHeight;
        int twoPowerVal = power(2, initialHeight);
        if (idPointerNCounter >= twoPowerVal)
            TreeHeight += 1;
    }
    
    @Override
    public int getTreeHeight()
    {
        return TreeHeight;
    }
    
    @Override
    public boolean isEmpty()
    {
        return (idPointerNCounter == 0);
    }
    
    @Override
    public boolean isFull()
    {
        return (idPointerNCounter == power(2, TreeHeight) - 1);
    }
    
    /*___________________DEPTH-FIRST TRAVERSALS___________________*/
    @Override
    public void preOrderTraversal(TreeNodeInterface<T> thisNode)
    {

        if (thisNode == null) return;
        thisNode.whatAmI();
        preOrderTraversal(thisNode.getLeftChild());
        preOrderTraversal(thisNode.getRightChild());
    }// Ends the preOrderTraversal
      
    @Override
    public void inOrderTraversal(TreeNodeInterface<T> thisNode)
    {
        if (thisNode==null) return;
        inOrderTraversal(thisNode.getLeftChild());
        System.out.println("ID: " + thisNode.getId() + ", Key: " + thisNode.getKey() + ", Value: " + thisNode.getDatum());
        thisNode.whatAmI();
        inOrderTraversal(thisNode.getRightChild());
    }   //  end inOrderTraversal
    
    @Override
    public void postOrderTraversal(TreeNodeInterface<T> thisNode)
    {
        if (thisNode==null) return;
        postOrderTraversal(thisNode.getLeftChild());
        postOrderTraversal(thisNode.getRightChild());
        thisNode.whatAmI();
    }   //  end postOrderTraversal
    /*############################################################*/
    
    
    /*_____________________ADD NODE__________________________*/
    @Override
    public void addNode(T datum)
    {
        //  Every time this is called the binary_counter is incremented
        binary_counter += 1;
        if (binary_counter % 2 == 1)
            current_node.setLeftChild(new TreeNodeStruct<>(datum, current_parent_node, ids[idPointerNCounter++]));
           
        if (binary_counter % 2 == 0)
            current_node.setRightChild(new TreeNodeStruct<>(datum, current_parent_node, ids[idPointerNCounter++]));
         
        if (binary_counter == 2)
            binary_counter = 0;
        
        updateTreeHeight();
    }
    
    //  With this version, note that the tree must already have a root node data.
    @Override
    public void addNodes(T[] data)
    {
        //  This queue was used to keep track of the tree traversal
        //  Comment date: Thurs-30-May-2024
        QueueGeneric<TreeNodeInterface<T>> nodeQueue = new QueueGeneric(10);
        nodeQueue.enQueue(root);
        
        
        for (T datum : data)
        {
            binary_counter += 1;
            while (true)
            {
                if (!current_node.isFull())
                {
                    if (binary_counter % 2 == 1)
                    {
                        if (current_node.getLeftChild()== null)
                        {
                            current_node.setLeftChild(new TreeNodeStruct(datum, current_node, ids[idPointerNCounter++]));
                            nodeQueue.enQueue(current_node.getLeftChild());
                        }
                        break;
                    }
                    else if (binary_counter % 2 == 0)
                    {
                        if (current_node.getRightChild() == null)
                        {
                            current_node.setRightChild(new TreeNodeStruct(datum, current_node, ids[idPointerNCounter++]));
                            nodeQueue.enQueue(current_node.getRightChild());
                        }
                        break;
                    }
                    //  This is meant to be outside the while loop within the for loop
                    if (binary_counter == 2)
                    {
                        binary_counter = 0;
                    }
                }
                else
                {
                    //  Remove the first node to be put in
                    System.out.println("Served: " + nodeQueue.serve());
                    //  Make current node the next
                    current_node = nodeQueue.peek();
//                  break;
                }
            }   
        }
    }
    
    

    /*__________________RECURSIVE NODE ADDITION______________________*/
    /**
     * Note that, unlike the iteration-based `addNode` and `addNodes`...
     * this one does not use the member pointers for current_node and such...
     * of this Tree Datatype.
     * It starts with a reference from what node to start from
     */
    
    @Override
    public int addNodesRecursive(T[] data, TreeNodeInterface<T> thisNode, int pointer)
    {
        boolean done = false;
        if (pointer < data.length)
        {
            if (!thisNode.childrenAreSet())
            {
                if (thisNode.getLeftChild() == null && pointer < data.length)
                    thisNode.setLeftChild(new TreeNodeStruct<>(data[pointer++],
                            thisNode, ids[idPointerNCounter++]));
                else
                    return pointer;
                if (thisNode.getRightChild() == null && pointer < data.length)
                    thisNode.setRightChild(new TreeNodeStruct<>(data[pointer++],
                            thisNode, ids[idPointerNCounter++]));
                else
                    return pointer;
                //  Hence done can only be true if the node previously did
                //  not have its children set
                done = true;
            }
            
            updateTreeBalance();
            updateTreeHeight();
            
            //  If the tree is not balanced and this node's children are set...
            if (done == true && thisNode.childrenAreSet() && !thisNode.equals(root))
                return pointer; //  Go back
           

            pointer = addNodesRecursive(data, thisNode.getLeftChild(), pointer);
            pointer = addNodesRecursive(data, thisNode.getRightChild(), pointer);
            
            addNodesRecursive(data, thisNode, pointer);
        }
        
        //  Just for the final stack frame at node A
        return pointer;
    }
    /*####################################################################3*/
     
    
    /*______________ADDING_BINARY SEARCH TREE NODES' KEYS/IDS_______*/
    //  note that count is only added since it's recursive
    //  to keep each stack frame's count updated
    @Override
    public int updateNodeKeys(TreeNodeInterface<T> thisNode, int count)
    {
        /**
         * This uses in-order traversal. -- it's recursive
         * Note that it runs through every node in the tree so
         * each of their keys are updated when something is added.
         * 
         * Pree that it has to return the count value so that when, for example...
         * the left branch of the root is done, the current node can get the
         * up to date count value and the right branch can have the up to date count value also.
        */
        if (thisNode == null) return count; //  Returns count
        
        //  As long as count is not greater than the number of added nodes.
        if (count <= idPointerNCounter)
        {
            count = updateNodeKeys(thisNode.getLeftChild(), count);
            thisNode.updateKey(count++);    //  Only incremented when key is updated
            count = updateNodeKeys(thisNode.getRightChild(), count);
        }
        
        return count;
    }
    
    /*###############################################################*/
    
    
    /*_________________DELETING NODES________________*/
    /*  To delete a node,  remove all its data, id, and key, and remove parent's....
        reference from it, and any child referencing it.
    
        Used inOrderTraversal because if the left branch finds and deletes,
        the whole things hsould stop.
        Wed-29-May-2024
        Changed to PREORDER TRAVERSAL so that if the current node is the target...
        it immediately returns without needing to finish traversing the left sutree
        as in inOrderTraversal.
    */
    
    /*  _____________DELETING_LEAF_NODE___________
        For leaf node with no children, there is no need to rearrange
      also only it's parents are removed, and its data is destroyed
      Just call its delete method
    */
    private boolean deleteLeafNode(String leafTargetId, TreeNodeInterface<T> thisNode)
    {
        /**
         *  Yo, immediately the node is deleted, its done
         */
        boolean deleted = false;
        //  UsesinOrderTraversal
        if (thisNode == null) return false;

        //  Comparing Strings
        if (thisNode.getId().equals(leafTargetId))
        {
            thisNode.delete();
            deleted = true;
            return deleted;
        }
        
        deleted = deleteLeafNode(leafTargetId, thisNode.getLeftChild());
        if (!deleted)
            deleted = deleteLeafNode(leafTargetId, thisNode.getRightChild());
        
        return deleted == true;
    }
    /* __________FINDING_LEAF_NODE_________________
        Always pass in starting or root node
      This uses inOrder and once leaf is found, return boolean
    */
    private boolean isLeafNode(String targetId, TreeNodeInterface<T> thisNode)
    {
        boolean found = false;
        //  UsesinOrderTraversal
        if (thisNode == null) return false;

        //  Comparing Strings
        if (thisNode.getId().equals(targetId) && thisNode.isLeaf())
        {
            return true;
        }
        
        found = isLeafNode(targetId, thisNode.getLeftChild());
        if (!found)
            found = isLeafNode(targetId, thisNode.getRightChild());
        
        return found == true;
    }
    //    #########################################
    
    /*__METHOD_1-Iterative__*/
      /*
        Different from my recursive method of adding data to nodes iteratively
          1. This uses a stack data type. The stack datatype is suitable in keeping track of which
              Node to travrse next
          2.  This uses non-members to keep track of states
          Note that because this method uses a stack dt, though all nodes are successfully traversed
          It traverses the tree from the right branch rather from the left branch
          though I can reverse this b making the right branch nodes to be added to the stack first,
          controlled by the `binary_count` variable and the conditionals.
          IN FACT, TO KEEP CONSISTENCY, I DO THAT.
       */
    private void deleteNodeNormal(String targetId, TreeNodeInterface<T> thisNode)
    {
        //  1. *thisNode* is the starting node, normallly root.
        int binary_count =  0; //  2.
        //  Note can't use object instance in `.class` -- only class name
        MyStackDT<TreeNodeInterface<T>> nodeStack = new MyStackDT(TreeNodeStruct[].class, 10);  //  3. Successfully initialised

        while(true)
        {
            binary_count += 1;
            
            //  This operation precondition is checked for every node in this Tree
            if (thisNode.getId().equals(targetId))
            {
                //  If thisNode has a left child (left subtree) but no right subtree
                if (thisNode.getLeftChild() != null && thisNode.getRightChild() == null)
                {
                    if (thisNode.getLeftChild().getRightChild() != null)   //  If the left subtree has a right node
                        thisNode.getLeftChild().getRightChild().supplant(thisNode);
                    else if (thisNode.getLeftChild().getLeftChild() != null)   //  If it doesn't, take available node
                        thisNode.getLeftChild().getLeftChild().supplant(thisNode);
                    else    //  If neither, it means the left subtree starting node is the node to work on
                    {       //  according to lecture examples
                        thisNode.getLeftChild().supplant(thisNode);  //  according to lecture examples
                    }
                    thisNode.delete();
                    break;
                }
                //  If thisNode has a right child (right subtree) but no left subtree
                else if (thisNode.getRightChild() != null && thisNode.getLeftChild() == null)
                {
                    if (thisNode.getRightChild().getRightChild() != null)   //  If the left subtree has a right node
                        thisNode.getRightChild().getRightChild().supplant(thisNode);
                    else if (thisNode.getRightChild().getLeftChild() != null)   //  If it doesn't, take available node
                        thisNode.getRightChild().getLeftChild().supplant(thisNode);
                    else    //  If neither, it means the left subtree starting node is the node to work on
                    {       //  according to lecture examples
                        thisNode.getRightChild().supplant(thisNode);  //  according to lecture examples
                    }
                    thisNode.delete();
                    break;
                }
                else    // It has both -- was called the tricky case -- not for me
                {       //  that is, has a both left and right subtree
                    
                    /*Chose to do it this way to find the right-most of left subtree*/
                    //  Now update information by supplanting.
                    //  Note that these objects keep references -- copies are shallow
                    if (thisNode.getLeftChild().getRightChild() != null)   //  If the left subtree has a right node
                        thisNode.getLeftChild().getRightChild().supplant(thisNode);
                    else if (thisNode.getLeftChild().getLeftChild() != null)   //  If it doesn't, take available node
                        thisNode.getLeftChild().getLeftChild().supplant(thisNode);
                    else    //  If neither, it means the left subtree starting node is the node to work on
                    {       //  according to lecture examples
                        thisNode.getLeftChild().supplant(thisNode);  //  according to lecture examples
                    }
                    thisNode.delete();
                    break;
                }
                
            }
            
            if (binary_count % 2 == 1 && thisNode.childrenAreSet())
            {
                nodeStack.push(thisNode.getRightChild());
            }
            else if (binary_count % 2 == 0 && thisNode.childrenAreSet())
            {
                nodeStack.push(thisNode.getLeftChild());
            }
            
            if (binary_count == 2)
            {
                binary_count = 0;
                thisNode = nodeStack.pop();
            }
        }
    }
    /*___METHOD_2-Recursive__*/
    
    //  Preorder style, so it checks if current node is the target before traversing at all
    private boolean deleteNodeRecursive(String targetId, TreeNodeInterface<T> thisNode)
    {
        boolean deleted = false;
        if (thisNode == null) return false;
        
        
        //  Process first
        if (thisNode.getId().equals(targetId))
        {
            //  getRightMostNode(thisNode.getLeftChild()).supplant();
            if (thisNode.getLeftChild().getRightChild() != null)   //  If the left subtree has a right node
                thisNode.getLeftChild().getRightChild().supplant(thisNode);
            else if (thisNode.getLeftChild().getLeftChild() != null)   //  If it doesn't, take available node
             thisNode.getLeftChild().getLeftChild().supplant(thisNode);
            else    //  If neither, it means the left subtree starting node is the node to work on
                thisNode.getLeftChild().supplant(thisNode);  //  according to lecture examples
            
            thisNode.delete();
            deleted = true;
            return deleted;
        }
                
        deleted = deleteNodeRecursive(targetId, thisNode.getLeftChild());
        if (!deleted)
            deleted = deleteNodeRecursive(targetId, thisNode.getRightChild());
        
        return deleted == true;
    }
    
    //  Wed-29-May-2024
    @Override
    public void deleteNode(String targetId)
    {
//        TreeNode thisNodeRef = tree.root;
        if (isLeafNode(targetId, root))
        {
            deleteLeafNode(targetId,  root);
        }
        else
        {
            deleteNodeNormal(targetId,  root);
//            deleteNodeRecursive(targetId, root);
        }
        System.out.println("Node of ID " + targetId + " has been deleted.");
        updateNodeKeys(root, 1);
    }
    
    
    public static void main(String[] args)
    {
        test1();
    }
    
    private static void test1()
    {
        System.out.println("Date: Wed-29-May-2024\n");
        System.out.println("Deleting Nodes Normally: \n");
        MyTreeDTGeneric myTree = new MyTreeDTGeneric("Start");
        String[] arr = {"I", "will", "love you", "forever", "my", "heart", "is", "with", "you"};
        System.out.println("\nBefore Deletion:\n");
//        myTree.addNodesRecursive(arr, myTree.root, 0);
        myTree.addNodes(arr);
        myTree.updateNodeKeys(myTree.root, 1);
        myTree.preOrderTraversal(myTree.root);
        System.out.println("\nAfter Deletion:\n");
        //  Delete
        myTree.deleteNode("B");
        myTree.preOrderTraversal(myTree.root);
    }
}

