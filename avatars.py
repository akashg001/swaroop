import openai
import requests
from io import BytesIO
from PIL import Image


openai.api_key = "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"


def avatar(prompt):
    response = openai.Image.create(
    prompt=prompt,
    n=1,
    size='256x256'
    )
    img_data = requests.get(response['data'][0]['url']).content
    return response
    

def context(qstn):
    model_engine = "text-davinci-003"
    prompt = qstn

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    return response