import axios from "axios";

const API_URL = "http://localhost:8000/"; // Django API base URL

export const getPortfolios = async () => {
  try {
    const response = await axios.get(`${API_URL}portfolios/`);
    return response.data;
  } catch (error) {
    console.error("Error fetching portfolios:", error);
    throw error;
  }
};
