import re
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
################################################################################
#
# end CipherInterface
#
################################################################################
