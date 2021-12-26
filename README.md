# oop_Ex3#
class:
---------
**Node:**<br />
A class that represents node data, object: id, pos, weight, tag and dict to edge in and dict to edge out. <br />
**Edge:** <br />
A class that represents edges data object: weight id1=src, id2=dest. <br />
**DiGraph:** <br />
A class that implements the interface GraphInterface, object: sizeNode, sizeEdge, listNode, listEdge, mc. <br />
-function: *v_size:returns the number of nodes in this graph <br />
           *e_size:returns the number of edges in this graph <br />
           *get_all_v:return a dictionary of all the nodes in the Graph. <br />
           *all_in_edges_of_node: return a dictionary of all the nodes connected to (into) node_id. <br />
           *all_out_edges_of_node:return a dictionary of all the nodes connected from node_id. <br />
           *get_mc:returns the current version of this graph. <br />
           *add_edge:adds an edge to the graph. <br />
           *add_node:adds a node to the graph.
           *def remove_node:removes a node from the graph.
           *remove_edge:removes an edge from the graph.
**GraphAlgo:**
A class that implements the interface GraphAlgoInterface, object: DiGraph Graph.
-function:* get_graph:return the graph that the algorithm works on.
          * load_from_json: loads a graph from a json file.
          * save_to_json: saves the graph in JSON format to a file
          * shortest_path:returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
            We used this function in Dijkstra We sent the src node to Dijkstra and according to the parents dict we received we went
            from the destination node to reach the source and returned the weight of the node and the and list of the route.
            If there is no route, we returned an empty list and infinite.
          * TSP:finds the shortest path that visits all the nodes in the list
            In this function we checked the short path between all 2 vertices if the short path contains all the vertices in the list and is the minimum we returned this path,               and the minimum distance. If it did not exist, we checked for every 2 consecutive vertices in the list the short route between them and returned the short route and             the minimum distance
          * centerPoint:finds the node that has the shortest distance to it's farthest node.
            This function we used a Dijkstra We sent each a node to Dijkstra and checked what the maximum distance is for each nodes and we checked if this distance is the                   minimum and we returned from all the maximum distances the minimum distance and the nodes that holds it.
            If there is a node from which the Dijkstra returned an empty dict, that is, there is no way to reach it from other nodes, that is, the graph is not linked. We                   returned -1 and infinity 
          * plot_graph:plots the graph.
-We also implemented auxiliary functions:*changeMaxVal:Updates to all weight of nodes to infinite
                                         *Dijkstra:We implemented the Dijkstra algorithm the algorithm gets a nodes src and updates שccording to the algorithm the weight of                                                        each nodes the minimum distance from src to the node,the algorithm returns a dictionary representing for each nodes                                                              the node that preceding in the path from the src to the node.

  



