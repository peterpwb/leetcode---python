#完全平方数肯定是前n个连续奇数的和，68ms
#Time:O(n) Space: O(1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=1
        while num>0:
            num-=i
            i+=2
        return 0==num

        
#基本不等式(a+b)/2 >=√ab 推导自 (a-b)^2 >= 0 → a^2 + b^2 >= 2ab → (a+b)/2 >=√ab（换元），
#注意 a>0 且 b>0  (r + num / r) / 2 >= √num 而 r > num / r 保证每次迭代 r 在不断减小,
#而//的存在保证最接近的时候能够逃离循环体

#基本不等式,68ms
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num
        while r * r > num:
            r = (r + num / r) // 2
        return r * r == num