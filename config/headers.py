import os
from dotenv import load_dotenv


load_dotenv()

class Headers:

    basic = {
        "api_key": f"Bearer {os.getenv('API_TOKEN')}"
    }