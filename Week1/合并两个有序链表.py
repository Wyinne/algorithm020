class Node(object):
    def __init__(self,elem):
        self.elem=elem
        self.next=None
class Soultion:
    def AddTwoList(self,l1,l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.elem<l2.elem:
            l1.next=self.AddTwoList(l1.next,l2)
            return l1
        else:
            l2.next=self.AddTwoList(l1,l2.next)
            return l2
    def get(self,list):
        if list:
            node=Node(list.pop(0))
            node.next=self.get(list)
            return node
if __name__=="__main__":
    list1=[1,3,5,7,9,10,13,14,16,17]
    list2=[2,4,6,7,8,9,13,17,21,23]
    tlist1=Soultion().get(list1)
    tlist2=Soultion().get(list2)
    flist=Soultion().AddTwoList(tlist1,tlist2)
    while flist:
        print(flist.elem,end=" ")
        flist=flist.next

