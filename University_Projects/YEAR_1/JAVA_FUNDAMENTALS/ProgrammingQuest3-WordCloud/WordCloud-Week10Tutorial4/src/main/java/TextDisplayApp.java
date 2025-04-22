
/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Ebenezer Ayo-Meti 22021699
 */

import java.awt.Font;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
//import java.awt.*;
//import javax.swing.*;

public class TextDisplayApp {

//    public static void main(String[] args) {
//        
//        String[] dictionary = {"door", "exit", "main", "fire", "assembly", "point", "the", "a", "alarm", "bell"};
//        int[] lengths = {3, 2, 1, 4, 3, 2, 6, 12, 3, 1};
//        
//        wordCloud(dictionary, lengths);
//    }
    
    public static void wordCloud(String[] words, int[] sizes)
    {
        JFrame frame = new JFrame("Word cloud");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        JPanel panel = new JPanel();
        JLabel[] labels = new JLabel[words.length];
        
        frame.setSize(600, 800);

        int maxFontSize = 100;
        int minFontSize = 10;
        
        // Rescale the font sizes.
        int max=sizes[0], min=sizes[0];
        for(int i=1; i<words.length; i++) {
            if(sizes[i] > max) {
                max = sizes[i];
            }
            
            if(sizes[i] < min) {
                min = sizes[i];
            }
        }

        for(int i=0; i<words.length; i++) {
            /*
                Comment: Wed-21-Feb-2024
            Elab:
                sizes[i] is the actual size or rather frequency of occurence of the text.
                doing sizes[i] - min is like finding the difference in proportion between the current word's...
                frequency and the minimum frequency, as determined in the code segment above...
                dividing by (max - min) is a way of scaling it to be not larger than the greatest possible difference.
                
                Then mulitplying this by the fontSize largest possible difference  added to the minimum fontSize can be explained liek this.
                (maxFontSize - minFontSize) is like the rate of increase. Like r = v(t) + a
                r = new value. v = rate. t = time or scale. a = previous value.
                In this case, the scale is (sizes[i] - min)/(float)(max - min) and the rate is (maxFontSize - minFontSize)...
                with the previous, the smallest possible value being minFontSize.
            
                Understand? Yes please! Thank the Father for the Son and inthe name of the Son.
            */
            int labelSize = (int)Math.round((((float)(sizes[i] - min)/(float)(max - min)) * (float)(maxFontSize - minFontSize)) + minFontSize);
            labels[i] = new JLabel(words[i]);
            labels[i].setFont(new Font("Times New Roman", Font.PLAIN, labelSize));

            panel.add(labels[i]);
        }
        
        frame.add(panel);
        
        frame.setVisible(true);
    }
    
}

