# 🎬 My Tracker app

A full-stack Django web application to manage your personal watch list.

Users can:
- Add titles
- Edit entries
- Delete entries
- Mark as Completed or Pending
- Manage their own personalized anime list securely

---

# 🚀 Features

✅ User Authentication  
✅ Add New Titles  
✅ Edit Existing  Entries  
✅ Delete Entries  
✅ Mark as Completed  
✅ Mark as Pending  
✅ Pagination Support  
✅ Django Messages Framework  
✅ User-Specific Anime Lists  
✅ Secure CRUD Operations  

---

# 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| Django | Backend Framework |
| HTML/CSS | Frontend |
| SQLite3 | Database |
| Django Authentication | User Login System |

---

# 📂 Project Structure

```bash
project/
│
├── anime_app/
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   ├── create.html
│   │   ├── edit.html
│   │   └── animelist.html
│   │
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── manage.py
└── db.sqlite3
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/anime-tracker.git
cd anime-tracker
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install django
```

---

## 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5️⃣ Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

## 6️⃣ Run the Development Server

```bash
python manage.py runserver
```

Open in browser:

```bash
http://127.0.0.1:8000/
```

---

# 🔐 Authentication

Protected routes use Django's built-in authentication system.

```python
@login_required
```

This ensures only logged-in users can access and modify their anime lists.

---

# 📄 Views Overview

## 🏠 Home Page

Displays the landing page.


## ➕ Create Anime Entry

Allows users to:
- Add anime
- Edit anime
- Save anime per user


## ✏️ Edit Anime Entry

Features:
- Edit existing anime
- Delete anime entries
- Pagination support



## 📋 Anime List Page

Displays all anime entries of the logged-in user.



## ✅ Complete Task

Marks anime as completed.



## ⏳ Pending Task

Marks anime as pending.



# 📚 Pagination

The project uses Django's built-in paginator.

Only 4 anime entries are displayed per page.

# 🔔 Messages Framework

Success notifications are shown using Django Messages Framework.

# 🌟 Future Improvements

- Anime Poster Integration using Jikan API
- Search and Filter Anime
- Dark Mode
- Anime Ratings
- Watch Progress Tracker
- REST API
- React Frontend
- Responsive UI Improvements

---

# 📸 Screenshots

<img width="1536" height="732" alt="Screenshot 2026-05-13 150124" src="https://github.com/user-attachments/assets/d94e3cf2-2a7a-4805-b7b8-5fe9334c9a74" />
<img width="1536" height="726" alt="Screenshot 2026-05-13 150157" src="https://github.com/user-attachments/assets/b50b6176-2575-4afa-9bd5-a78f1fe3251c" />
<img width="1520" height="728" alt="Screenshot 2026-05-13 150339" src="https://github.com/user-attachments/assets/51eb5d62-03b8-43cc-8790-890cebc18a3e" />
<img width="1536" height="728" alt="Screenshot 2026-05-13 150359" src="https://github.com/user-attachments/assets/40be47cf-0ba8-4f5b-b423-fcdf00aa0498" />
<img width="1512" height="723" alt="Screenshot 2026-05-13 150426" src="https://github.com/user-attachments/assets/6c4831ef-edfa-4145-b192-8447233fa977" />
<img width="1536" height="726" alt="Screenshot 2026-05-13 150444" src="https://github.com/user-attachments/assets/32ef126b-ec76-4d78-8cff-869780ca6112" />
<img width="1532" height="730" alt="Screenshot 2026-05-13 150508" src="https://github.com/user-attachments/assets/6e21aaf6-f849-4ccb-a0ed-009268a45273" />


# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Developed by **Chanchal**

---

# ⭐ Support

If you liked this project, give it a ⭐ on GitHub.
