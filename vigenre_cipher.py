from cipher_interface import CipherInterface
################################################################################
#
# Vigenre Cipher
#
################################################################################
class VigenreCipher(CipherInterface):
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
