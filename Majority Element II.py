
# better solution with timw o(n) and space o(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = dict()
        for i in nums:
            if i in counts:
                counts[i]+=1
            else:
                counts[i]=1
        n = len(nums)/3
        res = []
        for key,value in counts.items():
            if value>n:
                res.append(key)
        return res
        



# optimal solution with timeo(n) and space o(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1=0
        count2=0
        ele1=0
        ele2=0
        for i in nums:
            if count1==0 and ele2!=i:
                count1=1
                ele1=i
            elif count2==0 and ele1!=i:
                count2=1
                ele2=i
            elif ele1==i:
                count1+=1
            elif ele2==i:
                count2+=1
            else:
                count1-=1
                count2-=1
        res = []
        count1=0
        count2=0
        print(ele1, ele2)
        for i in nums:
            if ele1==i:
                count1+=1
            elif ele2==i:
                count2+=1
        n = len(nums)//3
        if count1>n:
            res.append(ele1)
        if count2>n:
            res.append(ele2) 
        return res
        
