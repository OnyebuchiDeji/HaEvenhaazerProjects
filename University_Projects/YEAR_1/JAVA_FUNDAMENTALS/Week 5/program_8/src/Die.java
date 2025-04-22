public class Die
{
    int outcome;
    
    void roll()
    {
        double x = Math.random();
        x = 1.0 + (x * 6.0);
        
        outcome = (int)Math.floor(x);   // math.floor returns the largest integer value <= the number
        //  It just returns a whole number because this is int
    }    
}

