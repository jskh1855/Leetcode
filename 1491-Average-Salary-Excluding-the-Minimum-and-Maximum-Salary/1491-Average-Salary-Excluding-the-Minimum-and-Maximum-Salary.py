class Solution:
    def average(self, salary: List[int]) -> float:

        max_salary, min_salary = 0, 10**6
        total = 0
        size = 0

        for money in salary:
            
            total += money
            max_salary = max(max_salary, money)
            min_salary = min(min_salary, money)
            size += 1

        return (total - max_salary - min_salary)/(size-2)
