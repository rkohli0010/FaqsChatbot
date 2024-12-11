import numpy as np
import chainlit as cl

import os
import queue
import time

import os
import queue
import time
from functools import partial
import numpy as np
import tritonclient.grpc as grpcclient
from tritonclient.utils import InferenceServerException, np_to_triton_dtype
from transformers import AutoTokenizer, AutoModelForCausalLM

from milvus_retrieval import retrieve_chunks
from milvus_retrieval import retrieve_chunks_nocode
from milvus_retieval_no_match import retrieve_chunks_nomatch
from vertexai_embeddings import embed_text
#from gemini2 import get_output_gemini
#from gemini_followup import get_output_gemini_followup
#from gemini_query_creator import get_output_gemini_nq_fp
from gemini_single_sol import get_output_gemini_1
#from gemini_2_sol import get_output_gemini_2
#from gemini_3_sol import get_output_gemini_3
from gemini_no_match import get_output_gemini_nomatch
from get_error_code import extract_error_code
from GEMINI_ASK_ERROR import gemini_show_errors
from GEMINI_GET_SINGLE_ERROR import gemini_show_sol

conversation_memory = []
current_state = 'None'

@cl.on_chat_start
async def start_chat() :
    msg = cl.Message(content = 'Lets go!')
    await msg.send()
    landing_page_text = """
**Welcome!** 🤖  
I'm here to assist you with your technical FAQ's. 🔧  
You can start by sharing your **Error Message**, **Log Message**, or an **Error Code**. 📈
"""
    msg.content = landing_page_text
    await msg.update()

@cl.on_message
async def process_message(message) :
    global conversation_memory, current_state
    user_query = message.content
    code_path = extract_error_code(user_query)
    #Code Path : NoErrorCode or Specific Error Code
    query_vector = embed_text([user_query])[0].values

    if current_state == 'None' :
        if code_path == 'NoErrorCode' and current_state == 'None' :
            retrieved_data = retrieve_chunks_nocode(query_vector)
            #Data will be retrieved only based on similariyu
        elif code_path != 'NoErrorCode' and current_state == 'None' :
            retrieved_data = retrieve_chunks(query_vector, code_path)
            #Search is hybrid : Error Code and Similarity

        if len(retrieved_data) == 1 and current_state == 'None' :
            response = get_output_gemini_1(retrieved_data, max_tokens = 1000).text
            print(f'Single Match Succesfull')
            #Current state is not getting changed

        elif len(retrieved_data) > 1 and current_state == 'None' :
            response = gemini_show_errors(retrieved_data, max_tokens = 1000)
            conversation_memory.append(
                {
                    'user_query' : user_query,
                    'chatbot_response' : response,
                    'retrieved_chunks' : retrieved_data
                }
            )
            current_state = 'Followup'
            print('More than 1 matches on similarity')

        elif len(retrieved_data) == 0 and current_state == 'None' :
            retrieved_data = retrieve_chunks_nomatch(code_path)
            print(f'###RETRIEVED DATA### : {retrieved_data}')
            if len(retrieved_data) == 0 :
                response = 'Based on the provided info I am unable to fetch an accurate response. Could you please share an error code?!'
            else :
                response = get_output_gemini_nomatch(retrieved_data, code_path)
                conversation_memory.append(
                    {
                        'user_query' : user_query,
                        'chatbot_response' : response,
                        'retrieved_chunks' : retrieved_data
                    }
                )

                current_state = 'Followup'
                print('Fetched on error code')

    elif current_state == 'Followup' :
        response = gemini_show_sol(conversation_memory[-1]['retrieved_chunks'], conversation_memory, user_query)
        conversation_memory.clear()
        current_state = 'None'
        print('Followup taken')


    print(f'History : {conversation_memory}')
    #print(f'Chunks : {retrieved_data}')
    print(f'State : {current_state}')
    print(f'Error Path : {code_path}')

    await cl.Message(content = response).send()


#Things to work on :
#1. Architecture Diagram : Rishav
#2. UI Changes : 
#a. Output Prompts and Formatting : Raunaq
#b. Chainlit Logo Change : Rishav

#3. Email Send Out
#4. What if user asks a followup? : Raunaq
#5. Guardrails so LLM doesn't go out of context : 
#6. Focus More on Problem Scoping 
#7. Beautify Output