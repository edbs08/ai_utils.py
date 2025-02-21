import requests

class LLMConnection:
    def __init__(self, model=None):
        API_KEY = "2J9J86TiKivzUXACJvxZCH1CFNoupMiw"  
        self.llm_api_address = "https://api.deepinfra.com/v1/openai/chat/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

    def send_request_llm(self,prompt,model=None,system_prompt=None):
        llm_model = model or "meta-llama/Llama-3.3-70B-Instruct"
        #default system prompt 
        s_prompt = system_prompt or "You are a professional assistant"

        data = {
            "model": llm_model,  
            "messages": [
                {"role": "system", "content": s_prompt},
                {"role": "user", "content": prompt}
            ],
            "stream": False  # Disable streaming
        }

        response = requests.post(self.llm_api_address, headers=self.headers, json=data)

        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content']
            status = True
        else:
            print("Request failed, error code:", response.content)
            content = ""
            status = False
        
        return status, content

if __name__=="__main__":
    llm = LLMConnection()
    status, content = llm.send_request_llm("say hi in two words")
    print(content)


