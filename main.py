from flask import Flask, render_template, request
import chat_gpt

app = Flask(__name__)

chatgpt = chat_gpt.ChatGPT(system_content="设定你是个老年看护器人")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}!"
    return render_template("index.html")


@app.route("/chat", methods=["GET", "POST"])
def chat_with_chatgpt():
    user_message = request.form.get("user_message")
    ai_output = chatgpt.ask_gpt(user_message)
    return {"chatbot_reply": ai_output}


if __name__ == "__main__":
    app.run(debug=True)
