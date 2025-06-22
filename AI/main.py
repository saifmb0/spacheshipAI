from openai import OpenAI
import json ,requests , random , time
import os

base_url = "https://api.aimlapi.com/v1"
api_key = os.getenv("AI_API_KEY")  # Load from environment variable

readings ={
"readings" : {
        "temperature": round(random.uniform(-80, 100), 2),
        "pressure": round(random.uniform(0.1, 1.5), 2),
        "radiation_level": round(random.uniform(0.01, 0.5), 3),
        "fuel_pressure": round(random.uniform(30, 100)),
        "engine_temperature": round(random.uniform(500, 1200)),
}
}


system_prompt = ""
user_prompt = f"data {readings} give task from data" 

api = OpenAI(api_key=api_key, base_url=base_url)


def main():
    completion = api.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=256
    )

    response = completion.choices[0].message.content

    print("User:", user_prompt)
    print("AI:", response)

if __name__ == "__main__":
    main()