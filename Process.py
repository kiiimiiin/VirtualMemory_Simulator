import HashPageTable

PAGE_SIZE = 4096  # 단위: 비트 -> 4KB

class Page:
    def __init__(self, logical_address, page_number):
        self.logical_address = logical_address # 페이지의 첫번째 논리주소
        self.page_number = page_number
        
    def __str__(self):
        return f"Logical Address: {self.logical_address}, Page Number: {self.page_number}"

class Process:
    def __init__(self, process_id, page_count):
        self.process_id = process_id
        self.page_count = page_count
        self.hash_table_size = self.page_count // 4  # 해쉬페이지 테이블 크기를 프로세스가 가진 페이지의 갯수보다 작게 만듦
        self.pagetable = HashPageTable.HashPageTable(self.hash_table_size)
        self.pages = []
        for page_number in range(page_count):
            logical_address = page_number * PAGE_SIZE
            self.pages.append(Page(logical_address, page_number))

    def __str__(self):
        return f"Process ID: {self.process_id}, Page Count: {self.page_count}, Pagetable Size: {self.hash_table_size}"
    
    def get_virtual_memory_text(self):
        virtual_memory_text = f"Process ID: {self.process_id}, Page Count: {self.page_count} \n"
        for page in self.pages:
            virtual_memory_text += str(page) + "\n"
        return virtual_memory_text


if __name__ == "__main__":
    process_a = Process(1, 10)  
    process_b = Process(2, 20)  

    print(process_a)
    print(process_b)

    for page in process_a.pages:
        print(page)

    for page in process_b.pages:
        print(page)
    print(process_a.get_virtual_memory_text())