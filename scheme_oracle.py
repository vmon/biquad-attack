# This file was *autogenerated* from the file scheme_oracle.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_4 = Integer(4)
"""
When queried generates the random public key for RFC 3526 Protocol.

AUTHORS::
    vmon - 2012 Initial version.
"""

class KeyOracleRFC3526(object):
    """
    The protocol goes as follows. 
        - Let p = 3 (4) and q = (p-1) prime
        - g(+)0  = Z_q (+) Z_2 such that g generate Z_q
        - choose random even r in [0, p]
        - X = g^x
        - send either P-X or X

    """
    def __init__(self, p):
        """
        Just set the base module of the protocol and find g
        """
        assert(p % _sage_const_4  == _sage_const_3 )
        self.mod_p = p 
        self.quad_gen = primitive_root(p)**_sage_const_2  #self._quad_gen should be quadratic residue to be in Z_q subgroup of Z_q (+) Z_2
        

    def key_query(self):
        """
        - generate a random integer r between [0,p] and decrease it 1
        if not even.
        - compute X = g^r

        - flip a coin and either return P or P-X
        """
        r = randint(_sage_const_0 , self.mod_p - _sage_const_1 )
        if r % _sage_const_2 : r -= _sage_const_1 
        X = self.quad_gen**r % self.mod_p
        
        coin_flip = randint(_sage_const_0 ,_sage_const_1 )

        return coin_flip*(self.mod_p - _sage_const_2 *X) + X

    def random_query(self):
        return randint(_sage_const_0 , self.mod_p-_sage_const_1 )
