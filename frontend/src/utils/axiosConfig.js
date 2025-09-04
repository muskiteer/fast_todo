import axios from 'axios';
import { store } from '../store';
import { logout } from '../store/authSlice';
import { toast } from 'react-toastify';

const API_URL = 'http://localhost:8000/api';

// Create axios instance
const axiosInstance = axios.create({
  baseURL: API_URL,
});

// Request interceptor to add auth token
axiosInstance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor to handle unauthorized responses
axiosInstance.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    if (error.response && (error.response.status === 401 || error.response.status === 403)) {
      // Token is invalid or expired
      toast.error('Session expired. Please login again.');
      store.dispatch(logout());
      // Redirect will happen automatically due to protected routes
    }
    return Promise.reject(error);
  }
);

export default axiosInstance;
