# This class is for a chaining hash table.
# Collisions are handled via chaining
class ChainingHashTable:

    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Hash key and return hashed value
    # O(1)
    def hash_key(self, key):
        return hash(key) % len(self.table)

    # Insert value into hash table
    # O(N)
    def insert(self, key, value):
        # add bucket to list
        bucket_list = self.table[self.hash_key(key)]

        # if key exists, update key
        for k in bucket_list:
            if k[0] == key:
                k[1] = value
                return True

        # add value to end of bucket list if new key
        bucket_list.append([key, value])
        return True

    # Search for key in table using hashed key
    # return value if key found
    # O(N)
    def search_key(self, key):
        b = self.hash_key(key)
        for entry in self.table[b]:
            if entry[0] == key:
                return entry[1]

    # Function to return all values of a table
    # O(N^2)
    def get_values(self):
        values = []
        for i in range(self.table.__len__()):
            for j, k in self.table.__getitem__(i):
                values.append(k)
        return values

    # Remove entry from table if key found
    # O(N)
    def remove_entry(self, key):
        entry_key = self.hash_key(key)
        entry_exists = False
        bucket = self.table[entry_key]
        for i, j in enumerate(bucket):
            ky, val = j
            if key == ky:
                entry_exists = True
            if entry_exists:
                del bucket[i]
