import React, { useEffect, useState } from "react";
import { getPortfolios } from "../api/portfolioApi";

const PortfolioList = () => {
  const [portfolios, setPortfolios] = useState([]);

  useEffect(() => {
    getPortfolios()
      .then(data => setPortfolios(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Portfolios</h2>
      <ul>
        {portfolios.map(portfolio => (
          <li key={portfolio.id}>{portfolio.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default PortfolioList;