# '''
# Linked List hash table key/value pair
# '''
# We can use most of the array stuff for the insert, remove, and resize portion of the hashtable because I guess it's gonna be an array now
# use bcrypt to create the hash (we want to do this first)
# then do the array stuff (resizing, adding, removing) hashes
# step 1
# use bcrypt to create a hash
# step 2
# everything else
# don't worry about duplicates until tomorrow
# linked pair is for tomorrow
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        
        if self.storage[index] is not None:
            print("Warning: Index collision")
            return
        
        self.storage[index] = LinkedPair(key, value)
        return self.storage[index]

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is None:
            print("Warning: Key not found")
            return
        self.storage[index] = None
        
        pass


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        pair = self.storage[index]
        print(pair)
        if pair is None:
            return None
        else:
            return self.storage[index]


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity

        for pair in self.storage:
            if pair is None:
                new_index = self._hash_mod(pair.key)
                new_storage[new_index] = pair

        self.storage = new_storage
            


'''
if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
'''
newHT = HashTable(4)
print(newHT.insert('key-0', 'val-0'))
print(newHT.retrieve('key-0'))
#test.encode('utf-8')
# gensalt will be different every time it runs
#salt = bcrypt.gensalt()
#print(bcrypt.hashpw(b"test", salt))


