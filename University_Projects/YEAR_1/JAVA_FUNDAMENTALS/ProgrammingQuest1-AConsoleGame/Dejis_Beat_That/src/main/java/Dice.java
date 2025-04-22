/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author x7e30
 */
public class Dice {
    int outcome = 0;
    
    int roll_die()
    {
        double x = Math.random(); // Returns a random number between 0 and 1
        x = 1.0 + (x * 6.0);
        
        outcome = (int)Math.floor(x);
        
        return outcome;
    }
}
