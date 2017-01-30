from collections import defaultdict

def total(str):
    valid_set = set(['AU','GC','GU','UA','CG','UG'])
    start = 0
    end = len(str)-1
    opt = defaultdict(int)

    def _total(str,start,end):
        if (start,end) in opt:
            return opt[(start,end)]
        num_struct = 0
        if start == end:      # one element
            return 1
        if start == end + 1:  # (has nothing) after has nothing
            return 1
        for k in xrange(start+1,end+1): # assume first element is "(",check whether has ")" to pair
            if str[start]+str[k] in valid_set:
                num_struct += _total(str,start+1,k-1) * _total(str,k+1,end)
        num_struct += _total(str,start+1,end) # assume first element is "."
        opt[(start,end)] = num_struct
        return num_struct

    return _total(str,start,end)


print total("ACAGU")
print total("AC")
print total("GUAC")
print total("GCACG")
print total("CCGG")
print total("CCCGGG")
print total("UUCAGGA")
print total("AUAACCUA")
print total("UUGGACUUG")
print total("UUUGGCACUA")
print total("GAUGCCGUGUAGUCCAAAGACUUC")
print total("AGGCAUCAAACCCUGCAUGGGAGCG")
