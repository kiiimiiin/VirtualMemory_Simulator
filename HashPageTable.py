import HashChaining

class HashPageTable:
    def __init__(self, table_size):
        self.page_table = HashChaining.HashChaining(table_size)

    def page_to_frame(self, page_number, frame_number):
        self.page_table.insert(page_number, frame_number)

    def get_frame_number(self, page_number):
        return self.page_table.search(page_number)
    
    def remove_page(self, page_number):
        ( page_number, frame_number ) = self.page_table.remove(page_number)
        return frame_number     
    def print_table(self):
        self.page_table.print_table()
    
    def get_table_as_text(self):  # 시뮬레이터 출력을 위함 
        return self.page_table.get_table_as_text()

if __name__ == "__main__":
    page_table = HashPageTable(10)  # 페이지 테이블 크기는 10

    page_table.page_to_frame(5, 20)
    page_table.page_to_frame(15, 30)
    page_table.page_to_frame(7, 40)
    page_table.page_to_frame(10, 50)

    page_table.print_table()

    print("Frame number for page 5:", page_table.get_frame_number(5))
    print("Frame number for page 7:", page_table.get_frame_number(7))
    print("Frame number for page 11:", page_table.get_frame_number(11))

    page_table.page_table.print_table()