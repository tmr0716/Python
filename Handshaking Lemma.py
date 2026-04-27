vertice = ['A','B','C','D']
edges = [('A','B'),('A','C'),('B','C'),('C','D')]
v_map = {v:i for i,v in enumerate(vertice)}
matrix = [[0 for _ in range(4)] for _ in range(4)]
for start,end in edges:
    row,col = v_map[start],v_map[end]
    matrix[row][col] = 1
    matrix[col][row] = 1
print("    A  B  C  D")
print("    ----------")
for i,row in enumerate(matrix):
    print(f"{vertice[i]} | {'  '.join(map(str,row))}")
degree = {}
for i in range(4):
    degree[vertice[i]] = sum(matrix[i])
print("\nDegree of vertices: ")
for v in vertice:
    print(f"deg({v}) = {degree[v]}")
total_degree = sum(degree.values())
num_edges = len(edges)
print("\nSum of degrees = ",total_degree)
print("2 x Number of edges = ",2*num_edges)
if total_degree == 2*num_edges:
    print("Handshaking Lemma Verified!")
else:
    print("Handshaking Lemma NOT Verified!")
