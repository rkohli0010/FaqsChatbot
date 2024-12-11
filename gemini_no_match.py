import google.generativeai as genai

genai.configure(api_key='AIzaSyBsQl66K0OPxkv2Cp2btQLLLizNPP2JrFY')


def get_output_gemini_nomatch(retrieved_chunks, error_code) :


    category_dict = {
    
    "CLC001": "Cluster and Locator Connectivity Errors",
    "AUTH001": "Authentication and Token Validation Errors",
    "QRT001": "Queue, Rate Limiting, and Timeout Errors",
    "POL001": "Policy, Permission, and Access Errors",
    "REP001": "Reporting and Data Processing Errors",
    "SYS001": "System Connectivity and Synchronization Errors",
    "BUF001": "Static Content and Buffer Overflow Errors",
    "MBP001": "Memory, Buffer, and Payload Errors"

    }
    print(f'###ERROR CODE### : {error_code}')
    
    #prompt = f"""
    #You are an AI agent for a bank's technical team

    #You are provided with a set of Error-Issues-Solutions : {retrieved_chunks}

    #From the given Error-Logs-Solutions, clearly extract the error and the logs,

    #THE FIRST LINE OF YOUR OUTPUT WILL BE : Based on the error codes you provided, here are a few matching errors :

    #Then you will show the Error Code and Error Category
    
    #Error Code : {error_code}
    #Error Category : {category_dict[error_code]}

    #and display only the error and logs to the user, and ask him to select which error would they like a solution to

    #Dont use the word SET in the output, only add numbering. This numbering will be used to give the solution

    #Give your output in a clear and organized manner, displaying the error and the logs only

    #Make sure to display only the top 5 Error-Logs

    #Separate out all Error-Log sets using white lines

    #THE LAST LINE OF YOUR OUTPUT WILL BE : Please enter the number of the error you'd like to view



    #"""

    prompt = f"""
    You are an AI agent for a bank's technical team. 🏦🤖

    You are provided with:
    - **A set of Error-Logs-Solutions**: {retrieved_chunks}.

    Your task:
    1. Extract and display the **Error** and **Logs** from the provided data.
    2. Display the **Error Code** and **Error Category** at the top of the output.
    3. Display the errors and logs in a **numbered list**, formatted in Markdown.
    4. Include the following instructions for the user:
        - First line: **"Based on the error codes you provided, here are a few matching errors:"**
        - Last line: **"Please enter the number of the error you'd like to view."**
    5. Only include the top 5 sets Error-Log-Solutions
    6. Very clearly assign serial numbers to the Error-logs, as that is to be used further

    Formatting Instructions:
    - Start the output with the **Error Code** and its corresponding **Error Category**.
    - Separate each **Error** and **Logs** pair with a thin white line.
    - Use numbered formatting to clearly indicate each **Error-Log** pair.
    - Organize the output neatly and professionally for user clarity.
    - Do not use code blocks, only markdown formatting

    This is the error code to be included in the output : {error_code}

    This is the error cateogory to be included in the output : {category_dict[error_code]}
    Example Output Format:
    ---
    Based on the error codes you provided, here are a few matching errors: 🔍

    **Error Code:** Enter the error code here
    **Error Category:** Enter the error category here

    1️⃣. **Error Number :** Enter the serial number here
    
       **Error**: Describe the first error here.
        
       **Logs**: Relevant logs for the first error.

    2️⃣. **Error Number :** Enter the serial number here
    
       **Error**: Describe the second error here.
    
       **Logs**: Relevant logs for the second error.

    3️⃣. **Error Number :** Enter the serial number here
    
       **Error**: Describe the third error here.
    
       **Logs**: Relevant logs for the third error.

    4️⃣. Continue for additional Error-Logs

    **Please enter the error number of the error you'd like to view.** 💬
    ---

    DO NOT USE CODE BLOCKS ANYWHERE


"""
    
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(prompt)
    return response.text