import java.util.Random;
import java.lang.Math;


class randomTest1{

  public static void main(String[] args)
  {
    Random rnd = new Random();

    for (int i=0; i<100; i++){
      int val = rnd.nextInt(20);
      System.out.println("Random Number: " + val );
    }
  }

}