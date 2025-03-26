from flask import Blueprint, request, render_template, jsonify
from app.models.models import db, Users, SampleMenu, Feedback

# Blueprint for main routes
main_bp = Blueprint('main', __name__)

# ======== ROUTES ========

# 🏡 Home route - Loads testimonial.html
@main_bp.route('/')
def home():
    testimonials = Feedback.query.all()  # Fetch all feedbacks
    return render_template('testimonial.html', testimonials=testimonials)

# 📝 Feedback page
@main_bp.route('/feedback_page')
def feedback_page():
    testimonials = Feedback.query.all()
    return render_template('testimonial.html', testimonials=testimonials)

# 🔐 Login page
@main_bp.route('/login')
def login_page():
    return render_template('login.html')

# 📝 Signup page
@main_bp.route('/signup')
def signup_page():
    return render_template('signup.html')

# 🍕 Menu page
@main_bp.route('/menu_page')
def menu_page():
    return render_template('menu.html')

# ========== API ROUTES ==========

# 📚 Get all menu items
@main_bp.route('/menu', methods=['GET'])
def get_menu():
    menu = SampleMenu.query.all()
    result = [
        {
            "id": item.id,
            "food_items": item.food_items,
            "price": item.price,
            "description": item.description,
            "is_veg": item.is_veg,
        }
        for item in menu
    ]
    return jsonify(result)

# 👥 Get all users
@main_bp.route('/users', methods=['GET'])
def get_users():
    users = Users.query.all()
    result = []
    for user in users:
        result.append({
            'user_id': user.user_id,
            'user_name': user.user_name,
            'phone_number': user.phone_number,
            'email_id': user.email_id,
            'role': user.role
        })
    return jsonify(result)

# 🔍 Get a single user
@main_bp.route('/user/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = Users.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"user_name": user.user_name, "email_id": user.email_id})

# ✨ Add feedback
@main_bp.route('/feedback', methods=['POST'])
def add_feedback():
    data = request.json
    new_feedback = Feedback(
        user_name=data['user_name'],
        email_id=data['email_id'],
        profession=data.get('profession', ''),  # Optional profession
        messages=data['messages'],
    )
    db.session.add(new_feedback)
    db.session.commit()
    return jsonify({"message": "Feedback added successfully!"})
