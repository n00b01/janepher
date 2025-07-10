import React from "react";
import "./input.css";

export const Input = ({ value, onChange, onKeyDown, placeholder }) => {
  return (
    <textarea
      type="text"
      className="input"
      value={value}
      onChange={onChange}
      onKeyDown={onKeyDown}
      placeholder={placeholder}
    />
  );
};