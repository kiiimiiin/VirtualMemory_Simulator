import SList

class HashChaining:
    def __init__(self, size):
        self.tablesize = size
        self.array = []
        for i in range(size):
            self.array.append(SList.SList())

    def hash(self, key):
        return key % self.tablesize

    def insert(self, key, value):
        index = self.hash(key)
        self.array[index].insert_front((key, value))

    def search(self, key):
        index = self.hash(key)
        slist = self.array[index]
        target = slist.head
        while target:
            (tkey, tvalue) = target.item
            if tkey == key:
                return tvalue
            target = target.next
        return None

    def print_table(self):
        for index in range(len(self.array)):
            slist = self.array[index]
            print("Index", index, ":", end=" ")
            slist.print_list()
    
    def remove(self, key): # item 반환
        index = self.hash(key)
        slist = self.array[index]
        node = slist.delete_target((key,self.search(key))) # node 반환
        if node:
            return node.item
        return None
    
    def get_table_as_text(self): # 시뮬레이터 출력을 위한 텍스트, 인덱스내 갯수 추출 
        result = ""
        count = 0
        for index in range(len(self.array)):
            slist = self.array[index]
            result += f"Index {index}: "
            (text, count_in_index) = slist.get_list_as_text() 
            result += f"{text}\n"
            count += count_in_index
        return result, count

if __name__ == "__main__":
    hash_table = HashChaining(10)
    hash_table.insert(5, "apple")
    hash_table.insert(15, "apple")
    hash_table.insert( 7, "cherry")
    hash_table.insert(10, "kiwi")

    hash_table.print_table()

    print("\nRemoving key 5:")
    removed = hash_table.remove(5)
    print("Removed:", removed)

    print(hash_table.search(5))   
    print(hash_table.search(7))  
    print(hash_table.search(10))  
    print(hash_table.search(11))  

    hash_table.print_table()



