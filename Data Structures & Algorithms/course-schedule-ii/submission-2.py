class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        out_going_edges = dict()
        incomming_edges_count = dict()

        for i in range(numCourses):
            out_going_edges[i] = []

        for i in range(numCourses):
            incomming_edges_count[i] = 0

        for a, b in prerequisites:
            out_going_edges[b].append(a)
            incomming_edges_count[a] += 1

        res = []
        count = numCourses

        inc = True
        while inc:
            inc = False
            for i in range(numCourses):
                if incomming_edges_count[i] == 0:
                    res.append(i)
                    incomming_edges_count[i] -= 1
                    inc = True
                    for rec in out_going_edges[i]:
                        incomming_edges_count[rec] -= 1
        if len(res) != numCourses:
            return []
        return res
        