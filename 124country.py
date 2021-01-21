def divide_by_3_first(n, dict_remaider, answer):
    remainder = n%3
    answer = dict_remaider[remainder] + answer
    if remainder == 0:
        n = (n-3)//3
    else:
        n = (n - remainder)//3
    return n, answer

def solution(n):
    answer = ''
    dict_remaider = {1:'1', 2:'2', 0:'4'}
    dict_share = {1:'1', 2:'2', 3:'4'}

    while(True):
        n, answer = divide_by_3_first(n, dict_remaider, answer)
        if n>3: continue
        if n==0: break
        answer = dict_share[n] + answer
        break
    return answer

if __name__ == "__main__":
    n = 9
    answer = '24'
    assert solution(n) == answer