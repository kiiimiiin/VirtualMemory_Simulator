import Queue

FRAME_SIZE = 4096  # 단위: 비트 -> 4KB

class Frame:
    def __init__(self, physical_address, frame_number, linked_process, linked_page):
        self.physical_address = physical_address # 프레임의 첫번째 논리주소
        self.frame_number = frame_number
        self.linked_process = linked_process
        self.linked_page = linked_page

    def __str__(self):
        if self.linked_process and self.linked_page:
            linked_process_id = self.linked_process.process_id
            linked_page_number = self.linked_page.page_number
        else:
            linked_process_id = None
            linked_page_number = None
        return f"Physical Address: {self.physical_address}, Frame Number: {self.frame_number}, Linked Process: {linked_process_id}, Linked Page: {linked_page_number}"

class FrameTable:
    def __init__(self, frame_count):
        self.frame_count = frame_count
        self.frames = []
        self.queue = Queue.Queue()
        for frame_number in range(frame_count):
            physical_address = frame_number * FRAME_SIZE
            self.frames.append(Frame(physical_address, frame_number, None, None))
    def print_table(self):
        for frame in self.frames:
            print(frame)
    
    def get_table_as_text(self): # 시뮬레이터 출력을 위한 텍스트 추출 
        table_text = ""
        for frame in self.frames:
            table_text += str(frame) + "\n"
        return table_text
    


if __name__ == "__main__":
    frame_count = 10 
    frame_table = FrameTable(frame_count)
    frame_table.print_table()
