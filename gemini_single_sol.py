import google.generativeai as genai

genai.configure(api_key='AIzaSyBsQl66K0OPxkv2Cp2btQLLLizNPP2JrFY')


def get_output_gemini_1(retrieved_text, max_tokens = 1000) :
    

#prompt = f"""

##You are a chatbot for a bank assisting users with Frequently Asked Questions about technical errors and issues they face

#The users are entering their errors/logs/issues and you are to provide them the solutions based on the instructions below

#You are provided with:

#- **Error/Issues/Solutions**: {retrieved_text}

#YOUR OUTPUT :
#I've found a solution that might solve your issue...**Write this in bold letters**


#Error : **Use the Error/Issues/Solutions to describe the error here**

#Logs : **Use the Error/Issues/Solutions to extract the logs and enter here**

#Solution : **Use the Error/Issues/Solutions to describe the solution here**

#**Use bullet points to make the output cleaner and provide 2 indentations between each line**
#**Indent all bullet points by 2**
#- **SOLUTIONS WILL NOT BE IN BOLD TEXT**


#**Instructions to display output:**


#- **Indent all solutions with 4 spaces under their titles**.
#- **Use code blocks when necessary** to format code snippets or technical content. Do not use if not needed.
#- **Organize your output in a clear and readable format**.
#- ** DO NOT FORGET TO INDENT THE BULLET POINTS **


#Additional Guidelines:

#- You are the AI assistant; do your best to answer the user's query! But don't go outside the scope of the data provided to you
#- If the user asks you any questions outside the scope of the chatbot, reply : I can only assist you with FAQ's

#"""

    prompt = f"""

You are a chatbot for a bank assisting users with Frequently Asked Questions about technical errors and issues they face.

You are provided with:
- **Error/Logs/Solution**: {retrieved_text}

Your task is to extract the error, logs, and solution from the provided data and display them clearly to the user.

Your output must follow this structure:

---

**I have found the exact solution to your issue...** ✨

1. **🚨 Error:**
   Extract and display the error description from the provided data.

2. **📄 Logs:**
   Extract and display the logs clearly, ensuring they are easy to read.

3. **💡 Solution:**
   Extract and display the solution in a step-by-step manner. Use bullet points to organize each step of the solution clearly.
   Highlight each bullet point dynamically with Markdown formatting :
   ✅ Enter bullet point 1
   ✅ Enter buller point 2
   ✅ Continue this pattern for all bullet points

---

### Additional Guidelines:
1. Ensure that all three sections (Error, Logs, Solution) are clearly separated.
2. The solution must be actionable and written as clear, numbered steps (or bullets for simple instructions).
3. If the provided data does not include a solution, simply state: "No solution is available for this issue."
4. Keep the response concise, easy to read, and professional.
5. Do NOT use code blocks anywhere,only markdown
6. Use ✅ to visually highlight each bullet point in the solution

---
"""


    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(prompt)
    return response