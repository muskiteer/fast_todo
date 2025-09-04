import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { logout } from '../store/authSlice';
import { Link } from 'react-router-dom';

export default function Navbar() {
  const dispatch = useDispatch();
  const { isAuthenticated, user } = useSelector((state) => state.auth);

  return (
    <nav className="navbar">
      <div className="brand">Todo App</div>
      
      <div className="nav-links">
        {isAuthenticated ? (
          <>
            <span>Welcome, {user?.username}</span>
            <button onClick={() => dispatch(logout())}>Logout</button>
          </>
        ) : (
          <>
            <Link to="/login">Login</Link>
            <Link to="/register">Register</Link>
          </>
        )}
      </div>
    </nav>
  );
}