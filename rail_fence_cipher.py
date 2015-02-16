from cipher_interface import CipherInterface
import re
################################################################################
#
# RailFenceCipher
#
################################################################################
class RailFenceCipher(CipherInterface):
    ############################################################################
    #
    # Function: SetKey
    #
    # Purpose: Sets key for cipher
    #
    # Input:
    #   key -- string: number of rails in cipher
    #
    # Output: Nothing
    #
    # This will be overwritten in subclasses
    #
    ############################################################################
    def SetKey(self, key):
        self.num_rails = int(key)

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
        rails = []
        plaintext = self.PrepStringForCipher(plaintext)
        for i in range(self.num_rails):
            rails.append('')

        i = 0
        while i < len(plaintext):
            rails[i % self.num_rails] += plaintext[i]
            i += 1
        return ''.join(rails)

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
        rails = []
        ciphertext = self.PrepStringForCipher(ciphertext)
        plaintext = ''
        row_len = len(ciphertext) / self.num_rails
        row_start = 0
        row_end = row_len + (len(ciphertext) % self.num_rails)
        for i in range(self.num_rails):
            rails.append('')
            rails[i] = ciphertext[row_start:row_end]
            row_start = row_end
            row_end += row_len

        i = 0
        while len(plaintext) is not len(ciphertext):
            for rail in rails:
                if i < len(rail):
                    plaintext += rail[i]
            i += 1
        return plaintext
################################################################################
#
# end RailFenceCipher
#
################################################################################
