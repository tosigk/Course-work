import java.util.Collections;   // for shuffle
import java.util.Arrays;        // also for shuffle (need asList)
import java.util.Random;        // for seeding the random number for shuffle
                                // NOTE: we seed to be able to repeat results

public class Enigma 
{
    /*
      An Enigma object represents the venerable, Enigma Machine, which
      was used by the Nazi's to encrypt communication messages during
      WWII.  Please see https://en.wikipedia.org/wiki/Enigma_machine.

      An Enigma machine consists of three part types: Rotor,
      Plugboard, and Reflector.  You will find for this assignnment
      the respective class for these three part types:

           Rotor.java, Plugboard.java, and Reflector.java

      Read the comments in each provided class and implement the
      required constructors and methods.

      In total, there are five class for this assignment, this class
      and the three mentioned above plus the class, TestEnigma.java,
      which contains the main method and will "put everything
      together" and test our Enigma machine.
      
      All the interfaces have been written for you, and you CANNOT
      change these.  In addition, any code already provided for you
      must be used UNCHANGED.  You may add other private methods as
      "helper" methods.  You CANNOT import any other classes.
      Violating any of the rules will incur a severe point penalty!

      Each class is worth 4 points, and the assignment is worth 20
      points total.

      I have provided some useful comments to help you implement your
      constructors and methods.  Please read the comments.
    */

    // decide on what instance variables you need for an Enigma Machine
    // (ie.  What "parts" make up an Enigma Machine?)

    /*
       The following method will check if a given character "maps" to
       itself in alphaperm
    
       NOTE: you may use this function before/when constructing the
       reflector, U (which cannot have a self mapping).
    */
    private boolean check_for_self_mapping(Character[] alphaperm)
    {
	for (int i = 0; i < alphaperm.length; i++) 
	{
            if (alphaperm[i] == i + 'a') 
            {
		return true;
	    }
	}
	return false;
    }

    /*
      To "construct" an Enigma machine, you will need to specify the
      plugboard settings (a String of even length with up to 10 unique
      pairs of "swap" characters).  For example, "qwerty". The rotor
      (aka scrambler) orientation settings is a String of length three
      (eg. "qcw" or "abc").  This String indicates the initial
      positions of the three respective rotors in our Enigma machine,
      which I will call R, M, and L (as was done in the "Mathematical
      analysis" section of the wikipedia article).

      You must decide what instance variables you need to represent
      the Enigma object, and declare these instance variables just
      before the constructor.  They should be private.

      See the comments in the constructor for guidance on implemention.
    */
    private Rotor R;
    private Rotor M;
    private Rotor L;
    private Reflector U;
    private Plugboard P;
    public Enigma(Character[] plugboard_settings, String rotor_settings,
		  int rseed) 
    {
	Character[] l = new Character[26];  // "wrapper" class for char
	
	// you must build an array of characters, l, in order
	// (ie. ['a','b',...'z'])
	for (int count = 0; count < 26; count++)
	{
		l[count] = (char) (count + 97);
	}
	// NOTE: we are using the wrapper class, Character, for our
	// array of characters because we want to use the Collections
	// class to "shuffle" our array

	// "shuffle" will permute the list l
	Collections.shuffle(Arrays.asList(l), new Random(rseed));
	
	// you must construct rotor object, R, which permutes
	// (encodes) according to l.
	// do the same thing to construct other two scramblers, M and L
	R = new Rotor(l, rotor_settings.charAt(0));
	Collections.shuffle(Arrays.asList(l), new Random(rseed));
	M = new Rotor(l, rotor_settings.charAt(1));
	Collections.shuffle(Arrays.asList(l), new Random(rseed));
	
	L = new Rotor(l, rotor_settings.charAt(2));
	do 
	{
	    // NOTE: we can't use the same seed, else possible infinite loop
	    //       so we increment rseed each time through the loop
	    Collections.shuffle(Arrays.asList(l), new Random(rseed++));
	} 
	while (check_for_self_mapping(l) == true);
	
	U = new Reflector(l);
	
	// construct the plugboard object
	P = new Plugboard(plugboard_settings);
    }

    /*
      write a method, encode(), which will receive a plaintext
      character and encode it into a ciphertext character.  The term
      plaintext simply means the character or String we want to
      encrypt, and ciphtertext means the resulting encrypted character
      or String. The complete encryption formula for the Enigma
      machine is given in the wikipedia article:

          E = P R M L U L-1 M-1 R-1 P-1

      The above formula means, we first encode the character through
      the plugboard object, then through rotor R, then through rotor
      M, then through rotor L, then through the reflector object, U,
      and the back through the objects in reverse (a reverse operation
      is called decode).

      NOTE: you will also need to perform the "odometer"-like process
      of stepping (aka advancing) respective rotor positions.  Each
      character that is encoded/decoded will advance the R rotor by
      1/26th of a revolution.  Once this rotor reaches its "last"
      position, it cycles around to the first position and causes the
      M rotor to advance one position.  A similar process occurs
      between the M rotor and the L rotor.
    */
    public char encode(char ch) 
    {	
	char enc_ch = '\0';  // will hold the result of the encoded character
	enc_ch = P.encode(ch);
	boolean cont = false; // cont stands for continue
	if (R.advance() == true)
	{
		cont = true;
	}
	if (cont = true)
	{
		cont = false;
		if (M.advance() == true)
		{
		cont = true;
		}
	}
	if (cont == true)
	{
		L.advance();
	}
	enc_ch = R.encode(enc_ch);
	enc_ch = M.encode(enc_ch);
	enc_ch = L.encode(enc_ch);
	enc_ch = U.encode(enc_ch);
	enc_ch = L.decode(enc_ch);
	enc_ch = M.decode(enc_ch);
	enc_ch = R.decode(enc_ch);
	enc_ch = P.decode(enc_ch);

	return enc_ch;       // return encoded character
    }

    /*
      write the method, decode().  The Enigma is "self-reciprocal".
      This means that the decryption process is the same as the
      encryption process, only using the ciphertext character as
      input.  Also, note, that this prevents any letter from being
      encrypted to itself.  This method returns the plaintext character.
    */
    public char decode(char ch) 
    {
    	 
	char dec_ch = '\0'; // will hold the result of the decoded character
	dec_ch = P.encode(ch);
	
	boolean cont = false;
	if (R.advance() == true)
	{
		cont = true;
	}
	if (cont = true)
	{
		cont = false;
		if (M.advance() == true)
		{
		cont = true;
		}
	}
	if (cont == true)
	{
		L.advance();
	}
	dec_ch = R.encode(dec_ch);
	dec_ch = M.encode(dec_ch);
	dec_ch = L.encode(dec_ch);
	dec_ch = U.decode(dec_ch);
	dec_ch = L.decode(dec_ch);
	dec_ch = M.decode(dec_ch);
	dec_ch = R.decode(dec_ch);	
	dec_ch = P.decode(dec_ch);	
	
	return dec_ch;      // return decode character
    }

    /*
      write the method, reset().  This method will "reset" the Enigma
      machine to a specified rotor orientation settings.
      Nothing is returned.
    */
    public void reset(String rotor_settings) 
    {
	
	R.reset(rotor_settings.charAt(0));
	M.reset(rotor_settings.charAt(1));
	L.reset(rotor_settings.charAt(2));
	
    }
}
