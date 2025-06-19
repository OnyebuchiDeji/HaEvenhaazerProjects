package Advanced_Data_Structures.Exercise;

import java.util.LinkedHashMap;

public class VotingSystem
{
    //  A LinkedHashMap with the contestant name as key and...
    //  Number of votes as value
    private LinkedHashMap<String, Integer> voters = new LinkedHashMap<>();

    public void vote(String contestant)
    {
        //  Implement this method so that a new contestant is added to the map...
        //  If they are not already there.
        //  But if they are, increment their vote by 1

        /* Hard Way */
        if (voters.containsKey(contestant))
        {
            voters.put(contestant, voters.get(contestant) + 1);
        }
        else
        {
            voters.put(contestant, 1);
        }

        /*  Easy Way   */
        //voters.merge(contestant, 1, Integer::sum);

    }

    //  This method should return the LinkedHashMap field created at the top of the class:
    public LinkedHashMap getVotes()
    {
        return voters;
    }
}
