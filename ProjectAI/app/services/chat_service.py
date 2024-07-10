import httpx

async def get_ai_response(message: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.post("URL_ВАШЕГО_ИИ", json={"message": message})
        return response.json().get("response")
