from heapq import heappush, heappop
from collections import Counter

def leastInterval(tasks, n):
    c = Counter(tasks).most_common()
    spaces = n * (c[0][1]-1)
    for i, el in enumerate(c):
        if i == 0:
            continue
        spaces -= min(el[1], c[0][1]-1)
    return len(tasks)+spaces

def leastInterval2(tasks, N):
    task_counts = list(Counter(tasks).values())
    M = max(task_counts)
    print(task_counts, M)
    Mct = task_counts.count(M)
    print(M, Mct)
    return max(len(tasks), (M - 1) * (N + 1) + Mct)


def leastInterval3(tasks, n):
    curr_time, h = 0, []
    for k,v in Counter(tasks).items():
        heappush(h, (-1*v, k))
        print("heap push: ", h)
    while h:
        i, temp = 0, []
        while i <= n:
            curr_time += 1
            if h:
                x,y = heappop(h)
                if x != -1:
                    temp.append((x+1,y))
            if not h and not temp:
                break
            else:
                i += 1
            print(i , " : ", temp)
        for item in temp:
            heappush(h, item)
    return curr_time

if __name__ == '__main__':
    print(leastInterval3(["A","A","A","B","B","B"], 2))