import openai

openai.api_key = "YOUR_OPENAI_KEY"  # Replace with your actual key or load from env

def is_malicious_text(text):
    try:
        response = openai.Moderation.create(input=text)
        flagged = response["results"][0]["flagged"]
        return flagged
    except Exception as e:
        print(f"Moderation API Error: {e}")
        return False
