import React from "react";
import "./Avatar.css";

export const Avatar = ({ src, alt = "Avatar" }) => {
  return <img className="avatar" src={src} alt={alt} />;
};
