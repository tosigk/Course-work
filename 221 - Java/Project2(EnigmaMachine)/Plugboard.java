// Remember, you can't change the interface, nor add import statements
public class Plugboard 
{
    // decide on your instance variables to represent the plugboard
    	private Character[] swapsArray;
    // NOTE:  you need to be able to map and reverse-map                                    
    //        (remember the direction of flow when discussed in class)
    
    // swaps is a string with upto 10 pairs of characters to swap (eg. "ajqzbw")
    public Plugboard(Character[] swaps) 
    {  // construct a Plugboard
	if ((swaps.length/2 <= 10) && (swaps.length % 2 == 0))
	{
		swapsArray = new Character[swaps.length];
		swapsArray = swaps;
	}
	else
	{
		System.out.print("There is an error in the plugboard.");
		System.exit(1);
	}
	// NOTE: check that plugboard has 10 or fewer letter pairs
	// NOTE: check that plugboard has an even number of letters
	// if the above two are not both true, print a error message and exit
    }

    // encode one character through the plugboard
    // (you may assume that ch is a valid character in range ['a', 'z']
    public char encode(char ch) 
    {
	for (int pos = 0; pos < swapsArray.length; pos++) //pos stands for position of char in the list
	{
		if (ch == swapsArray[pos])
		{
			if (pos % 2 == 0)
			{
				return swapsArray[pos + 1];
			}
			else if (pos % 2 != 0)
			{
				return swapsArray[pos -1];
			}
		}
	}
	return ch;
    }

    // decode one character through the plugboard
    // (you may assume that ch is a valid character in range ['a', 'z']
    public char decode(char ch) 
    {	
	for (int pos = 0; pos < swapsArray.length; pos++) //pos stands for position of char in the list
	{
		if (ch == swapsArray[pos])
		{
			if (pos % 2 == 0)
			{
				return swapsArray[pos + 1];
			}
			else if (pos % 2 != 0)
			{
				return swapsArray[pos -1];
			}
		}
	}
	return ch;
    }
}
