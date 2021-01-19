def determine_print(docs):
    if docs[0] == max(docs):
        return True
    return False

def print_document(docs):
    docs.pop(0)

def bring_document_back(docs):
    docs.append(docs.pop(0))

def solution(priorities, location):
    answer=0
    while(True):
        if determine_print(priorities):
            print_document(priorities)
            answer += 1
            if (location == 0):
                return answer
            else: location -= 1
        else:
            bring_document_back(priorities)
            if (location == 0):
                location = len(priorities)-1
            else: location -= 1