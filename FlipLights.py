import timedef flipLights(n, m):    """    :type n: int    :type m: int    :rtype: int    """    if n > 4: n = 4    if m > 4 and m % 2 == 0: m = 4    if m > 4 and m % 2 == 1: m = 3    statusSet = []    for s1 in range(0, m + 1):        for s2 in range(0, m + 1 - s1):            for s3 in range(0, m + 1 - s1 - s2):                lights = [1] * n                s4 = m - s1 - s2 - s3                lights = [(s1 & 1) ^ i for i in lights]                lights[1:n:2] = [(s2 & 1) ^ i for i in lights[1:n:2]]                lights[0:n:2] = [(s3 & 1) ^ i for i in lights[0:n:2]]                lights[0:n:3] = [(s4 & 1) ^ i for i in lights[0:n:3]]                if lights not in statusSet:                    statusSet.append(lights)                if len(statusSet) == 8:                    print(statusSet)                    return 8    return len(statusSet)start = time.time()print(flipLights(4, 3))print(flipLights(4, 1000))print(time.time() - start)