from flask import Blueprint, request, render_template, jsonify
from app.models.models import db, Users, SampleMenu, Feedback

# Blueprint for main routes
main_bp = Blueprint('main', __name__)

# ======== ROUTES ========

# 🏡 Home - Loads testimonial.html
@main_bp.route('/')
def home():
    testimonials = Feedback.query.all()  # Fetch all feedback
    return render_template('testimonial.html', testimonials=testimonials)

# 🏠 Index Page - Main Dashboard
@main_bp.route('/index')
def index():
    return render_template('index.html')

# 📝 Feedback Page
@main_bp.route('/feedback')
def feedback():
    testimonials = Feedback.query.all()  # Fetch all feedbacks
    return render_template('testimonial.html', testimonials=testimonials)

# 🔐 Login Page
@main_bp.route('/login')
def login():
    return render_template('login.html')

# 📝 Signup Page
@main_bp.route('/signup')
def signup():
    return render_template('signup.html')

# 🍕 Menu Page
@main_bp.route('/menu')
def menu():
    menu_items = SampleMenu.query.all()
    return render_template('menu.html', menu_items=menu_items)

# 👥 Our Team Page
@main_bp.route("/team")
def team():
    return render_template("team.html")

# 📞 Contact Page 
@main_bp.route("/contact")
def contact():
    return render_template("contact.html")

# 📄 About Page 
@main_bp.route("/about")
def about():
    return render_template("about.html")


# 📄 Service Page
@main_bp.route("/service")
def service():
    return render_template("service.html")

# 📝 Booking Page
@main_bp.route("/booking")
def booking():
    return render_template("booking.html")

# 📝 Booking Page
@main_bp.route("/checkout")
def checkout():
    return render_template("checkout.html")

# ========== API ROUTES ==========

# 📚 Get all menu items
@main_bp.route('/api/menu', methods=['GET'])
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
@main_bp.route('/api/users', methods=['GET'])
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

# 🔍 Get a single user by ID
@main_bp.route('/api/user/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = Users.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({
        "user_name": user.user_name,
        "email_id": user.email_id,
        "phone_number": user.phone_number,
        "role": user.role
    })

# ✨ Add new feedback
@main_bp.route('/api/feedback', methods=['POST'])
def add_feedback():
    data = request.json
    if not data or 'user_name' not in data or 'messages' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    new_feedback = Feedback(
        user_name=data['user_name'],
        email_id=data['email_id'],
        profession=data.get('profession', ''),  # Optional profession
        messages=data['messages'],
    )
    db.session.add(new_feedback)
    db.session.commit()
    return jsonify({"message": "Feedback added successfully!"})

# ✅ Admin - Get all feedback
@main_bp.route('/api/all_feedback', methods=['GET'])
def get_all_feedback():
    feedbacks = Feedback.query.all()
    result = [
        {
            "user_name": fb.user_name,
            "email_id": fb.email_id,
            "profession": fb.profession,
            "messages": fb.messages,
        }
        for fb in feedbacks
    ]
    return jsonify(result)

# 📝 Update User Info
@main_bp.route('/api/user/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    user = Users.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    user.user_name = data.get('user_name', user.user_name)
    user.phone_number = data.get('phone_number', user.phone_number)
    user.email_id = data.get('email_id', user.email_id)
    user.role = data.get('role', user.role)

    db.session.commit()
    return jsonify({"message": "User updated successfully!"})

# ❌ Delete User
@main_bp.route('/api/user/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = Users.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully!"})

# ========== PAGE NOT FOUND HANDLER ==========
@main_bp.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
