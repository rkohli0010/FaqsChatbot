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

def retrieve_chunks_nomatch(error_code) :
    client = MilvusClient(
    uri='http://3.229.150.112:19530',
    user="root",
    password="Milvus"
        )

    client.load_collection(
        collection_name="Faqs_Chatbot",
        replica_number=1 
    )

    res = client.query(
    collection_name="Faqs_Chatbot",
    filter=f"group_error_code == '{error_code}' ",
    output_fields=['text', 'group_error_code', 'individual_error_code']
    )

    resultant_list = []

    for chunk in res :
        temp_dict = {}
        resultant_list.append(chunk['text'])
    
    resultant_dict = {}

    for i in range(len(resultant_list)) :
        resultant_dict[f'Set {i+1}'] = resultant_list[i]

    return resultant_dict



