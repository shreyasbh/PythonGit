class BinHeap(object):
    self.heapList = [0]
    self.currentSize = 0
    
    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp 
            i = i // 2
            
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)
        
    def percDown(self,i):
        while i*2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp 
            i = mc
        
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] > self.heapList[i*2+1]:
                return i * 2 + 1
            else:
                return i * 2
                
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[currentSize]
        self.currentSize -= 1
        self.percDown(1)
        return retval
                