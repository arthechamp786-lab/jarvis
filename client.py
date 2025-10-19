from google import genai


client = genai.Client(api_key="AIzaSyCYVZWxSFZx1MZPG6d20EXSQWaSAHFfD90")
                


response = client.models.generate_content(
    model="gemini-2.5-flash", contents="who is shahrukhkan"
)
print(response.text)


