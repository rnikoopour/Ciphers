from cipher_interface import CipherInterface
import re

################################################################################
#
# CAESARCIPHER
#
################################################################################
class CaesarCipher(CipherInterface):
    ############################################################################
    #
    # Function: SetKey
    #
    # Purpose: Sets key for cipher
    #
    # Input:
    #   key -- string: numerical amount to rotate by
    #
    # Output: Nothing
    #
    # This will be overwritten in subclasses
    #
    ############################################################################
    def SetKey(self, key):
        # Mod by 26 to keep within proper range
        self.rot_amount = int(key) % 26
    
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
        return ''.join([chr(((ord(x.lower()) - 97 + self.rot_amount) % 26) + 97) for x in re.sub(r'[\W0-9 ]', '', plaintext.lower())])
    
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
        return ''.join([chr(((ord(x.lower()) - 97 - self.rot_amount) + 97)) if (ord(x.lower()) - 97 - self.rot_amount) >= 0 else chr(((ord(x.lower()) - 97 - self.rot_amount) + 26) + 97) for x in re.sub(r'[\W0-9 ]', '', ciphertext.lower())])
    
################################################################################
#
# end CAESAR CIPHER
#
################################################################################
