from langchain.agents import create_agent


def check_weather(location: str) -> str:
    """Return the weather forecast for the specified location."""
    return f"It's always sunny in {location}"


graph = create_agent(model="ollama:qwen2.5:7b", tools=[check_weather])

inputs = {"messages": [{"role": "user", "content": "what is the weather in sf"}]}

# stream_mode:updates、messages、custom
for chunk in graph.stream(inputs, stream_mode="messages"):
    print(chunk[0].content, end="")
