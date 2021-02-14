def line_diagongal(min_w, min_h):
    temp = [min_w, min_h]
    if any(num%2 == 0 for num in temp):
        return ((min_h//2)+(min_w//2))*2
    return ((min_h//2)+(min_w//2))*2+1

def solution(w,h):
    from math import gcd
    gcd_num = gcd(w,h)
    min_w = w//gcd_num; min_h = h//gcd_num

    diagonal_square = line_diagongal(min_w, min_h)
    return w*h - (diagonal_square*gcd_num)

if __name__ == "__main__":
    w=8; h=12
    assert solution(w,h) == 80
