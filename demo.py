import os
from extracty import LLMExtractor
from dotenv import load_dotenv
import json
def jls_extract_def():
    return load_dotenv
jls_extract_def()()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
def main() -> None:
    fields = {
        "rank": int,
        "repo_name": str,
        "small_desc": str,
    }
    extractor = LLMExtractor(
        url="https://www.github.com/trending",
        query = "What are the top 5 trending repositories on GitHub?",
        api_key = OPENAI_API_KEY,
        fields=fields,
        gpt_model="gpt-3.5-turbo",
    )
    data = extractor.extract()
    with open("output.json",'w') as f:
        print("we are here")
        f.write(json.dumps(data.model_dump_json(), indent=4))
        #f.write(data.model_dump_json())
if __name__ == "__main__":
    main()
 