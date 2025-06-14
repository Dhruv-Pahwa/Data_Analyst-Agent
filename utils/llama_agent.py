import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TOGETHER_API_KEY")

def ask_llama(prompt):
    url = "https://api.together.xyz/inference"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
        "prompt": prompt,
        "max_tokens": 1024,
        "temperature": 0.7,
        "top_p": 0.9
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        print("🛰️ Status Code:", response.status_code)
        print("🛰️ Response Text:", response.text)

        if response.status_code != 200:
            return f"❌ Error from Together.ai: {response.text}"

        res_json = response.json()
        output = res_json.get("output") or res_json.get("choices", [{}])[0].get("text")

        if not output:
            return "⚠️ No output received from model."

        return output.strip()

    except Exception as e:
        return f"❌ Exception occurred: {str(e)}"
