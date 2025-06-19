
package Concurrency;

/**
 *
 * @author bethan
 */
public class Kitchen {

    public static Object spoon = new Object();
    public static Object bowl = new Object();

    public static void main(String args[]) {
        //  A deadlock would occur if this one accessed spoon first...
        Thread cook1 = new Thread(() -> {
            //  This is a synchronized block, allowing only one thread to enter at a time...
            //  The spoon synchronized(spoon) is a monitoring object, meaning that if a thread...
            //  is inside a synchronized block, no other thread can do anything with that object.
            synchronized (spoon) {
                System.out.println("Cook1: Holding the spoon...");
                System.out.println("Cook1: Waiting for the bowl...");

                //  Then the thread takes this second synchroinized block with bowl as the monitoring object
                synchronized (bowl) {
                    System.out.println("Cook1: Holding the spoon and the bowl.");
                }
            }
        });

        //  ... But this one accessed bowl first, so cook1 waits for cook2 to finish using bowl
        //  but cook22 cannot finish unless spoon is accessed, but spoon cannot be acccessed...
        //  Because cook1 has already accessed it and cannot release it unless cook2 releases bowl.
        Thread cook2 = new Thread(() -> {
            synchronized (bowl) {
                System.out.println("Cook2: Holding the bowl...");
                System.out.println("Cook2: Waiting for the spoon...");
        //  ...but cook2 can't finish unless with
                synchronized (spoon) {
                    System.out.println("Cook1: Holding the spoon and the bowl.");
                }
            }
        });
        //  SOLUTION
        //  Let them access the same objects at the same time. That way, the synchronized keyword...
        //  would automatically make sure that one finishes before the other.
        //  That way one would access and finish using bothe spoon and bowl before the other
        Thread cook2A = new Thread(() -> {
            synchronized (spoon) {
                System.out.println("Cook2: Holding the bowl...");
                System.out.println("Cook2: Waiting for the spoon...");

                synchronized (bowl) {
                    System.out.println("Cook1: Holding the spoon and the bowl.");
                }
            }
        });
        cook1.start();
        cook2A.start();
        
    }

}
