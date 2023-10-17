Given a directed graph, determine whether a vertex j is reachable from another vertex i for all vertex pairs (i, j) in the given graph. Here, vertex j is reachable from another vertex i means that there is a path from vertex i to j. The reachability matrix is called the transitive closure of a graph. The directed graph is represented by an adjacency matrix where there are N vertices. 

Example 1:

Input: N = 4
graph = {{1, 1, 0, 1}, 
         {0, 1, 1, 0}, 
         {0, 0, 1, 1}, 
         {0, 0, 0, 1}}
Output: {{1, 1, 1, 1}, 
         {0, 1, 1, 1}, 
         {0, 0, 1, 1}, 
         {0, 0, 0, 1}}
Explanation: 
The output list shows the reachable indexes.
Example 2:

Input: N = 3
graph = {{1, 0, 0}, 
         {0, 1, 0}, 
         {0, 0, 1}}
Output: {{1, 0, 0}, 
         {0, 1, 0}, 
         {0, 0, 1}}
Explanation: 
The output list shows the reachable indexes.
Your Task:
You do not need to read input or print anything. Your task is to complete the function transitiveClosure() which takes an integer N and a 2D array graph(adjacency matrix of the graph) as input parameters and returns the transitive closure of the graph in the form of 2D array.

Expected Time Complexity: O(N3)
Expected Auxiliary Space: O(N2)

Constraints:
1 ≤ N ≤ 100  



Solution:
class Solution:
    def transitiveClosure(self, N, graph):
        # code here
        
        adj=[[] for i in range(N)]
        
        for i in range(N):
            for j in range(N):
                if graph[i][j]==1:
                    if i!=j:
                        adj[i].append(j)
        
        ans=[[0 for i in range(N)] for j in range(N)]
        
        def dfs(r,i,visit):
            ans[r][i]=1
            visit.add(i)
            for ele in adj[i]:
                if ele not in visit:
                    dfs(r,ele,visit)
        
        for i in range(N):
            dfs(i,i,set())
        return ans
