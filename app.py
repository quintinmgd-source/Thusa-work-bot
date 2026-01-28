from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFY_TOKEN = "thusa_verify_token"

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Thusa Work Bot is live 🚀",
        "status": "ok"
    })

# STEP 1: Verification (Meta calls this)
@app.route("/webhook", methods=["GET"])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if token == VERIFY_TOKEN:
        return challenge
    return "Verification failed", 403

# STEP 2: Receive messages
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("INCOMING MESSAGE:", data)
    return "EVENT_RECEIVED", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
