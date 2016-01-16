'''
Created on Jan 15, 2016

@author: guy
'''


class graph(object):
    def __init__(self,edges_list,number_of_nodes):
        ''' edges list should be in format of a list of tuples 
        presenting edges. graph assumes nodes go from 0 - number of nodes
        hence only number of nodes should be assigned. '''
        self.adj_list = [[] for i in range(number_of_nodes)];
        self.number_of_edges = len(edges_list);
        self.number_of_nodes = number_of_nodes;
        for tup in edges_list:
            self.adj_list[tup[0]].append(tup[1])
        self.curr_pr = [1/number_of_nodes for i in range(number_of_nodes)];

    def page_rank(self,iterations,d):
        ''' implement the PageRank algorithm, returns the PR of each node 
        in the self.curr_pr variable '''
        N = self.number_of_nodes;
        for t in range(iterations):
            self.next_pr = [0 for i in range(N)];
            for node in range(self.number_of_nodes):
                for edge in self.adj_list[node]:
                    # PR(node_i,t+1) = (1-N)/d + d*sum{PR(node_j)/L(node_j)}
                    self.next_pr[edge] = self.next_pr[edge] + d*self.curr_pr[node]/len(self.adj_list[node])
                #adding the constant dumping factor
            self.next_pr = [self.next_pr[i]+(1-d)/N for i in range(N)];
            self.curr_pr = [x for x in self.next_pr];
        return self.curr_pr
    
    
if __name__ == '__main__':
 
    print("Testing two nodes, both connected to each other")
    itr = 20;
    d = 0.85;
    test_tree = [(0,1),(1,0)];
    N = 2;
    g = graph(test_tree,N);
    print(g.page_rank(itr,d));
    print("Testing two nodes, one connected to other")
    test_tree = [(0,1)]
    N = 2;
    g = graph(test_tree,N);
    print(g.page_rank(itr,d));
    print("Testing 3 nodes, all equale")
    test_tree = [(0,1),(1,2),(2,0)]
    N = 3;
    g = graph(test_tree,N);
    print(g.page_rank(itr,d));
    print("Testing 3 nodes, 0 most important than others")
    test_tree = [(2,0),(1,0),(0,1),(1,2)]
    N = 3;
    g = graph(test_tree,N);
    print(g.page_rank(itr,d));
    
    
    