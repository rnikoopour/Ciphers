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
