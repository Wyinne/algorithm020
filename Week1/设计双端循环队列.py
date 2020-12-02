class MyCircularDeque:
    def __init__(self,k:int):
        self.maxlen=k
        self.l=0
        self.deque=[0]*k
        self.pHead=0
        self.pRear=0
    def insertFront(self,value:int)->bool:
        if self.l==self.maxlen:
            return False
        if self.l:
            self.pHead=self.pHead-1 if self.pHead>0 else self.maxlen-1#????????????
        self.deque[self.pHead]=value
        self.l+=1
        return self.deque
    def insertLast(self,value:int)->bool:
        if self.l==self.maxlen:
            return False
        if self.l:
            self.pRear=self.pRear+1 if self.pRear<self.maxlen-1 else 0#????????????
        self.deque[self.pRear]=value
        self.l+=1
        return self.deque
    def deleteFront(self)->bool:
        if not self.l:
            return False
        if self.l!=1:
            self.pHead=self.pHead+1 if self.pHead<self.maxlen-1 else 0
        self.l=-1
        return self.deque
    def getFront(self)->int:
        if not self.l:
            return -1
        return self.deque[self.pHead]
    def getRear(self)->int:
        if not self.l:
            return -1
        return self.deque[self.pRear]
    def isEmpty(self)->bool:
        return not self.l
    def isFull(self)->bool:
        return self.l==self.maxlen


