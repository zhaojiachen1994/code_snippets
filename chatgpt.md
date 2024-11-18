<details>
<summary><strong>  Hello chatgpt </strong></summary>

```python
import os
os.environ['OPENAI_API_KEY'] = "sk-m7odSEhfBulT7rimGwP9Or0cJ9bMu6A7xPNO6fA3DXNK6xog"
os.environ['OPENAI_API_BASE']= "https://api.chatanywhere.tech/v1"
import openai
from openai import OpenAI

if __name__ == "__main__":
    client = OpenAI(
        api_key = os.environ.get("OPENAI_API_KEY"),
        base_url = os.environ.get("OPENAI_API_BASE"))
    
    json_data = {
    'model': 'gpt-4o',
    'messages': [{'role': 'system', 'content': 'This is the start of the conversation.'}],
    'max_tokens': 7,
    'temperature': 0.0
	}
    
    response = client.chat.completions.create(**json_data)
```

</details>
---

