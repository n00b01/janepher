// src/components/ProfileButton.jsx
import { useState } from "react";
import { useAuth } from "../../Authcontext";

const ProfileButton = ({ onOpenSignup }) => {
  const { user, logout } = useAuth();
  const [showPopover, setShowPopover] = useState(false);

  const handleClick = () => {
    if (!user) onOpenSignup();
    else setShowPopover(!showPopover);
  };

  return (
    <div className="relative inline-block">
      <button onClick={handleClick} className="bg-blue-500 text-white px-3 py-1 rounded-full">
        Profile
      </button>

      {user && showPopover && (
        <div className="absolute right-0 mt-2 w-60 bg-white p-4 shadow-lg rounded-xl z-50">
          <img src={user.photoURL} className="w-10 h-10 rounded-full" />
          <p className="font-bold mt-2">{user.name}</p>
          <p className="text-sm text-gray-500">{user.email}</p>
          <button onClick={logout} className="mt-4 bg-red-500 text-white px-3 py-1 w-full rounded">
            Sign Out
          </button>
        </div>
      )}
    </div>
  );
};

export default ProfileButton;
