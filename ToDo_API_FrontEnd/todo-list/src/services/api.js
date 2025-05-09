import axios from 'axios';

const api = axios.create({
  baseURL: 'https://api-backend-343319688013.us-central1.run.app',
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;