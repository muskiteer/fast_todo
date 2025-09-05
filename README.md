# FastAPI Todo App with React Frontend

A full-stack todo application built with FastAPI (backend) and React (frontend) featuring JWT authentication, async database operations, and modern UI.

## 🚀 Features

- **Authentication**: JWT-based user registration and login
- **Todo Management**: Create, read, update, delete todos
- **User Isolation**: Each user sees only their own todos
- **Real-time Updates**: Optimistic UI updates with error handling
- **Responsive Design**: Modern React UI with toast notifications
- **Auto-logout**: Automatic session management on token expiration
- **Async Operations**: FastAPI with async SQLAlchemy for better performance

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - Async ORM for database operations
- **SQLite** - Lightweight database (easily switchable)
- **JWT** - JSON Web Tokens for authentication
- **Bcrypt** - Password hashing
- **Uvicorn** - ASGI server

### Frontend
- **React 19** - Modern React with hooks
- **Redux Toolkit** - State management
- **React Router** - Client-side routing
- **Axios** - HTTP client with interceptors
- **React Toastify** - Toast notifications
- **Vite** - Fast development server and build tool

## 📁 Project Structure

```
├── backend/
│   ├── internal/          # Core utilities
│   │   ├── database.py    # Database configuration
│   │   ├── jwt.py         # JWT utilities
│   │   └── get_token.py   # Token validation
│   ├── models/            # Database models & CRUD
│   │   ├── user.py        # User authentication
│   │   └── todos.py       # Todo operations
│   ├── routes/            # API endpoints
│   │   └── routes.py      # All routes
│   ├── main.py           # FastAPI application
│   └── requirements.txt   # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── pages/         # Page components
│   │   ├── store/         # Redux store & slices
│   │   ├── utils/         # Utilities (axios config)
│   │   └── App.jsx        # Main app component
│   ├── package.json       # Node dependencies
│   └── vite.config.js     # Vite configuration
└── README.md             # This file
```

## 🚦 Getting Started

### Prerequisites
- Python 3.9+
- Node.js 16+
- npm or yarn

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/muskiteer/fast_todo
   cd fast_todo
   ```

2. **Set up Python virtual environment**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (optional)
   ```bash
   cp .env.example .env
   # Edit .env with your configurations
   ```

5. **Run the backend server**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

   Backend will be available at: `http://localhost:8000`
   API docs at: `http://localhost:8000/docs`

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

   Frontend will be available at: `http://localhost:5173`

## 🔑 API Endpoints

### Authentication
- `POST /api/users/register` - Register new user
- `POST /api/users/login` - User login
- `GET /api/users/auth` - Verify authentication

### Todos
- `GET /api/todos/` - Get user's todos
- `POST /api/todos/` - Create new todo
- `PUT /api/todos/{id}` - Update todo
- `DELETE /api/todos/{id}` - Delete todo

## 🔒 Authentication Flow

1. User registers/logs in → receives JWT token
2. Token stored in localStorage
3. Axios interceptor adds token to requests
4. Backend validates token for protected routes
5. Auto-logout on token expiration/invalid token

## 🧪 Development

### Running in Development Mode

**Terminal 1 (Backend):**
```bash
cd backend
source venv/bin/activate
uvicorn main:app --reload
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm run dev
```

### Database

- SQLite database (`test.db`) is created automatically
- Database tables are initialized on startup
- Easily switchable to PostgreSQL/MySQL by changing connection string

## 📦 Production Deployment

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Frontend
```bash
cd frontend
npm run build
# Serve the dist/ folder with your preferred web server
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues

- None at the moment

## 🔮 Future Enhancements

- [ ] Todo categories/tags
- [ ] Due dates and reminders
- [ ] Todo sharing between users
- [ ] Dark/Light theme toggle
- [ ] Mobile app with React Native
- [ ] Todo search and filtering
- [ ] Priority levels
- [ ] Todo attachments

## 📞 Support

If you have any questions or run into issues, please open an issue on GitHub.

---

**Happy coding! 🎉**
