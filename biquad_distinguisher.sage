"""
A distinguisher for  RFC 3526 Protocol key exchange protocol based
on counting bi-quadratic residue.

AUTHORS::
    vmon - 2012 Initial version.
"""
class BiquadDistinguisher(object):
    """
    Simply query the oracle and see how many times the result is
    biquadratic residue.
    """
    def __init__(self, key_oracle):
        """
        Stores the key_oracle and generate finite field object
        for later computation
        """
        self.key_oracle = key_oracle
        self.public_field = FiniteField(key_oracle.mod_p)
        self.total_order = self.public_field.order() - 1
        

    def distinguish(self, no_of_queries):

        print "Key oracle biquadratic residue ratio:", RR(self.biquadratic_stat(no_of_queries, self.key_oracle.key_query)/no_of_queries)

        print "Random oracle biquadratic residue ratio:", RR(self.biquadratic_stat(no_of_queries, self.key_oracle.random_query)/no_of_queries)

    def biquadratic_stat(self, no_of_queries, query_type):
        """
        Get the query function and count the number of biquadratic residues
        """
        i = no_of_queries
        bi_quad_counter = 0
        while(i):
            X = self.public_field(self.key_oracle.key_query())
            try:
                X.nth_root(4)
                bi_quad_counter +=1
            except:
                pass

            i -= 1

        return bi_quad_counter
