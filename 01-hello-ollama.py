# references: https://docs.langchain.com/oss/python/integrations/chat/ollama

# from langchain_ollama import ChatOllama

# llm = ChatOllama(
#     model="llama3.1",
#     temperature=0,
#     # other params...
# )

# messages = [
#     (
#         "system",
#         "You are a helpful assistant that translates English to French. Translate the user sentence.",
#     ),
#     ("human", "I love programming."),
# ]
# ai_msg = llm.invoke(messages)

# # AIMessage(content='The translation of "I love programming" in French is:\n\n"J\'adore la programmation."', additional_kwargs={}, response_metadata={'model': 'llama3.1', 'created_at': '2025-06-25T18:43:00.483666Z', 'done': True, 'done_reason': 'stop', 'total_duration': 619971208, 'load_duration': 27793125, 'prompt_eval_count': 35, 'prompt_eval_duration': 36354583, 'eval_count': 22, 'eval_duration': 555182667, 'model_name': 'llama3.1'}, id='run--348bb5ef-9dd9-4271-bc7e-a9ddb54c28c1-0', usage_metadata={'input_tokens': 35, 'output_tokens': 22, 'total_tokens': 57})

# print(ai_msg.content)

# from langchain_ollama import ChatOllama

# model = ChatOllama(
#     model="deepseek-r1:1.5b",
#     base_url="http://localhost:11434",
#     temperature=0.1,
# )


# for chunk in model.stream("簡單解釋LLM"):
#     print(chunk.content, end="", flush=True)

# references: https://docs.langchain.com/oss/python/langchain/models

from langchain.chat_models import init_chat_model

model = init_chat_model(
    "ollama:deepseek-r1:1.5b",
    # Set streaming=False to disable streaming for the chat model
    # streaming=False,
    base_url="http://localhost:11434",
    temperature=0.1,
    timeout=30,
    max_token=2000,
)

for chunk in model.stream("解釋NLP"):
    print(chunk.content, end="", flush=True)
