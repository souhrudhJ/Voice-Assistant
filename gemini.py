import google.generativeai as genai


API_KEY = ""
genai.configure(api_key = API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

def samantha(prompt):
    response = model.generate_content(prompt)
    return response.text

