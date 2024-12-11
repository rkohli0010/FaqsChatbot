import google.generativeai as genai

genai.configure(api_key='AIzaSyBsQl66K0OPxkv2Cp2btQLLLizNPP2JrFY')


def gemini_show_sol(retrieved_text, chat_history, user_query, max_tokens = 1000) :
    

    #prompt = f"""
    #This is the users current chat history : {chat_history}

    #The user has been asked to select an error by entering the serial number corresponding to the error, this is the users selection : {user_query}

    #These are the ERROR-LOG-SOLUTION : {retrieved_text}

    #Refer to the chat history and match the users entered number and the serial number of the errors

    #Based on the chat history, the users selection and the retrieved text, show the solution that corresponds to the users selection in a clear and organized manner

    #Use bullet points to organize the solutions, use bullet points only for solutions

    #Your output will only have the Error, the Log and the Solution of the selected Error

  
#"""
    prompt = f"""
You are a chatbot for a bank assisting users with Frequently Asked Questions about technical errors and issues they face.


Your task is to:
1. The user has been asked to select an error by entering the serial number corresponding to the error, this is the users selection : {user_query}
2. Refer to the provided chat history and match the user's entered number with the serial number of the errors. This is the chat history : {chat_history}
3. Based on the user's selection and the retrieved data, display the corresponding **Error**, **Logs**, and **Solution** clearly. These are the error log solutions : {retrieved_text}
4. Use Markdown formatting to organize the output in a clear and readable manner.

Your output must follow this structure:

---

**Here is the solution for the selected error:** 🎯

1. **🚨 Error:**
   Extract and display the error description from the provided data.

2. **📄 Logs:**
   Extract and display the logs clearly, ensuring they are easy to read.

3. **💡 Solution:**
   Extract and display the solution in a step-by-step manner. Use bullet points to organize each step of the solution clearly.
   Highlight each bullet point dynamically with Markdown formatting :
   ✅ Enter bullet point 1 here
   ✅ Enter buller point 2 here
   ✅ Continue this pattern for all bullet points

---

### Additional Guidelines:
1. Ensure that all three sections (**Error**, **Logs**, **Solution**) are clearly separated with a blank line.
2. The **Solution** section should use bullet points for multi-step instructions.
3. If the provided data does not include a solution, reply: "No solution is available for this issue."
4. Keep the response professional, well-structured, and user-friendly.
5. Do not use code blocks anywhere, only markdown formatting
6. Use ✅ in place of bullet points to visually highlight each bullet point in the solution


---

    """
    print(f'###THIS IS THE CHAT HISTORY GOING TO SELECT ANSWER : {chat_history}')
    print(f'###THIS IS THE USER INPUT : {user_query}')

    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(prompt)
    return response.text
