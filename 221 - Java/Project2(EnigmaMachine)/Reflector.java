// Remember, you can't change the interface, nor add import statements

public class Reflector 
{
    // decide on your instance variables to represent the reflector
    // NOTE:  you need to be able to map and reverse-map
    //        (remember the direction of flow when discussed in class)
    private Character[] letters = new Character[26];
     // helper function that checks for self mapping
    // return -1 if NO self map; otherwise return position of self map
    private static int check_for_self_mapping(Character[] alphaperm)
    {
	for (int i = 0; i < alphaperm.length; i++) 
	{
            if (alphaperm[i] == i + 'a') 
            {
		return i;
	    }
	}
	return -1;
    }

    // alphaperm is a permutation (rearrangement) of ['a','z']
    // NOTE: NO self mappings AND pairwise mapped.
    public Reflector(Character[] alphaperm)
    {
	letters = alphaperm;
    }

    // encode one character through the reflector
    public char encode(char ch) 
    {
	int tempIndexer = ((int) ch) - 97;
	return letters[tempIndexer];	
    }

    // decode one character through the reflector
    public char decode(char ch) 
    {
    	int tempIndexer = 0; 
	for (int count = 0; count < 26; count++)
	{
		tempIndexer = count;
		if (ch == letters[count])
		{
			break;
		}
	}
	return (char) (tempIndexer + 97); 
    }
}
