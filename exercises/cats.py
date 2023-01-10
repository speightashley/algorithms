def solution(start, finish):
    total_steps = finish - start
    return (total_steps // 3) + total_steps % 3


print(solution(1, 5))
