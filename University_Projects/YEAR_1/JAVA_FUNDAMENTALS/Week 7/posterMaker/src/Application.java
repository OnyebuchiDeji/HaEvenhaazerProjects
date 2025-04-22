public class Application
{
    public static float convertValue(int value)
    {
        if (value < 0)
        {
            value = 0;
            System.out.println("Value cannot be negative, it must be between 0 and 255!");
        }
        
        value = value % 255;
        
        float newValue;
        
        newValue = (float)value / 255;
        
        return newValue;
    }
    
    public static void firstPosterEG(String name)
    {
        Poster myPoster = new Poster();  // Create new poster.
        
        float red, green, blue;
        // Paint poster.

        red = 1.0F;
        green = 0.0F;
        blue = 0.0F;
        myPoster.setTileColour(0, 0, red, green, blue);

        red = 0.0F;
        green = 1.0F;
        blue = 0.0F;
        myPoster.setTileColour(0, 1, red, green, blue);
        
        red = 0.0F;
        green = 0.0F;
        blue = 1.0F;
        myPoster.setTileColour(1, 0, red, green, blue);

        
        myPoster.displayAndSave(name);  // Display the image and write to file.
    }
   
    public static void makePoster(String name)
    {
        Poster myPoster = new Poster();
        
        float red = 0.0f;
        float blue = 0.0f;
        float green = 0.0f;
        
        for (int row = 0; row < myPoster.height; ++row)
        {
            for (int rowTile = 0; rowTile < myPoster.width; ++rowTile)
            {
               
                red = convertValue(row+rowTile);
                green = convertValue(rowTile + row);
                blue = convertValue(row-rowTile);
                
                
                myPoster.setTileColour(rowTile, row, red, green, blue); 
            }
        }
        
        System.out.println("DONE!");
        
                
        myPoster.displayAndSave(name);
    }
    
    public static void main(String[] args)
    {
        //firstPosterEG("poster");
        
        makePoster("mySeventhPoster");
        
        
        
    }
}
