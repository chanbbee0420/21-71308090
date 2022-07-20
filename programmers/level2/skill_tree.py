def solution(skill, skill_trees):
    cnt = 0
    for skill_tree in skill_trees:
        tree = ''
        for el in skill_tree:
            if el in skill:
                tree += el
        if skill[:len(tree)] == tree:
            cnt += 1
                    
    return cnt



# def solution(skill, skill_trees):
#     answer = 0

#     for skills in skill_trees:
#         skill_list = list(skill)

#         for s in skills:
#             if s in skill:
#                 if s != skill_list.pop(0):
#                     break
#         else:
#             answer += 1

#     return answer