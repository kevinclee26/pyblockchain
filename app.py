import streamlit as st

@st.cache(allow_output_mutation=True)
def start(): 
	blockchain=[]
	return blockchain

blockchain=start()

record=st.text_input('Please input record')

if st.button('Add block'): 
	# add block
	blockchain.append(record)

st.write(blockchain)