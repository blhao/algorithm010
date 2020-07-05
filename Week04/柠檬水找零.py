# 柠檬水找零
# 如果顾客支付了 5 美元钞票，那么我们就得到 5 美元的钞票。
# 如果顾客支付了 10 美元钞票，我们必须找回一张 5 美元钞票。如果我们没有 5 美元的钞票，答案就是 False ，因为我们无法正确找零。
# 如果顾客支付了 20 美元钞票，我们必须找回 15 美元。
# 如果我们有一张 10 美元和一张 5 美元，那么我们总会更愿意这样找零，这比用三张 5 美元进行找零更有利。
# 否则，如果我们有三张 5 美元的钞票，那么我们将这样找零。
# 否则，我们将无法给出总面值为 15 美元的零钱，答案是 False 。
class Solution:
    def lemonadeChange(self, bills: list):
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


# bills=[5,5,5,10,20]
# bills=[5,5,10,10,20]
bills = [10, 10]
S = Solution()
S.lemonadeChange(bills)
