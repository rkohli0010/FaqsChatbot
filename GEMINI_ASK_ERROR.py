import google.generativeai as genai

genai.configure(api_key='AIzaSyBsQl66K0OPxkv2Cp2btQLLLizNPP2JrFY')


def gemini_show_errors(retrieved_text, max_tokens = 1000) :
    

    #prompt = f"""
    #You are an AI agent for a bank's technical team

    #You are provided with a set of Error-Issues-Solutions : {retrieved_text}

    #From the given Error-Logs-Solutions, clearly extract the error and the logs,

    #and display only the error and logs to the user with numbering, and ask him to select which error would they like a solution to

    #Give your output in a clear and organized manner, displaying the error and the logs only

    #YOUR FIRST LINE OF OUTOUT WILL BE : I couldn't find an exact match, but here are a few errors similar to the error entered by you

    #Clearly Separate out each Error-Log using white lines! USE WHITE LINES TO SEPARATE!!!

    #Make it look neat and well organized

    #For each set of Error and Log, put a space between the error and the log
    #YOUR LAST LINE OF OUTPUT WILL BE : Please enter the number of the error to view solution


#"""

    prompt = f"""
    You are an AI agent for a bank's technical team. 🏦🤖

    You are provided with:
    - **A set of Error-Logs-Solutions**: {retrieved_text}

    Your task:
    1. Extract and display only the **Error** and **Logs** from the provided data.
    2. Display the errors and logs in a **numbered list**, formatted in Markdown.
    3. Include the following instructions for the user:
        - First line: **"I couldn't find an exact match, but here are a few errors similar to the error entered by you:"**
        - Last line: **"Please enter the number of the error to view the solution."**

    Formatting Instructions:
    - Separate each **Error** and **Log** pair with a thin white line.
    - For each error, include a space between the error description and its logs.
    - Use bullet points or numbering to clearly indicate each error-log pair.
    - Organize the output neatly and professionally for user clarity.
    - Do not use code blocks anywhere only markdown formatting
    - Clearly assign serial numbers to the error and logs, as these serial numbers will be used for downstream operations

    Example Output Format:
    ---
    **I couldn't find an exact match or an error code for your request, but here are a few errors similar to the error entered by you:** 🔍


    1️⃣. **Error Number :** Enter the serial number 
    
       **Error**: Describe the first error here.
        
       **Logs**: Relevant logs for the first error.

    2️⃣. **Error Number :** Enter the serial number 
        
       **Error**: Describe the second error.

       **Logs**: Relevant logs for the second error.

    3️⃣. Continue this pattern for the subsequent Error-Logs

    ...

    **Please enter the error number of the error to view the solution.** 💬

    DO NOT USE CODE BLOCKS ANYWHERE
    ---

"""


    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(prompt)
    return response.text
