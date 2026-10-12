class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        temp = defaultdict(list)
        visits = sorted(zip(timestamp, username, website))
        
        for time, user, site in visits:
            temp[user].append(site)

        sol = defaultdict(int)

        for key in temp:
            sites = temp[key]
            seen = set()
            for i in range(len(sites)):
                for j in range(i + 1, len(sites)):
                    for k in range(j + 1, len(sites)):
                        pattern = (sites[i], sites[j], sites[k])

                        if pattern in seen:
                            continue
                        else:
                            seen.add(pattern)
                            sol[pattern] += 1
        
        best_pattern = None
        best_amt = 0

        for pattern, count in sol.items():
            if count > best_amt:
                best_pattern = pattern
                best_amt = count

            elif count == best_amt and best_pattern > pattern:
                best_pattern = pattern

        return list(best_pattern)

                

