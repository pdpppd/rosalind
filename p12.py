import itertools
import networkx as nx
import matplotlib.pyplot as plt
   
class GraphVisualization:
   
    def __init__(self):
        self.visual = []
          
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)
          

    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

def process_fasta(path):
    raw = open(path)
    raw = raw.read()
    new = raw.split('\n')
    indices = []
    final = {}
    for index, item in enumerate(new): 
        if item[0] == '>':
            indices.append(index)
    for i, index in enumerate(indices): 
        if index == indices[-1]:
            a = ''.join(new[index + 1:])
        else:   
            a = ''.join(new[index + 1: indices[i + 1]])
        name = new[index]
        name = name[1:]
        final[name] = a
    return final

def matchie(a, b):
    cnt = 0
    match = (False, cnt) 
    ind = 0
    while cnt <= 3: 
        if a[-cnt:] == b[:cnt]:
            match = (True, cnt)
        if cnt == len(a):
            break
        cnt += 1
    ind = match[1]
    if ind == 3: 
        match = True
    else: 
        match = False
    return match, ind

def main():
    G = GraphVisualization()
    genomes = process_fasta('data/p12test.txt')
    for genome1, genome2 in itertools.permutations(genomes, 2):
        result, ind = matchie(genomes[genome1], genomes[genome2])
        if genomes[genome1] == genomes[genome2]:
            result = False
        if result == True: 
            print("{} {}".format(genome1, genome2))
            G.addEdge(genome1, genome2)
            # print("{} {}".format(genomes[genome1], genomes[genome2]))
            # print(ind)
    G.visualize()

if __name__ == '__main__':
    main()
