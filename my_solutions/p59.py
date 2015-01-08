#!/Users/yukatherin/Applications/anaconda/bin/python
import pandas as pd
from itertools import product


def decode_char(ascii_code, key):
    return chr(ascii_code|key)

def decode(ss, char_keys_ord):
    k = len(char_keys_ord)
    decoded = []
    n=0
    while True:
        for c_ord in char_keys_ord:
            next_char = decode_char(ss[n],c_ord)
            decoded.append(next_char)
            n+=1
            if n==len(ss):
                return ''.join(decoded)  
 



def p59():
    df = pd.read_csv("p059_cipher.txt", header=None, skiprows=0)
    ss = list(df.iloc[0,:])
    print decode([107],[42])
    # char_range_ord = range(ord('a'), ord('a')+26)
    # for char_keys_ord in product(char_range_ord, char_range_ord, char_range_ord):
    #     decoded = decode(ss, char_keys_ord)
    #     n_char = len(set([c for c in decoded if ord(c)>=ord('a') and ord(c)<=ord('z')]))
    #     if decoded.count("John")>1:
    #         print decoded




if __name__=="__main__":
    p59()