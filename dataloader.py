
import pandas as pd
from collections import OrderedDict
import csv
import numpy as np
import statsmodels.api as sm
import logging as log
from patsy import dmatrices
from pytimeparse.timeparse import timeparse
import dateutil.parser
from sklearn.linear_model  import LogisticRegression 
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score 
from sklearn import metrics 
from datetime import datetime 
from ObliviousTree import ObliviousTree





#count default number of returned session items
count=5
f = "%d/%m/%Y %H:%M:%S"


script_start=datetime.now()
#reads buys
def load_sessions(count):
    log.info("loading vectors")
    vectors=pd.read_csv("sample-data.dat",names=["label","session","week","hour","category","item","dwell"],dtype={'item':pd.np.int64,'session':pd.np.int64}) 
    if count==0:
        return vectors 
    return vectors[:count]


obt=ObliviousTree(load_sessions(10),"hardcoded",True)
obt.load_tree()
obt.build_branching_node_label_domains()
obt.create()



