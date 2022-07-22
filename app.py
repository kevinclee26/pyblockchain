import streamlit as st
import PyBlockchain as pbc
import hashlib
import pandas as pd
from datetime import datetime

@st.cache(allow_output_mutation=True)
def start(): 
	blockchain=pbc.PyBlockchain()
	return blockchain

blockchain=start()

buyer_id=st.text_input('Please input buyer_id: ')
seller_id=st.text_input('Please input seller_id: ')
shares=st.slider('Please input shares: ')

if st.button('Add block'): 
	# add block
	new_record=pbc.Record(buyer_id=buyer_id, seller_id=seller_id, shares=shares)
	last_block=blockchain.chain[-1]
	prev_hash=last_block.hash_block()
	new_block=pbc.Block(record=new_record, trade_time=datetime.utcnow().strftime('%H:%M:%S') ,prev_hash=prev_hash)
	blockchain.add_block(new_block)
	st.balloons()

df=pd.DataFrame(blockchain.chain).astype(str)
st.write(df)

# if st.sidebar.button('Check chain'): 
# 	for i in range(len(blockchain.chain)): 
# 	    check_block=blockchain.chain[i]
# 	    test_hasher=hashlib.sha256()
# 	    test_hasher.update(str(check_block.record).encode())
# 	    test_hasher.update(check_block.trade_time.encode())
# 	    test_hasher.update(check_block.prev_hash.encode())
# 	    st.sidebar.write(test_hasher.hexdigest())

check_block=st.sidebar.selectbox('Which block would you like to check? ', blockchain.chain)

if st.sidebar.button('Check block'): 
	test_hasher=hashlib.sha256()
	test_hasher.update(str(check_block.record).encode())
	test_hasher.update(check_block.trade_time.encode())
	test_hasher.update(check_block.prev_hash.encode())
	st.sidebar.write(test_hasher.hexdigest())
