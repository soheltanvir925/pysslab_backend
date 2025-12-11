import axios from "axios";

const axiosClient = axios.create({
  baseURL: "http://localhost:8000",   // Django backend URL
  withCredentials: true,
});

export default axiosClient;


