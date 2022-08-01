# This file consists of function that hashes the string.
import hashlib


def hash_string(s: str, algorithm: str = 'sha256', to_string: bool = True):
    """
    Function  returns a hash object or a HEX string representing the hash
    :param s: string for hashing
    :param algorithm: hashing algorithm (available: 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512')
    :param to_string: if true- returns a HEX string representing the hash, if false- returns hex object
    :return: hashed string or hash object
    """
    # available algorithms
    av_algorithms = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
    # checking the function params
    if not all([isinstance(algorithm, str), isinstance(s, str), isinstance(to_string, bool)]):
        raise ValueError("Wrong types of params")
    # Checking if algorithm in available algorithms
    if algorithm.lower() in av_algorithms:
        try:
            # convert string to bytes
            b_string = str.encode(s)
            # get and return the result
            result = eval('hashlib.' + algorithm)(b_string)
            return result.hexdigest() if to_string is True else result
        except Exception as e:
            print(e, "Cannot hash the string")

    raise ValueError("Such algorithm isn`t available")


if __name__ == "__main__":
    s = "Python Bootcamp"
    print(hash_string(s, to_string=False))  # returns hash object
    print(hash_string(s))  # returns a HEX string representing the hash
