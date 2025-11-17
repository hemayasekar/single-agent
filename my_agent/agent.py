
from datetime import datetime
import pytz
from google.adk.agents.llm_agent import Agent

def get_current_time(city: str) -> dict:
    # """Returns the current time in a specified city."""
    # return {"status": "success", "city": city, "time": "10:30 AM"}

    try:
        # Map cities to timezones
        timezone_map = {
            "new york": "America/New_York",
            "london": "Europe/London",
            "tokyo": "Asia/Tokyo",
            "sydney": "Australia/Sydney",
            "mumbai": "Asia/Kolkata",
            "singapore": "Asia/Singapore",
        }

        tz_name = timezone_map.get(city.lower())
        if tz_name is None:
            return {"status": "error", "message": "City not supported."}

        tz = pytz.timezone(tz_name)
        current_time = datetime.now(tz).strftime("%I:%M %p")

        return {
            "status": "success",
            "city": city,
            "time": current_time
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}


def get_weather(city: str) -> dict:
    # Placeholder
    return {"status": "success", "city": city, "weather": "Sunny, 25°C"}


def web_search(query: str) -> dict:
    # Dummy placeholder
    return {
        "status": "success",
        "query": query,
        "results": [
            "Result 1 about " + query,
            "Result 2 about " + query,
        ]
    }


def read_file(path: str) -> dict:
    # read file in the path
    try:
        with open(path, "r") as f:
            content = f.read()

        return {"status": "success", "path": path, "content": content}

    except Exception as e:
        return {"status": "error", "message": str(e)}


def summarize_text(text: str) -> dict:
    # LLM will use this output to generate a real summary
    return {"status": "success", "text": text}




root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='''
You are a helpful AI assistant.
Use tools when needed.
''',
    tools=[
        get_current_time,
        get_weather,
        web_search,       
        read_file,        
        summarize_text    
    ],
)

