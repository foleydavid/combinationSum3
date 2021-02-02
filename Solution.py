# TESTING PUSH PULL WITH PYCHARM

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        #may only use 1 - 9, once per sum
        """
        
        # 0 < x < 10 for all numbers used
        return(Solution.getSums(k, n, 0))
              
    @staticmethod    
    def getSums(k_left, num, skip):
        all_ans = []
        
        #asking only two nums that add up to desired sum
        if k_left == 2:
            
            #begin considering vals after skip, and go until halfway point
            #max out at 9
            for i in range(skip + 1, min(int(num / 2) + 1,10)):
                
                #as long as duplicate vals are not present
                #max out at 9
                if i != num - i and (num - i) < 10:
                    ans = []
                    
                    #create short list of vals
                    ans.append(i)
                    ans.append(num - i)
                    
                    #append short list to complete list
                    all_ans.append(ans)
                    
        #asking for more than two nums to reach desired sum
        else:
            
            #begin considering vals after skip, and go until halfway point
            #max out at 9
            for i in range(skip + 1, min(int(num / 2) + 1,10)):
                
                #given current val, get any other vals to add up to missing total
                #start next function with adjusted nums, begin searching after current val
                past_sol = Solution.getSums(k_left - 1, num - i, i)
                
                #for each solution, add current val to start of solution
                #add full solution to complete list of solutions
                for element in past_sol:
                    element.insert(0,i)
                    all_ans.append(element)
                          
        return all_ans
