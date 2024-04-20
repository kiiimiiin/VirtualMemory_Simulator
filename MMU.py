import FrameTable
import random
import Process

class MMU:
    def __init__(self, frame_table):
        self.frame_table = frame_table
        self.page_fault_count = 0
        self.fifo_count = 0
        self.display_history = ""

    def randomly_access(self, process): # 프로세스내 페이지와 프레임 랜덤 할당
        chosen_page = random.choice(process.pages)
        frame_number = process.pagetable.get_frame_number(chosen_page.page_number)

        if frame_number != None:  # 이미 프레임에 할당된 페이지에 접근
            self.record_message(f"프로세스{process.process_id} - 페이지 {chosen_page.page_number}를 통해 프레임 {frame_number}에 접근하였습니다.")
        else:  # 페이지가 할당되지 않은 경우
            empty_frames = []  # 비어 있는 프레임을 저장할 빈 리스트 생성
            for frame in self.frame_table.frames:  # 프레임 테이블의 모든 프레임에 대해 반복
                if frame.linked_page is None:  # 프레임이 연결된 페이지가 없는지 확인
                    empty_frames.append(frame)  # 만약 프레임이 비어 있다면 리스트에 추가
            
            if empty_frames:  # 비어있는 프레임이 있을 경우 할당
                chosen_frame = random.choice(empty_frames)
                chosen_frame.linked_page = chosen_page
                chosen_frame.linked_process = process
                process.pagetable.page_to_frame(chosen_page.page_number, chosen_frame.frame_number)
                self.frame_table.queue.enqueue(chosen_frame)  # FIFO 페이지 교체를 위함
                self.record_message(f"프로세스{process.process_id} - 페이지 {chosen_page.page_number}를 프레임 {chosen_frame.frame_number}에 할당했습니다. (Page fault)")
                self.page_fault_count += 1
            else:  # 비어있는 프레임이 없을 경우 FIFO 페이지 교체 알고리즘
                oldest_frame = self.frame_table.queue.dequeue()
                oldest_process = oldest_frame.linked_process
                oldest_page = oldest_frame.linked_page
                removed_frame_number = oldest_process.pagetable.remove_page(oldest_page.page_number)
                
                if removed_frame_number != None:
                    oldest_frame.linked_page = chosen_page
                    oldest_frame.linked_process = process
                    process.pagetable.page_to_frame(chosen_page.page_number, removed_frame_number)
                    self.frame_table.queue.enqueue(oldest_frame)
                    self.record_message(f"FIFO 페이지교체: 프로세스{process.process_id} - 페이지 {chosen_page.page_number}를 프로세스 {oldest_process.process_id}의 페이지 {oldest_page.page_number}를 제거하고 프레임 {removed_frame_number}에 할당했습니다. (Page fault)")
                    self.page_fault_count += 1
                    self.fifo_count += 1

                else:
                    self.record_message(f"FIFO 페이지교체: 프로세스{oldest_process.process_id} - 페이지 {oldest_page.page_number}의 프레임을 제거하는 데 실패했습니다.")       

    def record_message(self, message): # 시뮬레이터 디스플레이를 위한 text 누적
        print(message)
        self.display_history += message + "\n"
        
    def get_history_as_text(self):
        return self.display_history

if __name__ == "__main__":
    frametable = FrameTable.FrameTable(4)
    process_a = Process.Process(1, 4)
    process_b = Process.Process(2, 4)
    mmu = MMU(frametable)
    
    for i in range(10):
        mmu.randomly_access(process_a)
        mmu.randomly_access(process_a)
        mmu.randomly_access(process_b)
    mmu.frame_table.print_table()
    process_a.pagetable.print_table()
    process_b.pagetable.print_table()