/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package MyTreeDT.source;



/**
 *
 * @author Ebenezer Ayo-Meti
 * comment: Wed - 21-Feb-2024
 * 
 * Continuation: Sun-26-May-2024
 * Continuation: Mon-27-May-2024
 * Continuation: Wed-29-May-2024
 * 
 * NOTES:
 * 1.   Started building the TreeDT
 * 2.   Implemented addition of new nodes to Tree, even addition of an array of data.
 * ##   These I did from Wed-21-Feb-2024 -- yes
 * 3.   Now, today writing this, I aim to finish the whole Tree Data Structure.
 * TODOS:
 *      ##  Considering that TreeDT is a Binary Search Tree -- and it is because
 *          each node can only have 0 or 2 children -- that's how I implemented
 *          the adding of data to each node. It legit starts from the left.
 *          *However* it does this non-recursively.
 *          It uses a queue DT and loops.
 *      1.  Implement Binary Search Tree functions from Lecture notes:
 *          The Depth-first search/traversal techniques:
 *          Pre-order traversal, Post-order traversal, In-order traversal
 *          All of this is recursive
 *          The TreeNodes are already done
 *          ***DONE***
 *      1B. Can't I use this recursive traversal form to add new nodes?
 *          Balance!
 *          I have the formula/code/algorithm to recursively do this.
 *          It makes use of the Height of the Tree structure.
 *          Since each node of a Binary Tree can either have a value or not have any...
 *          The Tree can always either be balanced or not.
 *          Generally, populating the tree starts first with the left branch and then ends toward
 *          the right branch, and pointer returns back to the root.
 *          #####
 *          SO, we did the algorithm based on this.
 *          ***DONE****
 *          
 *          
 *      2.  Implement the use of keys and numbering, because BSTs' nodes are ordered
 *          so that when searching from a target node, it is known which sub-tree to
 *          continue searching in.
 *          This way, the max number of comparisons on searching = height of tree
 *          This is hence the need of the `key-field` that must be unique and ordered, usually
 *          as a numerical (int) or alphanumerical/
 *          
 *          BST RULE:
 *              They are a special Binary Tree organised such that for each node, N, this rule applies:
 *                  If L is any node in the left sub-tree of N, then the value of L is less than N.
 *                  If R is any node in the right sub-tree of N, then the value of R is greater than N.
 *              So the operation of searching the BST can then be recursively expressed like this:
 *              while (key not found and more tree to search<node count number not reached>)
 *              {
 *                  if (key 'less than' current value)
 *                      search the left sub-tree
 *                  else
 *                      search the right sub-tree
 *              }
 *          @   Mon-27-May-2024
 *          The implementation is crazy easy! I can simply use postOrderTraversal
 *          to put the key numbers of each of them, just by incrementing by 1 from the left most node.
 *          I explain more where it's done!
 *          ***DONE***
 * 
 *      3.  Implement the small things like isEmpty(), isFull(), getHeight() -- addNode and deleteNode are
 *           by now
 *           ***DONE***
 *      4.  Finally, Add Node deletion. Wed-29-May-2024.
 *          ***DONE*** Thurs-30-May-2024
 */

/**
 * Date: Sun-26-May-2024
 * Added Ids to be integers not characters.
 * So that I can implement the Key-field thing.
 * But I leave the String character ids
 */
class TreeNode
{
    private int m_datum;
    private String m_id;
    //  To be implemented
    private int m_key;
    private boolean isSet = false;
    
    private TreeNode m_parent;
    private TreeNode m_leftChild;
    private TreeNode m_rightChild;
    
    public TreeNode(int datum, TreeNode parent, String id)
    {
        m_datum = datum;
        m_parent = parent;
        this.m_id = id;
        isSet = true;
    }
    
    public String getId()
    {
        return m_id;
    }
    public void updateKey(int newValue)
    {
        m_key = newValue;
    }
    
    public String getKey()
    {
        return Integer.toString(m_key);
    }
    public int getKeyVal()
    {
        return m_key;
    }
    
    public void setParent(TreeNode newParent)
    {
        m_parent = newParent;
    }
    
    
    public void setLeftChild(TreeNode newNode)
    {
        m_leftChild = newNode;
    }
    public void setRightChild(TreeNode newNode)
    {
        m_rightChild = newNode;
    }
    
    public boolean childrenAreSet()
    {
        //  Checks if this node's children have been set.
        //  Important in addNodeRecursive!
        return (m_leftChild != null && m_rightChild != null);
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
    
    public boolean isSet()
    {
        //  Just tells whether node has gotten data
        return isSet;
    }

    public boolean isFull()
    {
        return (getRightChild() != null && getLeftChild() != null);
    }
    public void printDatum()
    {
        System.out.println("Datum: " + m_datum + ", ID: " + m_id);
    }
    
    public boolean equals(TreeNode other)
    {
        boolean precon = this.m_datum == other.getDatum() && this.m_id.equals(other.getId());
        if (this.m_parent!=null)
            return precon && this.m_parent.equals(other.getParent());
        else
            return precon & this.m_parent==null && other.getParent()==null;
    }
    
    public boolean isLeaf()
    {
        return (m_leftChild == null && m_rightChild == null);
    }
    
    public void delete()
    {
        this.m_datum = 0;
        this.m_key = 0;
        System.out.println("Node id " + m_id + " deleted.");
        this.m_leftChild = null;
        this.m_rightChild = null;
        this.m_parent = null;
        this.m_id = null;
    }
    
    public void supplant(TreeNode targetNode)
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
 * 1.   Finished add node -- iteration version.
 * 2.   Added the Depth-First recursive Traversal techniques
 * 3.   Added recursive node addition technique along with keeping track of the Tree's height
 * 4.       #isEmpty to check for an empty tree
 *          # isFull to check for a full tree
 *          # getHeight to obtain the height of the tree
 *          # addNode to add a new node
 *          # deleteNode to remove a node
 *          * DONE
 * 5. DONE? PROBABLY APART FROM RECURSIVE ADD NODE
 */
class Tree
{
    public TreeNode root;
    private int binary_counter = 0;
//    private int call_counter = 0;
    private TreeNode current_node = null;
//    private TreeNodeInterface next_parent_node = null;
    private TreeNode current_parent_node = null;
//    private TreeNodeInterface previous_parent_node = null;
//    private TreeNodeInterface next_node;
    
    private String[] ids = {"A", "B", "C", "D", "E", "F", "G", "H", "I",
                            "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                            "S", "T", "U", "V", "W", "X", "Y", "Z"};
    //  For ids of nodes that have been deleted
//    private String[] idBank = new String[26];
    
    /*##    THE BELOW ARE USED IN THE addNodeRecursive METHOD   */
    //  idPointer is limited to 26 characters of the alphabet.
    //  Soon I will find a way to get random character sequences as the id
    //  for every added node
    //  ##  idCounter serves to count how many nodes are added.
    //  ##  It will be usd to get the tree's height, the maximum level of the tree
    private int idPointerNCounter = 0;
    //    The maximum level
    private int TreeHeight  = 0;
    private boolean balanced;
  
    
    
    public Tree(int rootData)
    {
        root = new TreeNode(rootData, null, ids[idPointerNCounter++]);
        current_node = root;
        current_parent_node = root;
        TreeHeight = 1;
        balanced = true;
//        next_parent_node = root;
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
    
    public int getTreeHeight()
    {
        return TreeHeight;
    }
    
    public boolean isEmpty()
    {
        return (idPointerNCounter == 0);
    }
    
    public boolean isFull()
    {
        //  basically checks if the current number of nodes
        //  is equal to the *max number of nodes at the current height*
        return (idPointerNCounter == power(2, TreeHeight) - 1);
    }
    
    /*##########################################################*/
    
    /*___________________DEPTH-FIRST TRAVERSALS___________________*/
    /**
        * This thing is coolade recursive! *bruh!*
        * It processes it's value first, goes to left child...
        * then left child processes its value and goes to its left child...
        * and does this until a leaf node is reached so that when it calls this
        * function again passing its null left child, because of the starting precondition
        * it returns back to that leaf parent. Then likewise for the right child.
        * Then when it has finished, that stack frame is popped, execution goes back to
        * the previous function executed by the previous node.
        * Then it follows this recursive way, and the automatic return when finished executing....
        * to go through every node.
        * This is the bases for all the Depth-First Traversals -- their only difference is when
        * they process their data, like printing it out.
        * 
    */
    public void preOrderTraversal(TreeNode thisNode)
    {
        if (thisNode == null) return;
        thisNode.whatAmI();
        preOrderTraversal(thisNode.getLeftChild());
        preOrderTraversal(thisNode.getRightChild());
    }// Ends the preOrderTraversal
      
    public void inOrderTraversal(TreeNode thisNode)
    {
        if (thisNode==null) return;
        thisNode.whatAmI();
        
        inOrderTraversal(thisNode.getRightChild());
    }   //  end inOrderTraversal
    
    public void postOrderTraversal(TreeNode thisNode)
    {
        if (thisNode==null) return;
        postOrderTraversal(thisNode.getLeftChild());
        postOrderTraversal(thisNode.getRightChild());
        thisNode.whatAmI();
    }   //  end postOrderTraversal
    /*############################################################*/
    
    
    
    /*_____________________ADD NODE__________________________*/
    public void addNode(int datum)
    {
        //  Every time this is called the binary_counter is incremented
        binary_counter += 1;
        if (binary_counter % 2 == 1)
            current_node.setLeftChild(new TreeNode(datum, current_parent_node, ids[idPointerNCounter++]));
           
        if (binary_counter % 2 == 0)
            current_node.setRightChild(new TreeNode(datum, current_parent_node, ids[idPointerNCounter++]));
         
        if (binary_counter == 2)
            binary_counter = 0;
        
        updateTreeHeight();
    }
    
    //  With this version, note that the tree must already have a root node data.
    public void addNodes(int[] data)
    {
        //  This queue was used to keep track of the tree traversal
        //  It was used to control the order at which nodes are added
        //  and what branches they were put in.
        /**
         * It is pretty cool when you see how it helps the algorithm :)
        */
        QueueGeneric<TreeNode> nodeQueue = new QueueGeneric(10);
        nodeQueue.enQueue(root);
        
        
        for (int datum : data)
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
                            current_node.setLeftChild(new TreeNode(datum, current_node, ids[idPointerNCounter++]));
                            nodeQueue.enQueue(current_node.getLeftChild());
                        }
                        break;
                    }
                    else if (binary_counter % 2 == 0)
                    {
                        if (current_node.getRightChild() == null)
                        {
                            current_node.setRightChild(new TreeNode(datum, current_node, ids[idPointerNCounter++]));
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
    
    public int addNodesRecursive(int[] data, TreeNode thisNode, int pointer)
    {
//        int dataAvailable = data.length;
//        pointer = data.length - data.length;
        
        //  Basically, dataAvailable keeps track of data there
        //  it is post decremented, so it first returns its value before decrementing
        //  So the first element is accessed at index zero, before dataAvailable decreases
        
        if (pointer < data.length)
        {
            if (thisNode.getLeftChild() == null)
                thisNode.setLeftChild(new TreeNode(data[pointer++],
                        thisNode, ids[idPointerNCounter++]));
            if (thisNode.getRightChild() == null)
                thisNode.setRightChild(new TreeNode(data[pointer++],
                        thisNode, ids[idPointerNCounter++]));
            
            updateTreeBalance();
            
            //  If the tree is not balanced and this node's children are set...
            if (balanced == false && thisNode.childrenAreSet() && !thisNode.equals(root))
                return pointer; //  Go back
           
//            int[] remainingData =  new int[data.length - pointer];
            //  .arraycopy(src, src_startpos, dest, dest_startpos, length_of_data);
//            System.arraycopy(data, data[pointer], remainingData, 0, data.length - pointer);
            pointer = addNodesRecursive(data, thisNode.getLeftChild(), pointer);
            pointer = addNodesRecursive(data, thisNode.getRightChild(), pointer);
            
//            remainingData =  new int[pointer];
//            System.arraycopy(data, data[pointer], remainingData, 0, data.length - pointer);
            addNodesRecursive(data, thisNode, pointer);
        }
        
        //  Just for the final stack frame at node A
        return 0;
    }
    /*####################################################################3*/
     
    
    /*______________ADDING_BINARY SEARCH TREE NODES' KEYS/IDS_______*/
    //  note that count is only added since it's recursive
    //  to keep each stack frame's count updated
    public int updateNodeKeys(TreeNode thisNode, int count)
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
    private boolean deleteLeafNode(String leafTargetId, TreeNode thisNode)
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
    private boolean isLeafNode(String targetId, TreeNode thisNode)
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
    private void deleteNodeNormal(String targetId, TreeNode thisNode)
    {
        //  1. *thisNode* is the starting node, normallly root.
        int binary_count =  0; //  2.
        //  Note can't use object instance in `.class` -- only class name
        MyStackDT<TreeNode> nodeStack = new MyStackDT(TreeNode[].class, 10);  //  3. Successfully initialised

        while(true)
        {
            binary_count += 1;
            
            //  This operation precondition is checked for every node in this Tree
            if (thisNode.getId().equals(targetId))
            {
                //  If thisNode has no left child but a right child
                if (thisNode.getLeftChild() == null && thisNode.getRightChild() != null)
                {
                    //  Checks if thisNode is the parent's left child
                    if (thisNode.getKeyVal() < thisNode.getParent().getKeyVal())
                    {
                        thisNode.getParent().setLeftChild(thisNode.getRightChild());   
                    }
                    else    //  If not then the right child
                    {
                        thisNode.getParent().setRightChild(thisNode.getRightChild());   
                    }
                }
                //  If thisNode has no right child but a left child
                else if (thisNode.getRightChild() == null && thisNode.getLeftChild() != null)
                {
                    //  Checks if thisNode is the parent's left child
                    if (thisNode.getKeyVal() < thisNode.getParent().getKeyVal())
                    {
                        thisNode.getParent().setLeftChild(thisNode.getLeftChild());   
                    }
                    else    //  If not then the right child
                    {
                        thisNode.getParent().setRightChild(thisNode.getLeftChild());   
                    }
                }
                else // It has both -- was called the tricky case -- not for me
                {
                    //  Find the right-most node of the left sub tree of the target (thisNode)
                    //  rightMostNode = thisNode.getLeftChild()
                    /*while (true)    //  Keep iterating through left subtree of target till...
                    {
                        //  The right most node (always a leaf) is found
                        if (rightMostNodeRef.isLeaf())
                        {
                            break;
                        }
                        rightMostNodeRef = rightMostNodeRef.getRightChild();
                    }*/
                    /*Chose to do it this way to find the right most of left subtree*/
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
                //  Get most recently added node for its turn for processing
                //  also, it's children will be added to the stack.
                
                thisNode = nodeStack.peek();
                nodeStack.pop();    //  remove it from stack since it's been gotten
            }
        }
    }
    /*___METHOD_2-Recursive__*/ 
    
    //  Recursive way to get the right-most node
    //  There ust always be a leaf node
    //  Thurs-30-May-2024
    //  turns out it's not to get the righ-most node as I thought.
    //  It's easily just the first right node of the left tree of the target.
    //  and if there is no right child of the starting node of the left sub-tree, that starting node is used.
    /*
    private TreeNode getRightMostNode(TreeNode thisNode)
    {
        if (thisNode.isLeaf())
            return thisNode;
        
        thisNode = getRightMostNode(thisNode.getRightChild());
        
        return thisNode;
    }
    */
    
    //  Preorder style, so it checks if current node is the target before traversing at all
    private boolean deleteNodeRecursive(String targetId, TreeNode thisNode)
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
    public void deleteNode(String targetId, Tree tree)
    {
//        TreeNode thisNodeRef = tree.root;
        if (isLeafNode(targetId, tree.root))
        {
            deleteLeafNode(targetId,  tree.root);
        }
        else
        {
            deleteNodeNormal(targetId,  tree.root);
//            deleteNodeRecursive(targetId, tree.root);
        }
        System.out.println("Node of ID " + targetId + " has been deleted.");
        updateNodeKeys(tree.root, 1);
    }
    
}

public class TreeDT {
    
    public static void main(String[] args)
    {
//        character A is less than B
//        System.out.println('A'<'B');
        
//        objectComparisonTest();
//        test1();
//        test2();
        
        //  Done: Mon-27-May-2024
//        testNormalNodeAdding();
//        testRecursiveNodeAdding();
//        testKeyUpdating();
//        test();
        
        testDeleting();
    }
    
    private static void testDeleting()
    {
        System.out.println("Date: Wed-29-May-2024\n");
        System.out.println("Deleting Nodes Normally: \n");
        Tree myTree = new Tree(23);
        int[] arr = {45, 72, 89, 10, 100, 77};
        System.out.println("\nBefore Deletion:\n");
        myTree.addNodesRecursive(arr, myTree.root, 0);
        myTree.updateNodeKeys(myTree.root, 1);
        myTree.postOrderTraversal(myTree.root);
        System.out.println("\nAfter Deletion:\n");
        //  Delete
        myTree.deleteNode("B", myTree);
        myTree.postOrderTraversal(myTree.root);
    }
    
    private static void testKeyUpdating()
    {
        System.out.println("Date: Mon-27-May-2024\n");
        System.out.println("Updating Tree's Nodes' Keys \n\n");
        Tree myTree = new Tree(23);
        int[] arr = {45, 72, 89, 10, 100, 77};
        myTree.addNodesRecursive(arr, myTree.root, 0);
        myTree.updateNodeKeys(myTree.root, 1);
        myTree.postOrderTraversal(myTree.root);
    }
    

    private static void testRecursiveNodeAdding()
    {
        System.out.println("Date: Mon-27-May-2024\n");
        System.out.println("Recursive Node Adding: \n\n");
        Tree myTree = new Tree(23);
        int[] arr = {45, 72, 89, 10, 100, 77};
        myTree.addNodesRecursive(arr, myTree.root, 0);
        myTree.postOrderTraversal(myTree.root);
    }
    
    private static void testNormalNodeAdding()
    {
        System.out.println("Date: Mon-27-May-2024\n");
        System.out.println("Normal Node Adding: \n\n");
        Tree myTree = new Tree(23);
        int[] arr = {45, 72, 89, 10, 100, 77};
        myTree.addNodes(arr);
//        myTree.root.getLeftChild().printDatum();
//        myTree.root.getLeftChild().getRightChild().printDatum();
//        myTree.root.getLeftChild().getLeftChild().printDatum();
//        myTree.root.getRightChild().printDatum();
//        myTree.root.getRightChild().getRightChild().printDatum();
//        myTree.root.getRightChild().getLeftChild().printDatum();
        myTree.postOrderTraversal(myTree.root);
    }
    
    
    private static void objectComparisonTest()
    {
        //  This does not work
        TreeNode node1 = new TreeNode(55, null, "ZED");
        TreeNode node2 = new TreeNode(23, null, "UMF");
        TreeNode node3 = new TreeNode(55, null, "ZED");
        System.out.println(node1 == node2);
        System.out.println(node1 == node3);
        
        //  This does
        System.out.println(node1.equals(node2));
        System.out.println(node1.equals(node3));
        
    }
    
    private static void test2()
    {   
        /*
            Indeed, you can assign the left and right children of a TreeNodeInterface to variables that reference it...
            rather than making a copy.
            So when I changed the Data in them, it indeed changed the actual data in the...
            left and right children respectively
        */
        Tree myTree = new Tree(54);
        myTree.addNode(60);
//        myTree.addNode(13);
        System.out.println(myTree.root.isFull());
        myTree.root.getLeftChild().printDatum();
//        myTree.root.getRightChild().printDatum();
        TreeNode ref1 = myTree.root.getLeftChild();
        ref1.changeDatum(35);
//        TreeNodeInterface ref2 = myTree.root.getRightChild();
//        ref2.changeDatum(77);
        myTree.root.getLeftChild().printDatum();
//        myTree.root.getRightChild().printDatum();
        
    }

    private static void test()
    {
        /*
            According to this test, I have found out that returning a member...
            from the getChild methods of the TreeNodeInterface returns a reference to it.
            So I did getLeftChild() and getRightChild and it gave me a reference to them...
            most likely because I did not assign it to a variable.
            But look at test2()
        */
        Tree myTree = new Tree(54);
        myTree.addNode(60);
//        myTree.addNode(13);
//        myTree.root.getLeftChild().printDatum();
//        myTree.root.getRightChild().printDatum();
//        myTree.root.getLeftChild().changeDatum(20);
//        myTree.root.getRightChild().changeDatum(7);
//        myTree.root.getLeftChild().printDatum();
//        myTree.root.getRightChild().printDatum();
        myTree.inOrderTraversal(myTree.root);
        
    }
}

