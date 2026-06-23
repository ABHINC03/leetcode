class Solution:
    def intToRoman(self, num: int) -> str:
        nums = str(num)

        hashmap={1:'I',4:'IV',5:'V',6:'VI',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:"CD",500:"D",900:'CM',1000:"M"}
        
        value=[]
        pownum=[int(number)*10**(len(nums)-i-1) for i,number in enumerate(nums)]
        for nums in pownum:
            if nums>0:
                if (nums%1000)==0:
                    if nums in hashmap:
                        value.append(hashmap[nums])
                    
                    else:
                        temp=nums
                        while(temp>0):
                            value.append(hashmap[1000])
                            temp=temp-1000
                        
                elif (nums%100)==0:

                    
                
                    temp=nums
                    temps=[]
                    while(temp>0):
                        if temp in hashmap:
                            temps.append(hashmap[temp])
                            temp=temp-temp
                        else:
                            temps.append(hashmap[100])
                            temp-=100
                    temps.reverse()
                    print(temps)        
                    for values in temps:
                        value.append(values)
                elif (nums%10)==0:
                    temp=nums
                    temps=[]
                    while(temp>0):
                        if temp in hashmap:
                            temps.append(hashmap[temp])
                            temp=temp-temp
                        else:
                            temps.append(hashmap[10])
                            temp-=10
                    temps.reverse()
                    for values in temps:
                        value.append(values)
                else:

                    temp=nums
                    temps=[]
                    while(temp>0):
                        if temp in hashmap:
                            temps.append(hashmap[temp])
                            temp=temp-temp
                        else:
                            temps.append(hashmap[1])
                            temp-=1
                    temps.reverse()
                    for values in temps:

                        value.append(values)
        return ''.join(value)
            