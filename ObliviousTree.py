import numpy as np
class ObliviousTree: 

    'This is an implementation of Oblvious Tree'

    def __init__(self,data=[],func="C.45",autoload=False):
        self.data=data 
        self.split_funct=func
        self.autoload=autoload
        self.feature_names=self.data.columns.tolist()
        self.feature_name_domains={}
        self.category_level={}
    

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
        for feature_name,feature_domain in self.feature_name_domains: 
            if feature_name=="label":
                continue
            if is_root: 
                for domain in feature_domain:
                    root_node=





class Node:
    def __init__(self,feature_name,dataset,probability,feature_domain,edge_list=None):
        self.dataset=dataset
        self.feature_domain=feature_domain
        self.feature_name=feature_name
        self.probability=probability
        self.edge_list=edge_list 
   def set_edge_list(edge_list=None):
       self.edge_list=edge_list
        
class BranchingNode(Node):
    def __init__(self,feature_name,dataset,probability,feature_domain,edge_list=None):
        Node.__init__(self,feature_name,dataset,probability,feature_domain,edge_list)
    

      
class CategoryNode(Node):
    def __init__(self,feature_name,dataset,probability,feature_domain,edge_list=None):
        Node.__init__(self,feature_name,dataset,feature_domain,probability,edge_list)
        self.edge_list=None
       
class Edge:
    def __init_(self,label,incoming_node=None,outgoing_node=None):
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


      
      
      
