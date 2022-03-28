from .random_prime import get_prime_numbers
from .lambda_n import lambda_n
from .find_e import find_e
from .ext_euclidean import ext_euclidean

def create_rsa_key(length):
    """Funktio, joka tuottaa rsa-avaimen.

    Parametrit:
        Avaimen toivottu bittipituus.

    Palautusarvo:
        Monikko, jossa avaimeen kuuluvat osiot n ja e.
    """

    (p,q) = get_prime_numbers(length)
    n = p*q
    l_n = lambda_n(p,q)
    e = find_e(l_n)
    d = ext_euclidean(l_n, e)
    print('n', n)
    print('l_n', l_n)
    print('e', e)
    print('d', d)
    return (n,e,d)
