
333.py Run Input
1
class Mentor:
2
    'common base class'
3
    typeof = 'l'
4
    def __init__(self,name):
5
        self.name = name
6
    
7
    def setMentorOrLearner(self):
8
        val = input("Are you are a mentor? If yes,click Y else N")
9
        if val == 'Y':
10
            Mentor.typeof = 'm'
11
            return Mentor.typeof
12
            
13
    def addStacks(self):
14
        stack=[]
15
        a = input("Add field of interest or expertise")
16
        stack.append('a')
17
        
18
    def setAvailableTime(self):
19
        if Mentor.typeof == 'm'
20
            time = input("set available time please")
21
    
22
    def getMentor(self):
23
        
24
        
25
    
26
emp1 = Mentor("Alphi")
27
if emp1.setMentorOrLearner() == 'm':
28
    emp1.setAvailableTime()
29
    emp1.addStacks()
Line: 10 Col: 31