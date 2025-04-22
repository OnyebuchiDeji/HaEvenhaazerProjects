/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package week8pract13;

/**
 *
 * @author Ebenezer Ayo-Meti
 */
public class Dice {
    int outcome;
    
    void roll()
    {
        double x = Math.random();
        x = 1.0 + (x * 6.0);
        
        outcome = (int)Math.floor(x);
    }    
}
