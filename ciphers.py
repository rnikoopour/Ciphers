import re
from string import lowercase as lowercase_letters

################################################################################
#
# CipherInterface
#
################################################################################
class CipherInterface:
    ############################################################################
    #
    # Function: SetKey
    #
    # Purpose: Sets key for cipher
    #
    # Input:
    #   key -- string: key to be used for cipher
    #
    # Output: Nothing
    #
    # This will be overwritten in subclasses
    #
    ############################################################################
    def SetKey(self, key):
        self.key = key

    ############################################################################
    #
    # Function: Encrypt
    #
    # Purpose: Encrtyps input using cipher
    #
    # Input:
    #   plaintext -- string: Text to be encrypted
    #
    # Output:
    #   plaintext -- string: Same as input
    #
    # This will be overwritten in subclasses
    #
    ############################################################################
    def Encrypt(self, plaintext):
        return plaintext
    
    ############################################################################
    #
    # Function: Decrypt
    #
    # Purpose: Decrypts input using cipher
    #
    # Input:
    #   ciphertext -- string: Text to be decrypted
    #
    # Output:
    #   ciphertext -- string: Same as input
    #
    # This will be overwritten in subclasses
    #
    ############################################################################
    def Decrypt(self, ciphertext):
        return ciphertext
    
################################################################################
#
# end CipherInterface
#
################################################################################
    
################################################################################
#
# CAESARCIPHER
#
################################################################################
class CaesarCipher(CipherInterface):
    ############################################################################
    #
    # Function: Rot13
    #
    # Purpose: Rotates letter by 13
    #
    # Input:
    #   letter -- char -- string: Character to be rotated
    #
    # Output:
    #   Char rotated by 13 -- string
    #
    ############################################################################
    def Rot13(self, letter):
        return chr(((ord(letter.lower()) - 97 + 13) % 26) + 97)
    
    ############################################################################
    #
    # Function: Encrypt
    #
    # Purpose: Encrypts plaintext
    #
    # Input:
    #   plaintext -- string: Text to be encrypted
    #
    # Output:
    #   Encrypted text -- string
    #
    ############################################################################
    def Encrypt(self, plaintext):
        return ''.join([self.Rot13(x) for x in re.sub(r'[\W0-9 ]', '', plaintext.lower())])
    
    ############################################################################
    #
    # Function: Decrypt
    #
    # Purpose: Decrypts ciphertext
    #
    # Input:
    #   ciphertext -- string: Text to be decrypted
    #
    # Output:
    #   Decrypted text -- string
    #
    ############################################################################
    def Decrypt(self, ciphertext):
        return self.Encrypt(ciphertext)
    
################################################################################
#
# end CAESAR CIPHER
#
################################################################################

################################################################################
#
# Playfair Cipher
#
################################################################################
class PlayfairCipher(CipherInterface):
    ############################################################################
    #
    # Function: PrepStringForCipher
    #
    # Purpose: Prepare input string to be used in the cipher by stripping
    #           all nonalpha chars
    #
    # Input:
    #   text -- string: Text that needs to be formatted for cipher
    #
    # Output:
    #   text -- string:  String with only alpha chars
    #
    ############################################################################
    def PrepStringForCipher(self, text):
        # Calling lower to ensure all text is lowercase
        text = re.sub(r'j', 'i', text.lower())
        text = re.sub(r'[\W0-9 ]+', '', text)
        return text
    
    ############################################################################
    #
    # Function: CreateKeyTable
    #
    # Purpose: Sets up key_table property using the key. The key should
    #           contain each letter of the alphabet at least once.  Repeated
    #           letters are ignored
    #
    # Input:
    #   None
    #
    # Output:
    #   None
    #
    ############################################################################
    def CreateKeyTable(self):
        self.key_table = ''
        for letter in self.key:
            self.key_table += letter if letter not in self.key_table else ''

    ############################################################################
    #
    # Function: SetKey
    #
    # Purpose: Sets the key for the cipher.  The key is created by the
    #           concatenation of the input and the alphabet.  This ensures
    #           every letter of the alphabet is present at least once.
    #           This also creates the key table that will be used.
    #
    # Input:
    #   key -- string: The key to be used in the cipher.  Must be alpha only.
    #
    # Output:
    #   None
    #
    ############################################################################
    def SetKey(self, key):
        # Includes lower case letters to make sure entire alphabet is used
        self.key = self.PrepStringForCipher(key + lowercase_letters)
        self.CreateKeyTable()

    ############################################################################
    #
    # Function: CreatePairs
    #
    # Purpose: Creates letter pairs that will be used in the encryption.
    #
    # Input:
    #   text -- string: The text to be encrypted.
    #
    # Output:
    #   piars -- list:  A list of tuples containg the letter pairs of the text
    #                    If the letter is paired with itself the second letter
    #                    is replaced with an x and put back in front of the list
    #
    ############################################################################
    def CreatePairs(self, text):
        i = 0
        pairs = []
        while i < len(text) - 1:
            if text[i] is not text[i+1]:
                pairs.append((text[i], text[i+1]))
                i += 2
            else:
                pairs.append((text[i], 'x'))
                i += 1

        # This will append the last letter in the text in the 
        if i is not len(text):
            pairs.append((text[-1], 'x'))
        return pairs

    ############################################################################
    #
    # Function: HandleBoxPair
    #
    # Purpose: Handles the case where the letters are on different rows and
    #           different columns.
    #
    # Input:
    #   char1_loc -- int: The location where char1 is located in the key table
    #   char2_loc -- int: The location where char2 is located in the key table
    #
    # Output:
    #   (char1_loc, char2_loc) -- tuple (int, int): a tuple of ints with the
    #                                                new location of each char
    #
    ############################################################################
    def HandleBoxPair(self, char1_loc, char2_loc):
        distance = abs(char1_loc % 5 - char2_loc % 5)
        if char1_loc % 5 > char2_loc % 5:
            char1_loc -= distance
            char2_loc += distance
        else:
            char1_loc += distance
            char2_loc -= distance
        return (char1_loc, char2_loc)

    ############################################################################
    #
    # Function: EncryptPair
    #
    # Purpose: Encrypts each letter pair based off the rules of their locations
    #           in the key table.
    #
    # Input:
    #   pair -- tuple (char, char): A tuple of chars that need to be encrypted
    #
    # Output:
    #   Returns the encrypted letters as a string.
    #
    ############################################################################    
    def EncryptPair(self, pair):
        char1_loc, char2_loc = [self.key_table.find(x) for x in pair]
        # This handles vertical cases
        if char1_loc % 5 is char2_loc % 5:
            char1_loc = (char1_loc + 5) % 25
            char2_loc = (char2_loc + 5) % 25
        # This handles horizontal cases
        elif char1_loc / 5 is char2_loc / 5:
            char1_loc = char1_loc + 1 if (char1_loc + 1) % 5 is not 0 else char1_loc - 4
            char2_loc = char2_loc + 1 if (char2_loc + 1) % 5 is not 0 else char1_loc - 4
        # This handles box cases
        else:
            char1_loc, char2_loc = self.HandleBoxPair(char1_loc, char2_loc)
        return self.key_table[char1_loc] + self.key_table[char2_loc]

    ############################################################################
    #
    # Function: DecryptPair
    #
    # Purpose: Decrypts each letter pair based off the rules of their locations
    #           in the key table.
    #
    # Input:
    #   pair -- tuple (char, char): A tuple of chars that need to be encrypted
    #
    # Output:
    #   Returns the decrypted letters as a string.
    #
    ############################################################################
    def DecryptPair(self, pair):
        char1_loc, char2_loc = [self.key_table.find(x) for x in pair]
        # This handles vertical cases
        # If char_loc - 5 is negative we need to wrap around to the other side
        #  of the table
        if char1_loc % 5 is char2_loc % 5:
            char1_loc = char1_loc - 5 if char1_loc - 5 >=0 else char1_loc + 20
            char2_loc = char2_loc - 5 if char2_loc - 5 >=0 else char2_loc + 20
        # This handles horizontal cases
        # If char_loc -1 if less than char_loc / 5 we need to wrap around
        elif char1_loc / 5 is char2_loc / 5:
            char1_loc = char1_loc - 1 if char1_loc - 1 >= char1_loc / 5 else char1_loc + 4
            char2_loc = char2_loc - 1 if char2_loc - 1 >= char2_loc / 5 else char2_loc + 4
        # This handles box cases
        else:
            char1_loc, char2_loc = self.HandleBoxPair(char1_loc, char2_loc)
        return self.key_table[char1_loc] + self.key_table[char2_loc]

    ############################################################################
    #
    # Function: Encrypt
    #
    # Purpose: Gets the letter pairs and returns the encrypted string
    #
    # Input:
    #   plaintext -- string: Text to be encrypted
    #
    # Output:
    #   Returns the plaintext encrypted
    #
    ############################################################################
    def Encrypt(self, plaintext):
        plaintext = self.PrepStringForCipher(plaintext)
        return ''.join([self.EncryptPair(x) for x in self.CreatePairs(plaintext)])

    ############################################################################
    #
    # Function: Decrypt
    #
    # Purpose: Gets the letter pairs and returns the decrypted string
    #
    # Input:
    #   ciphertext -- string: Text to be decrypted
    #
    # Output:
    #   Returns the decrypted ciphertext
    #
    ############################################################################
    def Decrypt(self, ciphertext):
        ciphertext = self.PrepStringForCipher(ciphertext)
        return ''.join([self.DecryptPair(x) for x in self.CreatePairs(ciphertext)])
    
################################################################################
#
# end Playfair Cipher
#
################################################################################

################################################################################
#
# Vigenre Cipher
#
################################################################################
class VigenreCipher(CipherInterface):
    ############################################################################
    #
    # Function: PrepStringForCipher
    #
    # Purpose: Removes all nonalpha chars from text
    #
    # Input:
    #   text -- string: Text that will get encrypted
    #
    # Output:
    #   text -- string: The input text with all nonalpha chars removed
    #
    ############################################################################
    def PrepStringForCipher(self, text):
        # Ensure everything is lowercase that why .lower() is called
        #  Also removes spaces and non-alpha chars
        text = re.sub(r'[\W0-9 ]+', '', text.lower())
        return text

    ############################################################################
    #
    # Function: SetKey
    #
    # Purpose: Sets the key property for the class as well the the loc_in_key
    #           property and reset key loc
    #
    # Input:
    #  key  -- string: Key for cipher
    #
    # Output:
    #   None
    #
    ############################################################################
    def SetKey(self, key):
        self.key = self.PrepStringForCipher(key)
        self.loc_in_key = 0
        self.reset_key_loc = False

    ############################################################################
    #
    # Function: EncryptLetter
    #
    # Purpose: Encrypts the letter wth its matching letter from the key
    #
    # Input:
    #   plaintext -- char: Letter to be encrypted
    #   key -- char: Letter from key to be used in encryption
    #
    # Output:
    #   Returns the encrypted letter
    #
    ############################################################################
    def EncryptLetter(self, plaintext):
        if self.reset_key_loc:
            self.loc_in_key = 0
            self.reset_key_loc = False
        # a = ord(plaintext) - 97 normalizes value
        # b = ord(self.key[self.loc_in_key]) - 97 normalizes that value
        # c = a + b gives us our offset
        # d = c % 26 to catch overflow
        # e = d + 97 puts value back into lowercase ascii range
        encrypted = chr((((ord(plaintext) - 97) + (ord(self.key[self.loc_in_key]) - 97)) % 26) + 97)
        self.loc_in_key = (self.loc_in_key + 1) % len(self.key)
        return encrypted

    ############################################################################
    #
    # Function: DecryptLetter
    #
    # Purpose: Encrypts the letter wth its matching letter from the key
    #
    # Input:
    #   plaintext -- char: Letter to be encrypted
    #   key -- char: Letter from key to be used in encryption
    #
    # Output:
    #   Returns the encrypted letter
    #
    ############################################################################
    def DecryptLetter(self, plaintext):
        if self.reset_key_loc:
            self.loc_in_key = 0
            self.reset_key_loc = False
        decrypted = chr((ord(plaintext) - 97) - (ord(self.key[self.loc_in_key]) - 97) + 97) if (ord(plaintext) - 97) - (ord(self.key[self.loc_in_key]) - 97) >=0 else chr((ord(plaintext) - 97) - (ord(self.key[self.loc_in_key]) - 97) + 26 + 97)
        self.loc_in_key = (self.loc_in_key + 1) % len(self.key)
        return decrypted
    
    ############################################################################
    #
    # Function: Encrypt
    #
    # Purpose: Encrypts the inputted plain text
    #
    # Input:
    #   plaintext -- string: Text to be encrypted
    #
    # Output:
    #   Returns encrypted version of plaintext
    #
    ############################################################################
    def Encrypt(self, plaintext):
        encrypted = ''.join([self.EncryptLetter(x) for x in self.PrepStringForCipher(plaintext)])
        self.reset_key_loc = True
        return encrypted

    ############################################################################
    #
    # Function: Decrypt
    #
    # Purpose: Decrypt the inputted cipher text
    #
    # Input:
    #   plaintext -- string: Text to be decrypted
    #
    # Output:
    #   Returns decrypted version of ciphertext
    #
    ############################################################################
    def Decrypt(self, ciphertext):
        decrypted = ''.join([self.DecryptLetter(x) for x in self.PrepStringForCipher(ciphertext)])
        self.reset_key_loc = True
        return decrypted
        
################################################################################
#
# end Vigenre Cipher
#
################################################################################

a = VigenreCipher()
a.SetKey('playfair example')
b = (a.Encrypt('Hide the gold in the tree stump'))
print b
print a.Decrypt(b)
