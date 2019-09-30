import bcrypt

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


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        salt = bcrypt.gensalt()
        key = bcrypt.hashpw(b"test", salt)
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
        if self.value >= self.capacity:
            self.resize()
        for i in range(self.value, key, -1):
            self.storage[i] = self.storage[i-1]

        self.storage[value] = key
        self.value += 1



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pass


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        pass


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.value):
            new_storage[i] = self.storage[i]
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
print(newHT._hash('four'))

#test = "hellos"

#test.encode('utf-8')
# gensalt will be different every time it runs
#salt = bcrypt.gensalt()
#print(bcrypt.hashpw(b"test", salt))


