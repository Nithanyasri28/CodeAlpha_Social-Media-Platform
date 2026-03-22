                    📱 Social Media Platform (Django)
A full-stack Social Media Web Application built using Django.
Users can create posts, upload images/videos, like, comment, follow others, and interact in a dynamic social feed.


🚀 Features
 🔐 User Authentication (Login / Signup / Logout)
 📝 Create Posts (Image & Video Upload)
 ❤️ Like & Unlike Posts
 💬 Comment on Posts
 👥 Follow / Unfollow Users
 📰 Personalized Feed
 🔍 Search Users & Posts
 🗑 Delete Own Posts
 👤 User Profile Page
 📸 Media Preview before Upload

 
🛠️ Tech Stack
 Backend: Django (Python)
 Frontend: HTML, CSS, JavaScript
 Database: SQLite
 Media Handling: Django Media Files
 Version Control: Git & GitHub
 
📂 Project Structure
social_media/
│── accounts/
│── posts/
│── templates/
│── static/
│── media/
│── db.sqlite3
│── manage.py


⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/social-media-platform.git
cd social-media-platform
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Apply Migrations
python manage.py migrate
5️⃣ Run Server
python manage.py runserver
👉 Open in browser:
http://127.0.0.1:8000/
