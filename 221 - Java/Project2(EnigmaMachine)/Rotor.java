// Remember, you can't change the interface, nor add import statements

public class Rotor 
{
    // decide on your instance variables to represent a rotor
    private int pos;
    private int startPos;
    private Character[] letters = new Character[26];
    // The parameter alphaperm below is a permutation of ['a','z']
    // startpos is the starting position of the rotor
    public Rotor(Character[] alphaperm, char startpos) 
    {
	letters = alphaperm;
	for (int count = 0; count < 26; count++)
	{
		pos = count;
		startPos = count;
		if (letters[count] == startPos)
		{
			break;
		}
	}
    }

    // encode one character, ch, according to the rotor "wiring"
    public char encode(char ch) 
    {
    	int tempIndexer = (int) ch - 97 + pos;
    	if (tempIndexer >= 26)
    	{
    		tempIndexer = tempIndexer % 26;
    	}
	return letters[tempIndexer];
    }

    /*
       decode one character, ch, according to the rotor "wiring"
       (reverse dir). Decoding is a bit tricky.  First we need to
       reverse map the incoming character.  Then, we need to "rotate"
       (in the reverse direction) the decoded character by the
       position, pos.  To do this, we can't just subtract pos (might
       become negative), so we add 26, then subtract.
    */
    public char decode(char ch) 
    {
	int tempIndexer = 0;
	for (int count = 0; count < 26; count++) 
	{
		if (letters[count] == ch)
		{	
			tempIndexer = count + 26 - pos;
		}
	}
	if (tempIndexer >= 26)
    	{
    		tempIndexer = tempIndexer % 26;
    	}
    	return (char) (tempIndexer + 97);
    }

    /*
       advance the roter one position.  Think about what instance
       variable(s) you need to keep track of this.  This method
       returns true of the rotor has made a complete turn; otherwise
       false
    */
    public boolean advance() 
    {
	if (pos < 25)
	{
		pos = pos + 1;
	}
	else if (pos == 25)
	{
		pos = 0;
	}
	if (pos == startPos)
	{
		return true;
	}
	return false;
    }

    // reset the starting position for the rotor
    public void reset(char startpos) 
    {
	pos = startPos;
	
    }
}
