from langchain.agents import create_agent


def check_weather(location: str) -> str:
    """Return the weather forecast for the specified location."""
    return f"It's always sunny in {location}"


agent = create_agent(model="ollama:qwen2.5:7b", tools=[check_weather])

results = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

# results = agent.invoke(
#     {"messages": [{"role": "user", "content": "How many people in sf"}]}
# )

messages = results["messages"]
print(f"Total messages: {len(messages)}")

for message in messages:
    message.pretty_print()


# Q1 : what is the weather in sf
# Total messages: 4
# ================================ Human Message =================================

# what is the weather in sf
# ================================== Ai Message ==================================
# Tool Calls:
#   check_weather (a1e7c092-fcff-4f95-8b60-bcf298c39378)
#  Call ID: a1e7c092-fcff-4f95-8b60-bcf298c39378
#   Args:
#     location: sf
# ================================= Tool Message =================================
# Name: check_weather

# It's always sunny in sf
# ================================== Ai Message ==================================

# The weather forecast for San Francisco indicates it will be sunny. However, please note that this is a fictional response, and actual weather conditions may vary. For accurate weather information, you can check reliable weather websites or apps.


# Q2:How many people in sf
# Total messages: 2
# ================================ Human Message =================================

# How many people in sf
# ================================== Ai Message ==================================

# I'm sorry, I couldn't find direct information on the exact population of San Francisco (SF) through my current capabilities. You can easily find this information by searching online or using a database like the U.S. Census Bureau for the most recent estimate. Would you like me to provide more general information about San Francisco instead?
