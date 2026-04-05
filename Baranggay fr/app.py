from flask import Flask, render_template, url_for, request, jsonify
import bot  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('residents_login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('residents_dashboard.html')

# --- NEW: AI CHAT ROUTE ---
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get("message")
        
       
        # This calls the AI from my bot.py
        ai_response = bot.get_barangay_response(user_message)
        
        return jsonify({"response": ai_response})
    except Exception as e:
        print(f"Error in chat route: {e}")
        return jsonify({"response": "Sorry, I am having trouble connecting to the AI right now."}), 500
# -------------------------

@app.route('/profile')
def profile():
    return render_template('residents_profile.html')

@app.route('/certificates')
def certificates():
    return render_template('residents_certificaterequest.html')

@app.route('/concerns')
def concerns():
    return render_template('residents_suggestion&concerns.html')

@app.route('/appointments')
def appointments():
    return render_template('residents_apointment.html')

@app.route('/emergency')
def emergency():
    return render_template('residents_emergency.html')

@app.route('/announcements')
def announcements():
    return render_template('residents_announcements.html')

if __name__ == '__main__':
    app.run(debug=True)