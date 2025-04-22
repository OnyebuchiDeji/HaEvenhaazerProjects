/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Ebenezer Ayo-Meti
 * 
 * Date: Thurs-3-May-2024
 * DONE!!!
 * Finished lectures 14-20, except B-Trees (Bayer & MCreight)
 *      almost done with Tree node deletion.
 * Done:
 *      1. expression Tree, Queue, and Stack
 *      2. expression evaluation from infix to postfix...
 *      3. postfix to expression tree.
 *      4.  Expression tree back to infix (evaluation)
 *      5.  Finally, evaluating numeric expression from string.
 *              even implemented two methods: The normal one and stack one
 * 
 */
import java.util.Arrays;

class TreeNode<T>
{
//    private String m_name;
    private T m_datum = null;
    private TreeNode<T> m_parent;
    private TreeNode<T> m_leftChild;
    private TreeNode<T> m_rightChild;
    
    public TreeNode(T datum)
    {
        m_datum = datum;
//        class_type = new Class<T>();
    }
    public TreeNode(T datum, TreeNode<T> left, TreeNode<T> right)
    {
        m_datum = datum;
        m_leftChild = left;
        m_rightChild = right;
        //  Set the child to know who their parent is
        m_leftChild.setParent(this);
        m_rightChild.setParent(this);
    }
    public TreeNode(T datum, T leftChildDatum, T rightChildDatum)
    {
        m_datum = datum;
        m_leftChild = new TreeNode<>(leftChildDatum);
        m_rightChild = new TreeNode<>(rightChildDatum);
        //  Set the child to know who their parent is
        m_leftChild.setParent(this);
        m_rightChild.setParent(this);
    }
    
    public boolean isSet()
    {
        return m_datum == null;
    }
    
    public void set(TreeNode<T> node)
    {
        m_datum = node.getDatum();
        m_parent = node.getParent();
        m_leftChild = node.getLeftChild();
        m_rightChild = node.getRightChild();
        //  Set the child to know who their parent is
        m_leftChild.setParent(this);
        m_rightChild.setParent(this);
    }
    
    public void setParent(TreeNode<T> newNode)
    {
        m_parent = newNode;
    }
    
    public void setLeftChild(TreeNode<T> newNode)
    {
        m_leftChild = newNode;
    }
    public void setRightChild(TreeNode<T> newNode)
    {
        m_rightChild = newNode;
    }
    public TreeNode<T> getParent()
    {
        return m_parent;
    }
    public TreeNode<T> getLeftChild()
    {
        return m_leftChild;
    }
    public TreeNode<T> getRightChild()
    {
        return m_rightChild;
    }
    
    public T getDatum()
    {
        return m_datum;
    }
    
    public boolean isLeaf()
    {
        return (m_leftChild == null && m_rightChild == null);
    }
    
    public void whatAmI()
    {
        System.out.println("Datum: " + m_datum);
        if (m_parent != null)
            System.out.println("\tParent: " + (Object)(m_parent.getDatum()));
        if (m_leftChild!= null)
            System.out.println("\tleftChild: " + (Object)m_leftChild.getDatum());
        if (m_rightChild!=null)
            System.out.println("\trightChild: " + (Object)m_rightChild.getDatum());
        if (m_parent == null && m_leftChild == null && m_rightChild == null)
        {
            System.out.println("\tParent: " + null);
            System.out.println("\tleftChild: " + null);
            System.out.println("\trightChild: " + null);
        }
    }
    
};

class SimpleBinTree<T>
{
    private TreeNode<T> m_root;
//    private T current_node;
    private int m_numOfNodes;
    private int m_TreeHeight = 0;
    private boolean m_balanced;
    
    //  Didn't really use this.
    //  wanted to use it for the .whatAmI() method in TreeNode<T>
    private Class<T> class_type;
    
    SimpleBinTree()
    {
        
    }
    
    SimpleBinTree(TreeNode<T> startNode)
    {
        m_root = startNode;
        m_numOfNodes = 1;
        m_TreeHeight = 1;
        m_balanced = true;
    }
    
    SimpleBinTree(T rootDatum, Class<T> classType)
    {
        m_root = new TreeNode(rootDatum);
        m_numOfNodes = 1;
        m_TreeHeight = 1;
        m_balanced = true;
        class_type = classType;
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
    
    public TreeNode<T> getRoot()
    {
        return m_root;
    }
    
    private void updateTreeBalance()
    {
        int maxPossibleNumOfNodes = power(2, m_TreeHeight) - 1;
        m_balanced = m_numOfNodes == maxPossibleNumOfNodes;
    }
    
    public void updateTreeHeight()
    {
        int initialHeight = m_TreeHeight;
        int twoPowerVal = power(2, initialHeight);
        if (m_numOfNodes >= twoPowerVal)
            m_TreeHeight += 1;
    }
    
    public int getTreeHeight()
    {
        updateTreeHeight();
        return m_TreeHeight;
    }
    
    public boolean isEmpty()
    {
        return m_numOfNodes > 0;
    }
    public boolean isFull()
    {
        //  basically checks if the current number of nodes
        //  is equal to the *max number of nodes at the current height*
        return (m_numOfNodes == power(2, m_TreeHeight) - 1);
    }
    
    public void preOrderTraversal(TreeNode<T> thisNode)
    {

        if (thisNode == null) return;
        //  Process
        thisNode.whatAmI();
        //  Traverse sub-trees
        preOrderTraversal(thisNode.getLeftChild());
        preOrderTraversal(thisNode.getRightChild());
    }// Ends the preOrderTraversal
    
    //  Also with preOrderTraversal
    public boolean addNodeRecursive(TreeNode<T> startNode,TreeNode<T> newNode)
    {
        boolean done = false;
        if (!startNode.isSet())
        {
            startNode.set(newNode);
            done = true;
            return done;
        }
        if (startNode.getLeftChild() == null)
        {
            startNode.setLeftChild(newNode);
            done = true;
            return done;
        }
        else if (startNode.getRightChild() == null)
        {
            startNode.setRightChild(newNode);
            done = true;
            return done;
        }
        
        done = addNodeRecursive(startNode.getLeftChild(), newNode);
        if (!done)
            done = addNodeRecursive(startNode.getRightChild(), newNode);
        
        return done;
    }
    
    public void addNode(TreeNode<T> newNode)
    {
        addNodeRecursive(m_root, newNode);
        updateTreeHeight();
        updateTreeBalance();
    }
};

/**
 * Date: Thurs-30-May
 * 1.   Took expression string and processed
 * 2.   Enabled conversion to char[]
 * 3.   Created Datatypes: TreeNode and SimpleBinTree
 * 4.   Did infix to postfix of expression
 * 5.   Did postfix to expression
 * 6.   Last:
 *          Traversed tree for evaluation of expression using stack
 *
 */


public class expression_eval {
    public static void main(String[] args)
    {
        /*
        SimpleBinTree<Character> myTree = new SimpleBinTree('c', Character.class);
        SimpleBinTree<Character> myTree = new SimpleBinTree('c', Character.class);
        myTree.addNode(new TreeNode('F'));
        myTree.addNode(new TreeNode('i'));
        myTree.addNode(new TreeNode('*'));
        myTree.addNode(new TreeNode('H'));
        myTree.preOrderTraversal(myTree.getRoot());*/
        
//        String expr = "2 + 3 * 5";
//        String expr = "(A + B) * C - D / E";
        String expr = "(A + (B * (C - D)))";
        char[] expr_char = processExpression(expr);
        printArray(expr_char);
        System.out.println("Postfix Form: " + infixToPostfix(expr_char));
        
        char[] postfix_expr = stringToCharArray(infixToPostfix(expr_char));
        
        SimpleBinTree<Character> expr_tree = postFixToExprTree(postfix_expr);
//        expr_tree.preOrderTraversal(expr_tree.getRoot());
        
        System.out.println("Expression Tree to Infix: " 
                + exprTreeToInfix("", expr_tree.getRoot()));
        
        
        //  Evaluating actual numeric expression:
        System.out.println("\nEvaluating expression:");
        String numExpr = "(5 + (3 * (7 - 2)))";
        char[] numExprChar = processExpression(numExpr);
        printArray(numExprChar);
        char[] numExprPostfix = stringToCharArray(infixToPostfix(numExprChar));
        SimpleBinTree<Character> numExprTree = postFixToExprTree(numExprPostfix);
//        float result = evalExprTree(0, numExprTree.getRoot());
//        System.out.println("Result: " + result);
        float result = evalExprTreeM2(numExprTree.getRoot());
        System.out.println("Result: " + result);
        
    }
    
    private static char[] stringToCharArray(String str)
    {
        char[] charArray = new char[str.length()];
        for (int i = 0; i < str.length(); i++)
        {
            charArray[i] = str.charAt(i);
        }
        return charArray;
    }
    private static void printLength(String expr)
    {
        System.out.println("Length: " + expr.length());
    }
    
    private static char[] processExpression(String expression)
    {
        int length = 0;
        expression = expression.strip();
        for (int i=0; i < expression.length(); i++)
        {
            if (expression.charAt(i)!= ' ')
            {
                length += 1;
            }
        }
        char[] characterArray = new char[length];
        int change = 0;
        for (int i=0; i < expression.length(); i++)
        {
            if (expression.charAt(i)!= ' ')
            {
                characterArray[i - change] = expression.charAt(i);
            }
            else
            {
                change++;
            }
        }
        System.out.println("Read string length (without whitespace): " + length);
        return characterArray;
    }
    
    private static void printArray(char[] arr)
    {
        String expr = "";
        for (int i = 0; i < arr.length; i++)
        {
            if (i != arr.length - 1)
                expr += Character.toString(arr[i]) + " ";
            else
                expr += Character.toString(arr[i]);
        }
        System.out.println(expr);
    }
    
    private static String infixToPostfix(char[] expression)
    {
        MyStackDT<Character> exprStack = new MyStackDT(Character[].class, expression.length);
        int pointer = 0;
        //  This is used to determine their precedences
        String opsPrecedence = "+-*/";
        
        //  To hold final postfix string, not printing
        String postfixExpr = "";
    
        while (true)
        {
            if (pointer >= expression.length) break;
            
            char token = expression[pointer];
            //  If token is an operand, print it out
            switch(token)
            {
                case '(' -> {exprStack.push(token);}
                case ')' -> {
                    while (true)
                    {   
                        if (!exprStack.isEmpty())
                            token = exprStack.pop();
                        else
                            break;
                        //  Keeps printing from stack until token
                        //  is '('
                        if (token == '(')
                            break;
                        postfixExpr += token;
                    }
                }   
                case '+', '-', '*', '/' -> {
                    char topVal = ' ';
                    if (!exprStack.isEmpty())
                    {
                        topVal = exprStack.peek();
                    }           //  Remember - indexOf gives -1 if character can't be found
                    while(opsPrecedence.indexOf(topVal) >= opsPrecedence.indexOf(token))
                    {
                        if (!exprStack.isEmpty())
                        {
                            topVal = exprStack.peek();
                        }
                        else
                            break;
                        
                        if (!exprStack.isEmpty())
                            postfixExpr += exprStack.pop();
                    }
                    
                    exprStack.push(token);                    
                }
                default -> {postfixExpr += token;}
            }
            pointer++;
        }   //  When all tokens have been taken, loop exits
        while (!exprStack.isEmpty())
        {
            postfixExpr += exprStack.pop();
        }
        return postfixExpr;
    }
    
    private static SimpleBinTree<Character> postFixToExprTree(char[] expression)
    {
//        MyStackDT<Character> characterStack = new MyStackDT(Character.class, expression.length);
        
        /**
         * Yo! Pretty cool right ;) thank God.
         * pree that I used a Stack of TreeNodes to make things way simple
         * in the end, it returns the tree
         */        
        
        //  Either use this:
            //MyStackDT<TreeNode<Character>> treeNodeStack = new MyStackDT(TreeNode[].class, expression.length);
        //  OR this:
        MyStackDT<TreeNode<Character>> treeNodeStack = new MyStackDT(expression.length);
        int pointer = 0;
        char token = ' ';   //  Chars can't have empty char
        while (true)
        {
            if (pointer >= expression.length) break;
            
            token = expression[pointer++];  //  Post increment
            
            switch(token)
            {
                case '+', '-', '*', '/'->{
                    TreeNode<Character> right = treeNodeStack.pop();
                    TreeNode<Character> left = treeNodeStack.pop();
                    
                    treeNodeStack.push(new TreeNode(token, left, right));
                }
                default ->{ //  For operands
                    treeNodeStack.push(new TreeNode<>(token));
                }
            }
        }
        //  In the end stack will have just one item, the root
        //  of this expression tree
        return new SimpleBinTree<>(treeNodeStack.pop());
    }
    

    //  This basically converts expression tree back to infix.
    //  following this, I will be able to evaluate an expression of actual numbers.
    //  it probably requires a stack. Here I don't use a stack, rather
    //  it's appended to the string
    private static String exprTreeToInfix(String out_result, TreeNode startNode)
    {
//        if (startNode == null) return ""; no need for this
//        MyStackDT<TreeNode<Character>> exprEvalStack = new MyStackDT(10);

        if (startNode.isLeaf())
        {
            out_result += startNode.getDatum();
            return out_result;
        }
        else
        {
            out_result += '(';
            out_result = exprTreeToInfix(out_result, startNode.getLeftChild());
            out_result += startNode.getDatum();
            out_result = exprTreeToInfix(out_result, startNode.getRightChild());
            out_result += ')';
        }
        return out_result;
    }
    
    //  NOTE!, No, didn't use the stack, again.
    private static float evalExprTree(float out_result, TreeNode<Character> startNode)
    {
        /**
         * Doesn't use stack -- check method2
         */
        if (startNode.isLeaf())
        {   
            return Character.getNumericValue(startNode.getDatum());
        }
        else
        {
            out_result = evalExprTree(out_result, startNode.getLeftChild());
            switch(startNode.getDatum())
            {
                case '+'->{
                    out_result = out_result + evalExprTree(out_result, startNode.getRightChild());
                }
                case '*'->
                {
                    out_result = out_result * evalExprTree(out_result, startNode.getRightChild());
                }
                case '-' ->{
                    out_result = out_result - evalExprTree(out_result, startNode.getRightChild());
                }
                case '/' ->{
                    out_result = out_result / evalExprTree(out_result, startNode.getRightChild());
                }
            }
        }
        return out_result;
    }
    
    /*_________Evaluating Expression Tree Method 2 using Stack DT___*/
    
    
    //  This method uses the stackDT to evaluate -- superflous :/
    private static float evalExprTreeRecursive(MyStackDT<Float> exprEvalStack, TreeNode<Character> startNode)
    {
        float out_result = 0;
        
        if (startNode.isLeaf())
        {   
            exprEvalStack.push((float)Character.getNumericValue(startNode.getDatum()));
            return 0;
        }
        else
        {
            out_result = evalExprTreeRecursive(exprEvalStack, startNode.getRightChild());
            evalExprTreeRecursive(exprEvalStack, startNode.getLeftChild());
            
            if (out_result != 0)
                exprEvalStack.push(out_result);
            
            switch(startNode.getDatum())
            {
                case '+'->{
                    out_result = exprEvalStack.pop() +  exprEvalStack.pop();
                }
                case '*'->
                {
                    out_result = exprEvalStack.pop() *  exprEvalStack.pop();
                }
                case '-' ->{
                    out_result = exprEvalStack.pop() -  exprEvalStack.pop();
                }
                case '/' ->{
                    out_result = exprEvalStack.pop() /  exprEvalStack.pop();
                }
            }
        }
        return out_result;
    }
    private static float evalExprTreeM2(TreeNode<Character> startNode)
    {
        float out_result = 0;
        /**
         * It's very useful to know that every operator is not a leaf node
         * hence we make the stack store only the numeric values, the leaf nodes
         */
        MyStackDT<Float> exprEvalStack = new MyStackDT(10);
        
        out_result = evalExprTreeRecursive(exprEvalStack, startNode);
        
        return out_result;
    }
    
    
    //  The one that prints.
    private static void infixToPostfixPrint(char[] expression)
    {
        MyStackDT<Character> exprStack = new MyStackDT(Character[].class, expression.length);
        int pointer = 0;
        //  This is used to determine their precedences
        String opsPrecedence = "+-*/";
    
        while (true)
        {
            if (pointer >= expression.length) break;
            
            char token = expression[pointer];
            //  If token is an operand, print it out
            switch(token)
            {
                case '(' -> {exprStack.push(token);}
                case ')' -> {
                    while (true)
                    {   
                        if (!exprStack.isEmpty())
                            token = exprStack.pop();
                        else
                            break;
                        //  Keeps printing from stack until token
                        //  is '('
                        if (token == '(')
                            break;
                        System.out.print(token);
                    }
                }   
                case '+', '-', '*', '/' -> {
                    /**
                     * Date: Thurs-30-May-2024
                     * I've gone through this algorithm, and this part is pretty cool
                     * From lectures
                     * basically, its effect is seen at when token is '-' and '/'
                     * in expression (A + B) * C - D / E
                     * At point where token = B
                     * Stack = ['(' '+']
                     * Printed = [ A ]
                     * After token = B and is now = )
                     * Stack = []   -- note that '(' is popped and never printed, neither is ')'
                     * Printed = [ A B + ]
                     * At point where token = C
                     * Stack = ['*']
                     * Printed = [ A B + C ]
                     * At point where token = -
                     * Stack = ['-'] -- '*' was popped because it has higher precedence than -
                     * Printed = [A B + C * ]
                     * At point where token = /
                     * Stack = ['-' '/'] -- '-' remains because it has lower precedence than '/'
                     * Printed = [ A B + C * D]
                     * At point where token = E
                     * Stack = ['-' '/']
                     * Printed = [A B + C * D E]
                     * Lastly, now all tokens have been gone through, while loop is done
                     * As long as stack is not empty, it's printed out
                     * stack.pop() until stack is empty
                     * Stack = []
                     * Printed = [ A B + C * D E / - ]  <- Final postfix
                     */

                    char topVal = ' ';
                    if (!exprStack.isEmpty())
                    {
                        topVal = exprStack.peek();
                    }           //  Remember - indexOf gives -1 if character can't be found
                    while(opsPrecedence.indexOf(topVal) >= opsPrecedence.indexOf(token))
                    {
                        if (!exprStack.isEmpty())
                        {
                            topVal = exprStack.peek();
                        }
                        else
                            break;
                        
                        if (!exprStack.isEmpty())
                            System.out.print(exprStack.pop());
                    }
                    
                    exprStack.push(token);                    
                }
                default -> {System.out.print(token);}
            }
            pointer++;
        }   //  When all tokens have been taken, loop exits
        while (!exprStack.isEmpty())
        {
            System.out.print(exprStack.pop());
        }
        System.out.println("");
    }
}
