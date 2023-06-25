class Hash_Table:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_Method(self,key):
        hash = 0
        for i, j in enumerate(key):
            hash = (hash + ord(j) * i) % len(self.data)
        return hash
    
    def set(self, key, value):
        address = self.hash_Method(key)
        
        if self.data[address] is None:
            self.data[address] = []
        
        self.data[address].append([key,value])
        return self.data

    def get(self, key):
        address = self.hash_Method(key)
        current_Bucket  = self.data[address]

        if current_Bucket:
            for i in current_Bucket:
                if i[0] == key:
                    return i[1]
        return None

    def remove(self, key):
        address = self.hash_Method(key)
        current_Bucket = self.data[address]

        if current_Bucket:
            for i in range(len(current_Bucket)):
                if current_Bucket[i][0] == key:
                    value = current_Bucket.pop(i)

                    # I do not think this need 
                    # for j in range(i+1, len(current_Bucket)):
                    #     current_Bucket[j - 1] = current_Bucket[j]
                    if len(current_Bucket) == 0:
                        self.data[address] = None
                    return value
                
    def search(self, key):
        address = self.hash_Method(key)
        current_Bucket = self.data[address]

        if current_Bucket:
            for i in range(len(current_Bucket)):
                if current_Bucket[i][0] == key:
                    print(f"current_Bucket: {current_Bucket}")
                    return current_Bucket[i][1]
        return None
def object_hash():
    my_hash = Hash_Table(1000)
    return my_hash

def update_hash(objec_hash, key, data):
    objec_hash.set(key, data)
    return objec_hash

def hash_search(key, hash):
    lista = hash.search(key)
    if lista:
        return lista
    return lista
# Myhash = Hash_Table(50)
# Myhash.set("Diego","1990")
# Myhash.set("Mariana","1990")
# Myhash.set("Alejandra","2000")
# Myhash.remove("Diego")
# Myhash.remove("Mariana")
# print(Myhash.data)

