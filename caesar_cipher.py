from ciphers import CipherInterface
import re

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
    # Function: SetKey
    #
    # Purpose: Sets key for cipher
    #
    # Input:
    #   key -- string: String representing the numerical amount to rotate by
    #
    # Output: Nothing
    #
    # This will be overwritten in subclasses
    #
    ############################################################################
    def SetKey(self, key):
        # Mod by 26 to keep within proper range
        self.key = int(key) % 26
    
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

a = CaesarCipher()
b = a.Encrypt('test')
print b
print a.Decrypt(b)
