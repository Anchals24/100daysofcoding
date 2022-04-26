#User function Template for python3

class Solution:
    #Function to return the adjacency list for each vertex.
    def printGraph(self, V, adj):
        # code here
        #adj= [[3,2], [2], [1,0], [0]]
        ans = []
        j = 0
        for i in adj:
            i.sort()
            i.insert(0, j)
            ans.append(i)
            j += 1
        return ans
        

#{ 
#  Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.printGraph(V, adj)
		for i in range(len(ans)):
		    for j in range(len(ans[i])-1):
		        print(ans[i][j], end = "-> ")
		    print(ans[i][len(ans[i])-1]);

# } Driver Code Ends