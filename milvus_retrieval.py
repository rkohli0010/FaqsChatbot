from pymilvus import MilvusClient, DataType, connections, Collection, FieldSchema, CollectionSchema, AnnSearchRequest, WeightedRanker
from vertexai_embeddings import embed_text

client = MilvusClient(
    uri='http://3.229.150.112:19530',
    user="root",
    password="Milvus"
)

client.load_collection(
    collection_name="Faqs_Chatbot",
    replica_number=1 
)

def retrieve_chunks(query_vector, error_code) :
    client = MilvusClient(
    uri='http://3.229.150.112:19530',
    user="root",
    password="Milvus"
        )

    client.load_collection(
        collection_name="Faqs_Chatbot",
        replica_number=1 
    )

    search_results = client.search(
        collection_name = 'Faqs_Chatbot',
        filter=f"group_error_code == '{error_code}' ",
        data = [query_vector],
        limit = 3,
        output_fields=['text', 'error_category', 'group_error_code', 'individual_error_code'],
        search_params = {
            'metric_type' : 'COSINE',
            'params' : {}
        }
    )
    
    
    filtered_res = []
    if search_results[0][0]['distance'] >= 0.95:
        # to skip other matches if we found exact match
        filtered_res.append(search_results[0][0]['entity']['text'])
        return filtered_res
    
    elif search_results[0][0]['distance'] >= 0.80:
        filtered_res.append(search_results[0][0]['entity']['text'])

    if search_results[0][1]['distance'] >= 0.80:
        filtered_res.append(search_results[0][1]['entity']['text'])

    if search_results[0][2]['distance'] >= 0.80:
        filtered_res.append(search_results[0][2]['entity']['text'])


    print(f"The similarity score of the first chunk is : {search_results[0][0]['distance']}")

    return filtered_res

def retrieve_chunks_nocode(query_vector) :
    client = MilvusClient(
    uri='http://3.229.150.112:19530',
    user="root",
    password="Milvus"
        )

    client.load_collection(
        collection_name="Faqs_Chatbot",
        replica_number=1 
    )

    search_results = client.search(
        collection_name = 'Faqs_Chatbot',
        data = [query_vector],
        limit = 3,
        output_fields=['text', 'error_category', 'group_error_code', 'individual_error_code'],
        search_params = {
            'metric_type' : 'COSINE',
            'params' : {}
        }
    )
    
    
    filtered_res = []
    if search_results[0][0]['distance'] >= 0.95:
        # to skip other matches if we found exact match
        filtered_res.append(search_results[0][0]['entity']['text'])
        return filtered_res
    
    elif search_results[0][0]['distance'] >= 0.80:
        filtered_res.append(search_results[0][0]['entity']['text'])

    if search_results[0][1]['distance'] >= 0.80:
        filtered_res.append(search_results[0][1]['entity']['text'])

    if search_results[0][2]['distance'] >= 0.80:
        filtered_res.append(search_results[0][2]['entity']['text'])


    print(f"The similarity score of the first chunk is : {search_results[0][0]['distance']}")

    return filtered_res


#Example to search on basis of metadata first then similarity search
#res = client.search(
 #   collection_name="demo_collection",
  #  data=embedding_fn.encode_queries(["tell me AI related information"]),
   # filter="subject == 'biology'",
    #limit=2,
    #output_fields=["text", "subject"],
#)




# q = """
#     CRITICAL [nio-5432-exec-9] com.system.auth.processor.UserValidation - POST | /api/v2/authenticate/session | Failed to create user session token.
#     com.security.exception.TokenGenerationError - Session token could not be produced at this moment.
# """

# q = """
# API /process/forms/upload failed with the following error:
# ERROR [r-http-epoll-7] com.system.error.PSGFilter - POST | /process/forms/upload | HystrixRuntimeException: Unhandled exception for API service request. Cause: org.springframework.core.BufferOverflowException: Buffer limit exceeded (configured limit: 128KB).
# """

# used LLM to generate the query using a sample prompt (part of it).
# q = """
#     Authentication error encountered during token renewal process for endpoint /api/v4/refresh/keys.
#     com.auth.exception.TokenRefreshFailure - Failed to renew authentication credentials at this time.
# """

# q = "Cluster locator unavailable. Logs indicate failure to reach GemCluster endpoints."


# embed_text_ = embed_text([q])[0].values
# s = retrieve_chunks(embed_text_)
# print(s)