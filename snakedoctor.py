import requests
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()



class SnakeDoctor():
    def __init__(self):
        self.client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


    def analyze_product(self,product_name,brand,ingredients):
        prompt=f"""
            Analyze this food product for healthiness in english:
            product={product_name}
            brand={brand}
            ingredients={ingredients}

            Provide response in this exact format:
            COMMENT: [Brief health assessment - 1-2 sentences]
            SCORE: [Number from 1-10 where 1=very unhealthy, 10=very healthy]
            CATEGORY: [Healthy Snack/Processed Food/Sugary Drink/Neutral/etc.]
            SUGGESTION: [If score < 6, suggest SPECIFIC ALTERNATIVE PRODUCTS that are healthier but similar. If score >= 6, say "Good choice!"]
    """


        try:
            response = self.client.responses.create(
                model="gpt-5-nano",
                input=prompt
            )
            return response.output_text
        except Exception as e:
            return f"COMMENT: AI analysis unavailable\nSCORE: N/A\nCATEGORY: Unknown\nFACTORS: Error\nSUGGESTION: Try again later"


