#!/usr/bin/env python
# coding: utf-8

# In[68]:


import pandas as pd
import os


# In[91]:


def GetInstanceAndGroupID(dirname):
    
    

        #         with open(os.path.join(os.path.join(root,name), "mem.log"),'r') as f:
        #             lines = f.readlines()
        #             for line in lines:
        #                 print(line.split('":"'))

    #directory_list, root, name = GetDirectoryList()
    #print(directory_list)
    #IDAndInstance = []
    #for n in directory_list:
    d = dirname.split("_")
    #print(d)
    grpID = ''.join(d[0 : 2])
    instid = d[2]
    #print(ID)
    #dd =ID+[d[2]]
     #   IDAndInstance.append(dd)
    #print(IDAndInstance)
    return grpID, instid


# In[98]:


def LoadData():
    main_df = pd.DataFrame()
    directory_list, root, name = GetDirectoryList()
    #dd = GetInstanceAndGroupID()
    
    for i, n in enumerate(directory_list):
        print(n)
        groupid , instanceid = GetInstanceAndGroupID(n)
        while i < 100:
            Data = pd.read_csv(os.path.join("D:\\Assignment_Data\\"+n, "mem.log"), 'r', delimiter=':', header=None,
                               names=["Date", "value"])
            Data[["cpu_allocated", "cpu_used", "memory_allocate", "memory_used", "nw_bandwidth",
                  "disk_consumption"]] = Data.value.str.split(":", expand=True)
            for i in range(len(Data)):
                Data.loc[i,"group"] = groupid
                Data.loc[i,"instid"] = instanceid
            # print(Data.columns)
            # print(Data.head(2))
            main_df = main_df.append(Data, ignore_index=True)
            #print(1)
            print(main_df.tail(2))
            #break
    

    print("#############################################")


# In[99]:


LoadData()


# In[ ]:





# In[ ]:




