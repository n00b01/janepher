import React from "react";
import "./card.css";
import janapher_logo from "../janepher.svg"

export const Card = ({ children, className = "",sender }) => {
  return <>
  <div className="wrapper">
 {sender === "ai" && (
        <div className="message_icon">
          <img src={janapher_logo} alt="ai" width="30px" height="30px" />
        </div>
      )}
      <div className={`card ${className}`}>{children}</div>
  </div>
   </>
};

export const CardContent = ({ children }) => {
  return <div className="card-content">{children}</div>;
};