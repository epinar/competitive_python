
import collections

def groupAnagrams1(strs):

    d = {}
    for s in strs:
        srtd = ''.join(sorted(s))
        if srtd in d:
            d[srtd].append(s)
        else:
            d[srtd] = [s]

    return d.values()

def groupAnagrams1_b(strs):
    d = collections.defaultdict(list)
    for s in strs:
        d[tuple(sorted(s))].append(s)
    return d.values()

def groupAnagrams2(strs):
    ## Keep strings according to char count.
    d = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        d[tuple(count)].append(s)
    return d.values()


if __name__ == '__main__':
    print(groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))