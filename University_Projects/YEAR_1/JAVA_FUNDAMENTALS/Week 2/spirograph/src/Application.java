import java.awt.*;
import java.awt.event.*;    //  The star * means import everything in the class or method
import javax.swing.*;
import java.lang.Math;
import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;
import java.util.LinkedList;
import java.util.ListIterator;
import javax.swing.JOptionPane;

public class Application extends JFrame {
    
    public Application()
    {
        setTitle("Spirograph");
        
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        SpiroPanel sp = new SpiroPanel();
        add(sp);

        pack();
        setVisible(true);
    }

    public static void main(String[] args)
    {
        Application instance = new Application();
    }

    class SpiroPanel extends JPanel{
        
        
        ////////////////////////////////////////////////////////////////////
        // CHANGE VALUES IN THIS AREA 
        ////////////////////////////////////////////////////////////////////

        // Pen-oscillation frequencies in the x (horizontal direction)
        // Use values between 0.0 and 3.0
        double xf1 = 1.0;
        double xf2 = 3.0;
        // Pen-oscillation frequencies in the y (vertical direction)
        // Use values between 0.0 and 3.0
        double yf1 = 0.5;
        double yf2 = 2.0;

        // The rate of energy loss of the pen due to friction.
        // Use values between 1 and 50.
        // The smaller the value the longer it will take for the drawing to complete.
        double dissipation = 50.0;  // Pixels per second.

        // The starting colour.
        // Use values between 0 and 255.
        int red = 25;
        int green = 21;
        int blue = 49;

        // Colour-channel increments. These determine how fast each colour channel changes as the pen moves.
        // Use values between 0 and 100.
        int red_inc = 53;
        int green_inc = 77;
        int blue_inc = 14;
        
        ////////////////////////////////////////////////////////////////////
        ////////////////////////////////////////////////////////////////////
        
        
        int pw, ph;  // Canvas dimensions.
        int rx, ry;  // x and y radii.
        int x, y;  // Pen position.
        boolean first_run = true;
        double t = 0.0;  // Time in seconds.
        double dt = 0.01;  // Time increment in seconds.
        
        LinkedList<int[]> trace = new LinkedList<int[]>();
        
        MyActionListener anActionListner = new MyActionListener();
        Timer myTimer = new Timer((int)Math.round(dt * 1000.0), anActionListner);

        public SpiroPanel() {
            setPreferredSize(new Dimension(600, 600));
            setBackground(Color.white);
            
            myTimer.start();
        }

        public void paintComponent(Graphics g)
        {
            super.paintComponent(g);
            
            if(myTimer.isRunning())
            {
                t += dt;
    
                pw = getWidth();
                ph = getHeight();
                
                red += red_inc;
                green += green_inc;
                blue += blue_inc;
                
                if(red > 255) {
                    red = 255;
                    red_inc = -red_inc;
                } else if(red < 0) {
                    red = 0;
                    red_inc = -red_inc;
                }
                
                if(green > 255) {
                    green = 255;
                    green_inc = -green_inc;
                } else if(green < 0) {
                    green = 0;
                    green_inc = -green_inc;
                }
                
                if(blue > 255) {
                    blue = 255;
                    blue_inc = -blue_inc;
                } else if(blue < 0) {
                    blue = 0;
                    blue_inc = -blue_inc;
                }
                
                rx = (int)Math.round((pw / 2) - (dissipation * t));
                if(rx < 0) {
                    rx = 0;
                }
                ry = (int)Math.round((ph / 2) - (dissipation * t));
                if(ry < 0) {
                    ry = 0;
                }
                
                x = (int)Math.round(rx * Math.cos(2.0 * Math.PI * xf1 * t) * Math.cos(2.0 * Math.PI * xf2 * t)) + (pw / 2);
                y = (int)Math.round(ry * Math.cos(2.0 * Math.PI * yf1 * t) * Math.cos(2.0 * Math.PI * yf2 * t)) + (ph / 2);
                
                if(first_run) {
                    first_run = false;
                } else {
                    int[] p = {x, y, red, green, blue};
                    trace.add(p);
                }
    
                if((rx == 0) && (ry == 0))
                {
                    myTimer.stop();
    
                    BufferedImage bi = new BufferedImage(pw, ph, BufferedImage.TYPE_INT_RGB); 
                    Graphics fg = bi.getGraphics();
    
                    fg.setColor(Color.white);
                    fg.fillRect(0, 0, pw, ph);
    
                    ListIterator i = trace.listIterator();
                    int[] p1 = (int[])i.next();
                    while(i.hasNext()) {
                        int[] p2 = (int[])i.next();
                        fg.setColor(new Color(p2[2], p2[3], p2[4]));
                        fg.drawLine(p1[0], p1[1], p2[0], p2[1]);
                        p1 = p2;
                    }
    
                    try{
                        ImageIO.write(bi, "png", new File("image.png"));
                    } catch (Exception e) {
                        System.out.println(e.toString());
                    }
                    
                    JOptionPane.showMessageDialog(this, "Image file written.");
                }
            }
            
            // Draw trace
            if(trace.size() > 0) {
                ListIterator i = trace.listIterator();
                int[] p1 = (int[])i.next();
                while(i.hasNext()) {
                    int[] p2 = (int[])i.next();
                    g.setColor(new Color(p2[2], p2[3], p2[4]));
                    g.drawLine(p1[0], p1[1], p2[0], p2[1]);
                    p1 = p2;
                }
                g.fillOval(x-5, y-5, 10, 10); 
            }
        }
        
        public class MyActionListener implements ActionListener
        {
            public void actionPerformed(ActionEvent e) {
                repaint();
            }
        }
    }    
}
