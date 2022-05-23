import networkx as nx
import pylab as plt

# Create blank graph
D=nx.DiGraph()

# Feed page link to graph
read_file = open("../data/hollins_id_out_id.csv", "r")
for line in read_file:
    line = line.strip()
    line = line.split(",")
    D.add_edge(line[0], line[1])



# Print page rank for each pages
#print (nx.pagerank(D))

with open("../data/result_hollins_id_out_id.csv", "w") as f:
    for key, value in nx.pagerank(D).items():
        f.write(key + "," + str(value) + "\n")
