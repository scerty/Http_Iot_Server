import requests


API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/bc807aa418348e06d79c12556be14748/ai/run/"
headers = {"Authorization": "Bearer fRDOkAo6Rv1YArE6X85r1tHAVVkzyBq6M2JsVbJu"}


def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()


inputs = [
    { "role": "system", "content": "You are a norwaian teacher" },
    { "role": "user", "content": "skriv norsk test skriv som html code ", "stream": True}
];
output = run("@cf/meta/llama-3-8b-instruct", inputs)
print(output)















"""
$ curl -X POST \
"https://api.cloudflare.com/client/v4/accounts/bc807aa418348e06d79c12556be14748/ai/run/@cf/meta/llama-2-7b-chat-fp16" \
-H "Authorization: Bearer fRDOkAo6Rv1YArE6X85r1tHAVVkzyBq6M2JsVbJu" \
-H "Content-Type:application/json" \
-d '{ "prompt": "where is new york?", "stream": true }'

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
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

export HUGGINGFACE_TOKEN=yhf_FjDHggXOYEojXmLdELRtJXWZRCZjkFnAok


https://llama3-1.llamameta.net/*?Policy=eyJTdGF0ZW1lbnQiOlt7InVuaXF1ZV9oYXNoIjoib3VoeDhyZW45cjQ5N212MThsc3FxMmRwIiwiUmVzb3VyY2UiOiJodHRwczpcL1wvbGxhbWEzLTEubGxhbWFtZXRhLm5ldFwvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTcyMjAxNzkwNX19fV19&Signature=IOUDXEhafqYpGdhXuLSH5-osRCqNxf9CJCg1JZ6F%7EIpNwAF3LpkumbL9hCDVs9Kk5xWGPTZXew2v57akoV2IbreGishlRKHYnJY-kVsuY78Ss6CFUrgSr7ZDlpTj7fyrMpDoPYDbglJNTtJ%7EOXaRJe2RFCIjfyM3O%7Elweikwl3cX0E3mwy3kh4sNtK-j5WuJzEzo23lmxwo6mG-KCqZs%7EhkAx7725zv%7EN%7ExBjFtqF0b15VwwnyQChtXq2-ioG5ZopRrQVmi8LQRfHbyS8MlKaodzsq15eZTUipbJ0Zo2-6hUWj4O%7EScCC1aShi3Aqo-c7SHW8yjewMIoHpHXEA1rcQ__&Key-Pair-Id=K15QRJLYKIFSLZ&Download-Request-ID=1946663859183122
"""