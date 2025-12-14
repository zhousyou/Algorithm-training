from collections import deque

def judge(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count == 1

if __name__ == "__main__":
    n = int(input())
    beginStr, endStr = input().split()
    strList = []
    for _ in range(n):
        strList.append(input().strip())
    
    visited = [False for _ in range(n)]
    que = deque([])
    que.append((beginStr, 1))
    while que:
        cur_str, step = que.popleft()
        if judge(cur_str, endStr):
            print(step + 1)
            exit(0)
        for i in range(n):
            if not visited[i] and judge(cur_str, strList[i]):
                visited[i] = True
                que.append((strList[i], step + 1))
    print(0)
