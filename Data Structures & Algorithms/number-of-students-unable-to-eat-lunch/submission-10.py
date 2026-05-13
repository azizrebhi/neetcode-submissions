class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        hashmap={}
        hashmap[0]=students.count(0)
        hashmap[1]=students.count(1)
        for i in sandwiches :
            if hashmap[i]>0 : 
               hashmap[i]-=1
            else :
                return hashmap[0]+hashmap[1]
        return 0


        