# Importing the Required Libraries
import networkx as nx
import random
import itertools

#Consider an edge attribute sign with value as '+' or '-' and add sign to all the edges using the given file (0 means '-' and 1 means '+'). 
def create_graph_from_edges(filename):
    #Your code goes here
    G = nx.Graph()
    file = open(filename,'r')
    lines = file.readlines()
    for i in range(len(lines)-1):
    	node1 = lines[i+1].strip().split(',')[0]
    	node2 = lines[i+1].strip().split(',')[1]
    	weight = lines[i+1].strip().split(',')[2]
    	sign = lines[i+1].strip().split(',')[3]
    	if sign == '+':
    		G.add_edge(node1,node2,sign='+')
    	else:
    		G.add_edge(node1,node2,sign='-')
    	nx.set_edge_attributes(G,{(node1,node2):{'weight':weight,'sign':sign}})
    
    return G


#Find the list of triangles in the graph G            
def find_triangles(G):
    #Your code goes here
    triangles_lt = [list(triangle) for triangle in itertools.combinations(G.nodes(),3)]
        
    return triangles_lt


#Find the sign details of all the triangles
def find_triangles_signlist(G,triangles_lt):
    #Your code goes here
    signlt_triangles = []
    for i in range(len(triangles_lt)):
        triangle_signs = []
        triangle_signs.append(G[triangles_lt[i][0]][triangles_lt[i][1]]['sign'])
        triangle_signs.append(G[triangles_lt[i][1]][triangles_lt[i][2]]['sign'])
        triangle_signs.append(G[triangles_lt[i][2]][triangles_lt[i][0]]['sign'])
        signlt_triangles.append(triangle_signs)    
    
    return signlt_triangles


#Find the weight details of all the triangles
def get_all_signs(G,triangles_lt):
    #Your code goes here
    all_signs = []
    for i in range(len(triangles_lt)):
        triangle_signs = []
        triangle_signs.append(float(G[triangles_lt[i][0]][triangles_lt[i][1]]['weight']))
        triangle_signs.append(float(G[triangles_lt[i][1]][triangles_lt[i][2]]['weight']))
        triangle_signs.append(float(G[triangles_lt[i][2]][triangles_lt[i][0]]['weight']))
        all_signs.append(triangle_signs)    
    
    return all_signs


#Find the number of unstable triangles from the sign details of all the triangles 
def count_unstable_triangles(signlt_triangles):
    #Your code goes here
    num_unstable_triangles = 0
    for i in range(len(signlt_triangles)):
        if signlt_triangles[i].count('+')==0 or signlt_triangles[i].count('+')==2:
            num_unstable_triangles += 1

    return num_unstable_triangles

# Moving an unstable triangle to a stable state based on sign and weight values
def move_a_tri_to_stable(G, tris_list, all_signs):
    found_unstable=False
    case=0
    while(found_unstable==False):
        index=random.randint(0,len(tris_list)-1)
        i,j,k=all_signs[index]
        if i<0 and j<0 and k<0: #(all_signs[i].count('+')==2 or all_signs[i].count('+')==0):
            found_unstable=True
            case=1
        elif (i>=0 and j>=0 and k<0) or (i>=0 and j<0 and k>=0) or (i<0 and j>=0 and k>=0):
            found_unstable=True
            case=2
        else:
            continue
    i=float(G[tris_list[index][0]][tris_list[index][1]]['weight'])
    j=float(G[tris_list[index][1]][tris_list[index][2]]['weight'])
    k=float(G[tris_list[index][2]][tris_list[index][0]]['weight'])
    to_change=0
    if(abs(j)>abs(i)):
        to_change=1
        if(abs(k)>abs(j)):
            to_change=2
    elif(abs(k)>abs(i)):
        to_change=2
         
    if case==2:   
        if G[tris_list[index][to_change]][tris_list[index][(to_change+1)%3]]['sign']=='+':
            G[tris_list[index][to_change]][tris_list[index][(to_change+1)%3]]['sign']='-'
            i=float(G[tris_list[index][(to_change+1)%3]][tris_list[index][(to_change+2)%3]]['weight'])
            j=float(G[tris_list[index][(((to_change+1)%3)+1)%3]][tris_list[index][(((to_change+2)%3)+1)%3]]['weight'])
            if(i>j):
                weight=i+abs(j)-float(G[tris_list[index][to_change]][tris_list[index][(to_change+1)%3]]['weight'])
                weight=-weight
                G[tris_list[index][to_change]][tris_list[index][(to_change+1)%3]]['weight']=weight
        elif G[tris_list[index][to_change]][tris_list[index][(to_change+1)%3]]['sign']=='-':
            G[tris_list[index][to_change]][tris_list[index][(to_change+1)%3]]['sign']='+'
            weight=abs(float(G[tris_list[index][(to_change+1)%3]][tris_list[index][(to_change+2)%3]]['weight'])) + abs(float(G[tris_list[index][(((to_change+1)%3)+1)%3]][tris_list[index][(((to_change+2)%3)+1)%3]]['weight']))
            G[tris_list[index][to_change]][tris_list[index][(to_change+1)%3]]['weight']=weight
    
    elif case==1:
        G[tris_list[index][to_change]][tris_list[index][(to_change+1)%3]]['sign']='+'
        weight=abs(float(G[tris_list[index][(to_change+1)%3]][tris_list[index][(to_change+2)%3]]['weight'])) + abs(float(G[tris_list[index][(((to_change+1)%3)+1)%3]][tris_list[index][(((to_change+2)%3)+1)%3]]['weight']))
        G[tris_list[index][to_change]][tris_list[index][(to_change+1)%3]]['weight']=weight
        
    return G

#Stabilizing the graph by balancing triangles - balance theorem
def stabilize_graph(G):
	triangles_lt = find_triangles(G)
	signlt_triangles = find_triangles_signlist(G,triangles_lt)
	all_signs = get_all_signs(G,triangles_lt)
	#Finding triangle info related to the graph to use later
	num_unstable_triangles = count_unstable_triangles(triangles_lt)
	num_unstable_prev=num_unstable_triangles
	round_no = 0
	stopping_flag = 0
	# Balancing the graph till required for analysis
	while(round_no<100 and num_unstable_triangles>500 and stopping_flag<10):
	    num_unstable_prev=num_unstable_triangles
	    G=move_a_tri_to_stable(G, triangles_lt, all_signs)
	    signlt_triangles = find_triangles_signlist(G,triangles_lt)
	    num_unstable_triangles = count_unstable_triangles(signlt_triangles)
	    round_no+=1
	    if(num_unstable_prev==num_unstable_triangles):
	        stopping_flag+=1
	    else:
	        stopping_flag=0
	    #nx.write_gml(G, "graph_after_stablizing.gml")

def coalitions(G, rd):
    first_coal = []
    second_coal = []
    
    if rd == 1:
        r = '1'
    else:
        r = '17'
    
    first_coal.append(r)
    
    print(str(r) + 'is the randomly chosen node.')
    nodes_done = []
    nodes_left = [r]
    
    for each_node in nodes_left:
        if each_node not in nodes_done:
            neighbor = list(G.neighbors(each_node))
            
            for i in range(0, len(neighbor)):
                if G[each_node][neighbor[i]]['sign'] == '+':
                    if (neighbor[i] not in first_coal) and (neighbor[i] not in second_coal):
                        first_coal.append(neighbor[i])
                    if neighbor[i] not in nodes_left:
                        nodes_left.append(neighbor[i])
                
                elif G[each_node][neighbor[i]]['sign'] == '-':
                    if (neighbor[i] not in second_coal) and (neighbor[i] not in first_coal):
                        second_coal.append(neighbor[i])
                        nodes_done.append(neighbor[i])
                        
            nodes_done.append(each_node)
    
    return first_coal, second_coal

G = nx.read_gml('small-graph.gml')
before_coal1, before_coal2 = coalitions(G, 1)

G['1']['16']['sign']='+'
G['1']['16']['weight']='15'

stabilize_graph(G)
after_coal1, after_coal2 = coalitions(G, 2)