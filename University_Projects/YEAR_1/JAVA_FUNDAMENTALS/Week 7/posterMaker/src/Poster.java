import java.awt.*;
import java.awt.image.*;
import java.io.*;
import javax.imageio.*;
import javax.swing.*;

public class Poster
{
    final int width = 80;
    final int height = 60;

    private BufferedImage image;
    private WritableRaster raster;
    private ColorModel colourModel;
    
    public Poster()
    {
        image = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
        raster = image.getRaster();

        colourModel = image.getColorModel();
    }
    
    public void setTileColour(int x, int y, float red, float green, float blue)
    {
        Color colour  = new Color(red, green, blue);
        
        raster.setDataElements(x, y, colourModel.getDataElements(colour.getRGB(), null));
    }
    
    public void displayAndSave(String fileName)
    {
        final int scale = 10;

        // Create a new, scaled version of the image here.
        BufferedImage scaledImage = new BufferedImage((scale * width), (scale * height), BufferedImage.TYPE_INT_RGB);
        Graphics2D g = scaledImage.createGraphics();
        g.drawImage(image, 0, 0,(scale * width), (scale * height), null);
        g.dispose();
        
        try {
            ImageIO.write(scaledImage, "gif", new File(fileName + ".gif"));   
        } catch(IOException e) {
            System.out.println(e.toString());
        }

        JFrame imageFrame = new JFrame("Poster");
        ImagePanel imagePanel = new ImagePanel(scaledImage);
        imageFrame.add(imagePanel);
        imageFrame.setSize(((scale * width) + 16), ((scale * height) + 36));
        imageFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        imageFrame.setVisible(true);
    }
    
    private class ImagePanel extends JPanel
    {
        private BufferedImage image;
    
        public ImagePanel(BufferedImage image)
        {  
            this.image = image;
        }
       
        public void paintComponent(Graphics g)   
        {  
            super.paintComponent(g);
           
            if (image == null) {
                return;
            }
    
            g.drawImage(image, 0, 0, null);
        }
    }
}
