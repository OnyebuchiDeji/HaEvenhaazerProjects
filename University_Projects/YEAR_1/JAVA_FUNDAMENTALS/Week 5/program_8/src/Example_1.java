
public class Example_1 {

    public static void main(String[] args) {

        int trials = 0;
        int outcome = 0;

        Die die1 = new Die();
        Die die2 = new Die();

        do {

            die1.roll();
            die2.roll();

            outcome = die1.outcome + die2.outcome;

            trials++;

            if (outcome == 12) {
                System.out.println("Rolled a double-six after " + trials + " trials.");
            } else {
                System.out.println("Trial " + trials + ": " + outcome);
            }

        } while (outcome != 12);

    }
}
