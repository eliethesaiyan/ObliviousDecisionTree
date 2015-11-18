import numpy as np
class ObliviousTree: 

    'This is an implementation of Oblvious Tree'

    def __init__(self,data=[],func="C4.5",autoload=False):
        self.data=data 
        self.split_funct=func
        self.autoload=autoload
        self.feature_names=self.data.columns.tolist()
        self.feature_name_domains={}
        self.category_level={}
        self.level=0
        self.levels_nodes={}
    

    def load_tree(self):
        if not self.autoload:
            print("skipped autoloading")
        else:
            print(self.data)    
            print(self.feature_names)


    def build_branching_node_label_domains(self):
        print(self.split_function())

    def split_function(self):    
        if self.split_funct=="hardcoded":
            return self.hardcoded_features()

    def hardcoded_features(self):
        for feature_name in self.feature_names:
            self.feature_name_domains[feature_name]=np.unique(self.data[feature_name])
        return self.feature_name_domains  
    
    def create(self):
        is_root=True
        for feature_name in self.feature_name_domains: 
            level_list_nodes=[]
            if feature_name=="label":
                continue
            if is_root: 
                root_edge_list=[] 
                print(feature_name)
                root_domain=self.feature_name_domains[feature_name]
                root=Node(feature_name,self.data,100.0,root_domain)
                for domain in root_domain: 
                    branching_dataset=root.dataset[feature_name]=domain
                    print(branching_dataset)
                    braching_node=BranchingNode(feature_name,branching_dataset,branching_dataset.shape[0]/root.dataset.shape[0],domain,None)
                    root_edge_list.append(Edge(domain,root,braching_node))
                root.set_edge_list(root_edge_list)
                is_root=False

            self.level+=1


                
        print(root)
                    





class Node:
    def __init__(self,feature_name,dataset,probability,feature_domain,edge_list=None):
        self.dataset=dataset
        self.feature_domain=feature_domain
        self.feature_name=feature_name
        self.probability=probability
        self.edge_list=edge_list 
    def set_edge_list(self,edge_list=None):
        self.edge_list=edge_list
        
class BranchingNode(Node):
    def __init__(self,feature_name,dataset,probability,feature_domain,edge_list=None):
        Node.__init__(self,feature_name,dataset,probability,feature_domain,edge_list)
    

      
class CategoryNode(Node):
    def __init__(self,feature_name,dataset,probability,feature_domain,edge_list=None):
        Node.__init__(self,feature_name,dataset,feature_domain,probability,edge_list)
        self.edge_list=None
       
class Edge:
    def __init__(self,label,incoming_node=None,outgoing_node=None):
        self.label=label
        self.incoming_node=incoming_node
        self.outgoing_node=outgoing_node 

    def display(self):
        print(self.label)

    def get_incoming_node(self):
        if not self.incoming_node:
            print("No incoming node")
            return
        return self.incoming_node

    def get_outgoing_node(self):
        if not self.outgoing_node:
            print("No outgong Node")
            return
        return self.outgoing_node


      
      
      
