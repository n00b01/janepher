import React from "react";
import "./profile.css"
// this is a profile page
const isloggedIn = true 
// check if user is logged in to show profile info 
// if user is not logged in show the sign up/sign in page
return(
    <>
    <div className="profile-container">
        <div className="profile-items">
            <img src="" alt="profile pic" />
            <div className="profile-text">
                <p className="name">Mark Ndwaru</p>
                <p className="email">Marcosndwarunjoroge254@gmail.com</p>
            </div>
        </div>
        <ul>
            <li>Give feedback</li>
            <li>About us</li>
        </ul>
        <div className="signOut">
            <p>Sign Out</p>
        </div>
    </div>
    </>
)
