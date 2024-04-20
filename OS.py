import MMU
import Process
import FrameTable
import random

class OperatingSystem:
    def __init__(self, frame_count, process_count, page_count_per_process, random_mode=False):
        self.frame_table = FrameTable.FrameTable(frame_count)
        self.processes = []
        for process_id in range(process_count): # 프로세스 생성
            if random_mode:
                page_count = random.randint(4, page_count_per_process)
            else:
                page_count = page_count_per_process
            process = Process.Process(process_id, page_count)
            self.processes.append(process)
        
    def run_simulation(self, simulation_steps): 
        mmu = MMU.MMU(self.frame_table)
        simulation_result = ""
        for i in range(simulation_steps):
            process = random.choice(self.processes)
            mmu.randomly_access(process)
        page_fault_count = mmu.page_fault_count
        fifo_count = mmu.fifo_count
        simulation_result += f"전체 페이지 폴트 횟수 : {page_fault_count}번\n"
        simulation_result += f"FIFO 페이지 교체 알고리즘으로 인한 페이지 폴트 횟수 : {fifo_count}번\n"
        simulation_result += f"순수 할당으로 인한 페이지 폴트 횟수 : {page_fault_count - fifo_count}번\n\n"
        simulation_result += mmu.display_history
        return simulation_result

    def get_frametable_state(self): # 시뮬레이터 출력을 위한 텍스트 추출 
        return self.frame_table.get_table_as_text()
    
    def get_pagetable_state(self):
        pagetable_state = ""
        for process in self.processes:
            pagetable_state += str(process)
            pagetable_text, count = process.pagetable.get_table_as_text()
            pagetable_state += f" Mapping Page Count: {count}\n"
            pagetable_state += pagetable_text
        return pagetable_state
    
    def get_virtual_memory_state(self):
        virtual_memory_state =""
        for process in self.processes:
            virtual_memory_state += process.get_virtual_memory_text() + "\n"
        return virtual_memory_state
                
    def print_system_state(self):
        print("Frame Table:")
        self.frame_table.print_table()
        
        print("Processes and Page Tables:")
        for process in self.processes:
            print(process)
            process.pagetable.print_table()

if __name__ == "__main__":
    os = OperatingSystem(frame_count=1000, process_count=30, page_count_per_process=100, random_mode=False)
    os.run_simulation(1230, 50)
    print(os.get_virtual_memory_state())