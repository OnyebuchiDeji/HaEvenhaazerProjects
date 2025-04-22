public class Die
{
    int outcome;
    
    void roll()
    {
        double x = Math.random();
        x = 1.0 + (x * 6.0);
        
        outcome = (int)Math.floor(x);
    }    
}

