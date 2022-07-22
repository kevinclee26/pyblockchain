#!/usr/bin/env python
# coding: utf-8

# In[28]:


from datetime import datetime
from dataclasses import dataclass
import hashlib


# In[21]:


@dataclass
class Record(): 
    buyer_id: str
    seller_id: str
    shares: float


# In[75]:


@dataclass
class Block(): 
    record: Record
    trade_time: str=datetime.utcnow().strftime('%H:%M:%S')
    prev_hash: str='genisus'
    
    # def __init__(self): 
    #     self.record=''
    #     self.trade_time=datetime.utcnow().strftime('%H:%M:%S')
    
    def hash_block(self): 
        hasher=hashlib.sha256()
        hasher.update(str(self.record).encode())
        hasher.update(self.trade_time.encode())
        hasher.update(self.prev_hash.encode())
        return hasher.hexdigest()


# In[76]:


class PyBlockchain():
    def __init__(self): 
        self.chain=[Block(Record('', '', 0))]
        
    def add_block(self, block): 
        self.chain.append(block)


# In[94]:


# chain=PyChain()


# # In[95]:


# chain.chain


# # In[96]:


# new_record=Record(buyer_id='kevin', seller_id='harry', shares=1)
# display(new_record.buyer_id)
# display(new_record.seller_id)
# display(new_record.shares)


# # In[97]:


# # get last block of existing chain
# last_block=chain.chain[-1]

# prev_hash=last_block.hash_block()

# new_block=Block(record=new_record, prev_hash=prev_hash)
# display(new_block.record)
# display(new_block.trade_time)
# display(new_block.prev_hash)


# # In[98]:


# chain.add_block(new_block)


# # In[99]:


# chain.chain


# # In[100]:


# newer_record=Record(buyer_id='harry', seller_id='kevin', shares=1)
# display(newer_record.buyer_id)
# display(newer_record.seller_id)
# display(newer_record.shares)


# # In[101]:


# # get last block of existing chain
# last_block=chain.chain[-1]

# prev_hash=last_block.hash_block()

# newer_block=Block(record=new_record, prev_hash=prev_hash)
# display(newer_block.record)
# display(newer_block.trade_time)
# display(newer_block.prev_hash)


# # In[102]:


# chain.add_block(newer_block)


# # In[103]:


# chain.chain


# # In[105]:


# for i in range(len(chain.chain)): 
#     check_block=chain.chain[i]
#     test_hasher=hashlib.sha256()
#     test_hasher.update(str(check_block.record).encode())
#     test_hasher.update(check_block.trade_time.encode())
#     test_hasher.update(check_block.prev_hash.encode())
#     print(test_hasher.hexdigest())


# # In[ ]:




