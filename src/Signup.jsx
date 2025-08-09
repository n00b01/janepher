// src/components/SignupPanel.jsx
import { motion, AnimatePresence } from "framer-motion";
import { useAuth } from "./Authcontext";
import { User } from "lucide-react";
import "./signup.css"


const SignupPanel = ({ isOpen, onClose }) => {
  const { login } = useAuth();

  const handleSignup = (e) => {
    e.preventDefault();

    // Simulate login (replace with real API later)
    const user = {
      name: "Jane Doe",
      email: "jane@styleai.com",
    };

    login(user);
    onClose();
  };

  return (
    <AnimatePresence>
      {isOpen && (
        <motion.div
          initial={{ x: "100%" }}
          animate={{ x: 0 }}
          exit={{ x: "100%" }}
          transition={{ type: "spring", stiffness: 200, damping: 25 }}
          className="signup-panel"
        >
         <h2>Sign Up</h2>
      <form onSubmit={handleSignup}>
        <input type="text" placeholder="Name" />
        <input type="email" placeholder="Email" />
        <input type="password" placeholder="Password" />
        <button type="submit">Sign Up</button>
      </form>
      <button onClick={onClose} className="close-btn">✕</button>
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default SignupPanel;
