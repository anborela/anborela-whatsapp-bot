import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get("Body")
    sender = request.form.get("From")

    # Log para Railway
    print(f"📨 Mensaje recibido de {sender}: {incoming_msg}")

    resp = MessagingResponse()
    msg = resp.message()

    if "pizza" in incoming_msg.lower():
        msg.body("🍕 La pizza puede contener E250 y E160b. ¡Acompáñala con ensalada si puedes!")
    else:
        msg.body("🌿 Hola, soy Anborela. ¿Qué has comido hoy y cómo te sientes?")

    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

