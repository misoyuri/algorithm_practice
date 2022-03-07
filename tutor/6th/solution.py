"""
Project 6
CSE 331 S22 (Onsay)
Andrew McDonald and Aaron Jonckheere
solution.py
"""

from typing import TypeVar, List, Tuple, Generator

T = TypeVar("T")
HashNode = TypeVar("HashNode")
HashTable = TypeVar("HashTable")


class HashNode:
    """
    Implements a hashnode object.

    Properties
    - key: [str] lookup key of hashnode
    - value: [T] lookup value associated to key
    """
    __slots__ = ["key", "value"]

    def __init__(self, key: str, value: T) -> None:
        """
        Constructs a hashnode object.
        DO NOT EDIT.

        Time: O(1)
        Space: O(1)

        :param key: [str] lookup key of hashnode.
        :param value: [T] lookup value associated to key.
        """
        self.key: str = key
        self.value: T = value

    def __str__(self) -> str:
        """
        Represents the HashNode as a string.
        DO NOT EDIT.

        Time: O(1)
        Space: O(1)

        :return: [str] String representation of the hashnode.
        """
        return f"HashNode({self.key}, {self.value})"

    __repr__ = __str__  # alias the repr operator to call str https://stackoverflow.com/a/14440577

    def __eq__(self, other: HashNode) -> bool:
        """
        Implement the equality operator to compare HashNode objects.
        DO NOT EDIT.

        Time: O(1)
        Space: O(1)

        :param other: [HashNode] hashnode we are comparing with this one.
        :return: [bool] True if equal, False if not.
        """
        return self.key == other.key and self.value == other.value


class HashTable:
    """
    Implements a hashtable for fast insertion and lookup.
    Maintains ordering such that iteration returns items in the order they were inserted.
    Inspired by Raymond Hettinger's proposed implementation @
    https://code.activestate.com/recipes/578375/.
    Quoting from Raymond Hettinger,

        The current memory layout for dictionaries is unnecessarily inefficient.
        It has a sparse table of 24-byte entries containing
        the hash value, key pointer, and value pointer.
        Instead, the 24-byte entries should be stored in a
        dense table referenced by a sparse table of indices.
        For example, the dictionary:

        d = {'timmy': 'red', 'barry': 'green', 'guido': 'blue'}

        is currently stored as:

        entries = [['--', '--', '--'],
                   [-8522787127447073495, 'barry', 'green'],
                   ['--', '--', '--'],
                   ['--', '--', '--'],
                   ['--', '--', '--'],
                   [-9092791511155847987, 'timmy', 'red'],
                   ['--', '--', '--'],
                   [-6480567542315338377, 'guido', 'blue']]

        Instead, the data should be organized as follows:

        indices =  [None, 1, None, None, None, 0, None, 2]
        entries =  [[-9092791511155847987, 'timmy', 'red'],
                    [-8522787127447073495, 'barry', 'green'],
                    [-6480567542315338377, 'guido', 'blue']]

    Properties
    - indices: [list] a table into which keys are hashed, storing the
                      index of the associated value in self.entries
    - entries: [list] a table onto which values are appended, and
                      referenced by integers in indices
    - prime_index: [int] index of current prime in Hashtable.PRIMES
    - capacity: [int] length of self.indices
    - size: [int] number of entries in self.entries
    """
    __slots__ = ["indices", "entries", "prime_index", "capacity", "size"]

    # set constants
    FREE = -1
    DELETED = -2
    PRIMES = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
        89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
        181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
        281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
        397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
        503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
        743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
        863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
        997)

    def __init__(self, capacity: int = 8) -> None:
        """
        Initializes HashTable.
        DO NOT EDIT.

        Time: O(c) where c = capacity
        Space: O(c) where c = capacity

        :param capacity: [int] Starting capacity of the hashtable,
                               i.e., starting length of the indices table.
        """
        # create underlying data structures
        self.indices: List[int] = [self.FREE] * capacity  # a sparse table of indices
        self.entries: List[HashNode] = []  # a dense table of HashNodes
        self.capacity: int = capacity
        self.size: int = 0
        # set prime index for hash computations
        i = 0
        while HashTable.PRIMES[i] <= self.capacity:
            i += 1
        self.prime_index: int = i - 1

    def __eq__(self, other: HashTable) -> bool:
        """
        Implement the equality operator to compare HashTable objects.
        DO NOT EDIT.

        Time: O(c + s) where c = capacity and s = size
        Space: O(c + s) where c = capacity and s = size

        :param other: [HashTable] hashtable we are comparing with this one.
        :return: [bool] True if equal, False if not.
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        # the following line allows the underlying structure of the hashtables
        # to differ, as long as the items in each table are equivalent
        return list(self.items()) == list(other.items())

    def __str__(self) -> str:
        """
        Represents the HashTable as a string.
        DO NOT EDIT.

        Time: O(c + s) where c = capacity and s = size
        Space: O(c + s) where c = capacity and s = size

        :return: [str] String representation of the hashtable.
        """
        representation = [f"Size: {self.size}\nCapacity: {self.capacity}\nIndices: ["]
        for i in range(self.capacity):
            action = "FREE" if self.indices[i] == self.FREE \
                    else "DELETED" if self.indices[i] == self.DELETED \
                    else f'{self.indices[i]}: {self.entries[self.indices[i]]}'
            representation.append(f"[{i}]: " + action)
        representation.append("]\nEntries: [")
        for i in range(self.size):
            representation.append(f"[{i}]: {self.entries[i]}")
        representation.append("]")
        return "\n".join(representation)

    __repr__ = __str__  # alias the repr operator to call str https://stackoverflow.com/a/14440577

    def __len__(self):
        """
        Returns number of elements in the hashtable.
        DO NOT EDIT.

        Time: O(1)
        Space: O(1)

        :return: [int] Number of elements in the hashtable.
        """
        return self.size

    def _hash_1(self, key: str) -> int:
        """
        Converts a key into an initial bin number for double probing.
        DO NOT EDIT.

        Time: O(1)
        Space: O(1)

        :param key: [str] Key to be hashed.
        :return: [int] Initial bin number for double probing, None if key is an empty string.
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)
        return hashed_value % self.capacity

    def _hash_2(self, key: str) -> int:
        """
        Converts a key into a step size for double probing.
        DO NOT EDIT.

        Time: O(1)
        Space: O(1)

        :param key: [str] Key to be hashed.
        :return: [int] Double probing step size, None if key is an empty string.
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)

        prime = HashTable.PRIMES[self.prime_index]
        hashed_value = prime - (hashed_value % prime)
        if hashed_value % 2 == 0:
            hashed_value += 1
        return hashed_value

    ###############################################################################################
    # IMPLEMENT BELOW
    ###############################################################################################

    def _hash(self, key: str, inserting: bool = False) -> int:
        """
        Given a key string, return an index in self.indices, and should probe with double hashing
        :param key: the key being used in hash function
        :param inserting: doing insertion if True, no insertion otherwise
        :return: int at which self.indices[i] is freed or deleted for insertion,
                 or refers to HashNode at self.entries[self.indices[i]]
        """
        ret = self._hash_1(key)
        
        if ret is None:
            ret = self._hash_2(key)
        
        if inserting is True:
            self.entries[ret] 
        
        return ret
    def _insert(self, key: str, value: T) -> None:
        """
        Use the key and value parameter to add an entry to the hashtable
        :param key: key associated with the value we are storing
        :param value: value we are sotring
        :return: None
        """

        
        hash_address = self._hash_1(key)
        
        if self.indices[hash_address] >= 0:
            print("indices:", self.indices[hash_address])
            self.entries[self.indices[hash_address]].value = value
        
        else:
            if self.indices[hash_address] != -1:
                # hash_address = self._hash_2(key)
                hash_address += 1
            new_hash = HashNode(key, value)
            self.entries.append(new_hash)
            self.indices[hash_address] = self.size
            print("Hash Addr 1:", hash_address)
            print("Hash Addr 2:", self._hash_2(key))
            
            self.size += 1
        
            if self.size >= self.capacity / 2:
                self._grow()
        return None

    def _get(self, key: str) -> HashNode:
        """
        Find HashNode with the given key in the hashtable
        :param key: key we are looking up
        :return: HashNode with the key we looked up
        """
        pass

    def _delete(self, key: str) -> None:
        """
        Removes the HashNode with the given key from the hashtable
        :param key: key of the Node we are lookng to delete
        :return: None
        """
        pass

    def _grow(self) -> None:
        """
        Double the capacity of the existing hash table
        :return: None
        """
        self.capacity *= 2
        new_indices = [self.FREE] * self.capacity
        
        i = 0
        while HashTable.PRIMES[i] <= self.capacity:
            i += 1
        self.prime_index = i - 1
        
        for idx, hash_node in enumerate(self.entries):
            new_indices[self._hash_1(hash_node.key)] = idx
            
        self.indices = new_indices

    def __setitem__(self, key: str, value: T) -> None:
        """
        DOCSTRING, with function description, complete :param: tags, and a :return: tag.
        """
        pass

    def __getitem__(self, key: str) -> T:
        """
        DOCSTRING, with function description, complete :param: tags, and a :return: tag.
        """
        pass

    def __delitem__(self, key: str) -> None:
        """
        DOCSTRING, with function description, complete :param: tags, and a :return: tag.
        """
        pass

    def __contains__(self, key: str) -> bool:
        """
        DOCSTRING, with function description, complete :param: tags, and a :return: tag.
        """
        pass

    def update(self, pairs: List[Tuple[str, T]]) -> None:
        """
        DOCSTRING, with function description, complete :param: tags, and a :return: tag.
        """
        pass

    def keys(self, reverse: bool = False) -> Generator[str, None, None]:
        """
        DOCSTRING, with function description, complete :param: tags, and a :return: tag.
        """
        pass

    def values(self, reverse: bool = False) -> Generator[T, None, None]:
        """
        DOCSTRING, with function description, complete :param: tags, and a :return: tag.
        """
        pass

    def items(self, reverse: bool = False) -> Generator[Tuple[str, T], None, None]:
        """
        DOCSTRING, with function description, complete :param: tags, and a :return: tag.
        """
        pass

    def clear(self) -> None:
        """
        DOCSTRING, with function description, complete :param: tags, and a :return: tag.
        """
        pass


class DiscordDestroyer:
    """
    Implements a DiscordDestroyer post management system.
    It will be far better than Discord, Destroying Discord in the long run.
    This is only the beginning.

    Properties
    - posts_by_id: Hashtable mapping id strings to post strings
    - ids_by_user: Hashtable mapping user strings to list of Hashtable of posts from that user
    - post_id_seed: Starting value for post id
    """
    __slots__ = ["posts_by_id", "ids_by_user", "post_id_seed"]

    def __init__(self):
        """
        Initializes DiscordDestroyer class.
        DO NOT EDIT.

        Time: O(1)
        Space: O(1)

        :return: None
        """
        self.posts_by_id: HashTable = HashTable()
        self.ids_by_user: HashTable = HashTable()
        self.post_id_seed: int = 0

    def generate_post_id(self, user: str, message: str) -> str:
        """
        Creates a unique post id for each post.
        DO NOT EDIT.

        Time: O(1)
        Space: O(1)

        :return: [str] post id for the post.
        """
        post_id = hash(user + message + str(self.post_id_seed))
        self.post_id_seed += 1
        return str(post_id)

    ###############################################################################################
    # IMPLEMENT BELOW
    ###############################################################################################

    def post(self, user: str, message: str) -> str:
        """
        DOCSTRING, with function description, complete :param: tags, and a :return: tag.
        """
        pass

    def delete_post(self, user_post_id: str) -> bool:
        """
        DOCSTRING, with function description, complete :param: tags, and a :return: tag.
        """
        pass

    def get_most_recent_posts(self, v: int) -> Generator[Tuple[str, str], None, None]:
        """
        DOCSTRING, with function description, complete :param: tags, and a :return: tag.
        """
        pass

    def get_posts_by_user(self, user: str) -> Generator[Tuple[str, str], None, None]:
        """
        DOCSTRING, with function description, complete :param: tags, and a :return: tag.
        """
        pass
