def make_priority(skill):
    temp = []
    for i in range(len(skill)):
        temp.append(skill[i])
    return temp

def check_priority(skill_tree, skill_priority):
    temp = []
    for i in range(len(skill_tree)):
        if skill_tree[i] in skill_priority: temp.append(skill_tree[i])
    return temp

def compare_skilltree(checklist, skill_priority):
    for i in range(len(checklist)):
        if skill_priority[i] != checklist[i]:
            return False
    return True

def solution(skill, skill_trees):
    answer = 0
    skill_priority = make_priority(skill)
    for skill_tree in skill_trees:
        checklist = check_priority(skill_tree, skill_priority)
        if (compare_skilltree(checklist, skill_priority)):
            answer += 1
    return answer

if __name__ == "__main__":
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    assert solution(skill, skill_trees) == 2
