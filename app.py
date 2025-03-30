from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get("Body")
    resp = MessagingResponse()
    msg = resp.message()

    if "pizza" in incoming_msg.lower():
        msg.body("🍕 La pizza puede contener E250 y E160b. ¡Acompáñala con ensalada si puedes!")
    else:
        msg.body("Hola 🌿 Soy Anborela. Cuéntame qué comiste y cómo te sentiste.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
