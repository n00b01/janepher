import React from "react";
import "./button.css";

export const Button = ({ children, onClick, className = "", size = "md" }) => {
  return (
    <button onClick={onClick} className={`btn btn-${size} ${className}`}>
      {children}
    </button>
  );
};