from scheme_oracle import KeyOracleRFC3526
from biquad_distinguisher import BiquadDistinguisher

if __name__ == "__main__":
    p = next_prime(2^16)
    while(p % 4 != 3):
        p = next_prime(p)

    no_of_queries = 2^16
    
    my_oracle = KeyOracleRFC3526(p)
    my_distinguisher = BiquadDistinguisher(my_oracle)

    my_distinguisher.distinguish(no_of_queries)

    
    
