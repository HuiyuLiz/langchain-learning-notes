from langchain.agents import create_agent

agent = create_agent(model="ollama:qwen2.5:7b")

results = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

messages = results["messages"]
print(f"Total messages: {len(messages)}")

for message in messages:
    message.pretty_print()

# Total messages: 2
# ================================ Human Message =================================

# what is the weather in sf
# ================================== Ai Message ==================================

# To provide you with the most accurate and up-to-date information on the current weather in San Francisco (SF), I would need to check the latest weather reports or forecasts from a reliable source such as the National Weather Service, Weather.com, or another trusted meteorological service.

# However, generally speaking, San Francisco's climate is mild and temperate. Here are some typical characteristics:

# - **Temperature:** In summer (June to August), temperatures usually range from 59°F to 70°F (15°C to 21°C). Winters can be cool with nighttime lows around 43°F (6°C).
# - **Precipitation:** San Francisco receives most of its rainfall in the winter months, particularly from December to March.
# - **Humidity and Fog:** The city is known for its frequent fog, especially during the summer months. This is due to the coastal nature of the region.

# For the latest weather conditions, please check a current weather report or app for San Francisco.
