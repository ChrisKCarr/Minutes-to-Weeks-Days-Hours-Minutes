
# coding: utf-8

# In[63]:


def time(m):
    time = m
    week = time // (7 * 1440)
    time = time % (7 * 1440)
    day = time //  1440
    time = time % 1440
    hour = time // 60
    time %= 60
    minutes = time 
    time %= 60
    print("w:d:h:m-> %d weeks :%d days :%d hours :%d minutes" % (week, day, hour, minutes))


# In[64]:


time(30240)

