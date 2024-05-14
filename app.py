from server import app
from server.models import User, ChatData, UserConditions
from flask import jsonify, render_template

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/test")
def test():
    return render_template('test.html')

@app.route('/users')
def get_users():
    users = User.query.all()
    return jsonify([{
            'id': user.id,
            'language': user.language,
            'gender': user.gender,
            'age': user.age,
            'location': user.location,
            'whatsapp_number': user.whatsapp_number,
            'num_texts': user.num_texts
        } for user in users])

@app.route('/language')
def get_users_by_language():
    # Execute the query
    chinese_users = User.query.filter_by(language='Chinese').count()
    # return jsonify([{
    #         'id': user.id,
    #         'language': user.language,
    #         'gender': user.gender,
    #         'age': user.age,
    #         'location': user.location,
    #         'whatsapp_number': user.whatsapp_number,
    #         'num_texts': user.num_texts
    #     } for user in chinese_users])
    return jsonify(chinese_users)
    # # Print the results (for demonstration)
    # for user in chinese_users:
    #     print(f"ID: {user.id}, Language: {user.language}, Gender: {user.gender}, Age: {user.age}, Location: {user.location}, WhatsApp Number: {user.whatsapp_number}, Num Texts: {user.num_texts}")
    

@app.route('/chat_data')
def get_chat_data():
    chat_data = ChatData.query.all()
    # Process chat data as needed
    return jsonify([{
        'id': data.id,
        'whatsapp_number': data.whatsapp_number,
        'message_sent': data.message_sent,
        'response_sent': data.response_sent,
        'time_sent': data.time_sent.isoformat() if data.time_sent else None,
        'day_sent': data.day_sent.isoformat() if data.day_sent else None,
        'initial_context': data.initial_context,
        'updated_context': data.updated_context,
        'user_conditions_id': data.user_conditions_id
    } for data in chat_data])


@app.route('/user_conditions')
def get_user_conditions():
    user_conditions = UserConditions.query.all()
    # Process user conditions data as needed
    return jsonify([{
        'id': condition.id,
        'whatsapp_number': condition.whatsapp_number,
        'disease': condition.disease,
        'description': condition.description,
        'prevention': condition.prevention,
        'cure': condition.cure,
        'probability': condition.probability
    } for condition in user_conditions])