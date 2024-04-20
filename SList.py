class SNode:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next
    def __str__(self):
        return str(self.item)

class SList:
    def __init__(self):
        self.head = None # 리스트의 첫 노드를 가리킴
    
    def insert_front(self, item):
        if self.head == None:  # 비어있음
            self.head = SNode(item, None)
            return True

        node = SNode(item, self.head)
        self.head = node
        return True


    def print_list(self):
        if self.head == None: #비어있음
            return print("empty")

        target = self.head
        while target:
            if target.next:
                print(target, end = "->")
            else:
                print(target)
            target = target.next
    
    def delete_front(self):
        if self.head == None:
            return None
            
        target = self.head
        self.head = target.next
        return target  


    def delete_target(self,item):
        if self.head == None: # Node 0 
            return None
        if self.head.item == item: # target이 맨앞, Node 1 
            return self.delete_front()
        
        target_prev = None
        target = self.head
        while target:
            if target.item == item:
                target_prev.next = target.next
                return target
            target_prev = target
            target = target.next
        return None
    
    def insert_back(self, item):
        if self.head == None: 
            self.head = SNode(item, None)
            return
        
        target = self.head
        while target.next:
            target= target.next
        #마지막 노드로 이동
        target.next = SNode(item, None)

    def delete_back(self):
        if self.head == None: # 비어있을 때 
            return None
        
        if self.head.next == None: # 노드 하나 있을 때 
            return self.delete_front()

        target_prev = None
        target = self.head
        while target.next:
            target_prev = target
            target = target.next
        #마지막 노드로 이동
        target_prev.next = None
        return target

    def get_list_as_text(self):
        count = 0 
        result = ""
        target = self.head
        while target:
            result += str(target.item)
            if target.next:
                result += " -> "
            target = target.next
            count += 1  
        return result, count  

if __name__ == "__main__":
    s = SList() # 빈 연결 리스트 생성
    s.insert_front("mango")
    s.insert_front("tomato")
    s.insert_front("orange")
    s.insert_back("apple")
    s.print_list() # 출력
    s.delete_front() # 삭제
    s.delete_back()
    s.print_list()
    s.delete_target("mango")
    s.print_list()
    s.insert_back("kiwi")
    s.print_list()
    s.delete_back()
    s.delete_back()
    s.print_list()