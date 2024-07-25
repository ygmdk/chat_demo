import openai
import config
import json

# 设置API密钥
client = openai.OpenAI()


class ChatGPT:
    def __init__(self, system_content):
        self.messages = [
            {
                "role": "system",
                "content": system_content,
            }
        ]
        self.filename = "./user_messages.json"

    def ask_gpt(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        response = client.chat.completions.create(
            model=config.MODEL, messages=self.messages
        )
        ai_message = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": ai_message})
        return ai_message

    def save_messages(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.messages, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    chatgpt = ChatGPT(system_content="设定你是个老年看护器人")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        ai_output = chatgpt.ask_gpt(user_input)
        print("AI: \n\n", ai_output)

    # chatgpt.save_messages()
