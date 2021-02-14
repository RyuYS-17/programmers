def split_s(s, number):
    temp = [s[i:i+number] for i in range(0, len(s), number)]
    return temp

def count_split(str_split):
    temp = []
    temp.append([str_split[0],1])
    for string in str_split[1:]:
        if string == temp[-1][0]:
            temp[-1][1] += 1
        elif string != temp[-1][0]:
            temp.append([string,1])
    return temp

def make_compressed_str(cnt_split):
    string = ''
    for word in cnt_split:
        if word[1] == 1:
            string = string + word[0]
            continue
        string = string + str(word[1]) + word[0]
    return string

def find_shortest(answer_list, s):
    shortest = len(s)
    for word in answer_list:
        if len(word) < shortest:
            shortest = len(word)
    return shortest

def solution(s):
    answer = 0
    cut_number = [i for i in range(1, (len(s)//2+1))]
    answer_list = []
    for number in cut_number:
        str_split = split_s(s, number)
        cnt_split = count_split(str_split)
        str_compress = make_compressed_str(cnt_split)
        answer_list.append(str_compress)
    answer = find_shortest(answer_list, s)
    return answer

if __name__ == "__main__":
    s = "aabbaccc"
    assert solution(s) == 7
