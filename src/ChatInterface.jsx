import React, { useState } from "react";
import { Card, CardContent } from "./assets/components/card";
import { Button } from "./assets/components/button";
import { Input } from "./assets/components/input";
import { Avatar } from "./assets/components/Avatar";
import { Settings, Star, User } from "lucide-react";
import { motion } from "framer-motion";


import "./ChatInterface.css";

const dummyHistory = [
  { id: 1, title: "Summer outfit ideas" },
  { id: 2, title: "Red carpet looks" },
];

const dummyMessages = [
  { sender: "user", text: "Show me some party outfits" },
  {
    sender: "ai",
    text: "Here are a few looks you might like:",
    images: [
      {
        url: "https://example.com/image1.jpg",
        source: "https://source1.com",
      },
      {
        url: "https://example.com/image2.jpg",
        source: "https://source2.com",
      },
    ],
  },
];

const ChatInterface = () => {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState(dummyMessages);
  const [favorites, setFavorites] = useState([]);
  const [showFavorites, setShowFavorites] = useState(false);

  const sendMessage = () => {
    if (!input.trim()) return;
    setMessages([...messages, { sender: "user", text: input }]);
    setInput("");
    // Send input to Python backend here
  };

  const addToFavorites = (img) => {
    setFavorites((prev) => [...prev, img]);
  };

  const FavoritesPage = () => (
    <div className="favorites-container">
      <h2 className="favorites-title">My Favorites</h2>
      <div className="favorites-grid">
        {favorites.map((img, idx) => (
          <a
            key={idx}
            href={img.source}
            target="_blank"
            rel="noopener noreferrer"
          >
            <img
              src={img.url}
              alt="Favorite"
              className="favorite-img"
            />
          </a>
        ))}
      </div>
    </div>
  );

  return (
    <div className="chat-container">
      <aside className="chat-sidebar">
        <div>
          <h2 className="sidebar-title">History</h2>
          <ul>
            {dummyHistory.map((item) => (
              <li key={item.id} className="history-item">
                {item.title}
              </li>
            ))}
          </ul>
        </div>
        <div className="sidebar-icons">
          <User className="icon" />
          <Star className="icon" onClick={() => setShowFavorites(!showFavorites)} />
          <Settings className="icon" />
        </div>
      </aside>
      <main className="chat-main">
        {showFavorites ? (
          <FavoritesPage />
        ) : (
          <>
            <div className="chat-messages">
              {messages.map((msg, i) => (
                <motion.div
                  key={i}
                  className={`message-wrapper ${msg.sender === "user" ? "align-right" : "align-left"}`}
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.3 }}
                >
                  <Card className={`message-card ${msg.sender === "ai" ? "ai-message" : "user-message"}`}>
                    <CardContent>
                      <p className="message-text">{msg.text}</p>
                      {msg.images && (
                        <div className="image-carousel">
                          {msg.images.map((img, idx) => (
                            <div key={idx} className="carousel-item">
                              <a href={img.source} target="_blank" rel="noopener noreferrer">
                                <img
                                  src={img.url}
                                  alt="Fashion"
                                  className="carousel-img"
                                />
                              </a>
                              <Button
                                size="sm"
                                className="fav-button"
                                onClick={() => addToFavorites(img)}
                              >
                                +Fav
                              </Button>
                            </div>
                          ))}
                        </div>
                      )}
                    </CardContent>
                  </Card>
                </motion.div>
              ))}
            </div>
            <div className="chat-input">
              <Input
                placeholder="Ask about styles, outfits..."
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => e.key === "Enter" && sendMessage()}
              />
              <Button onClick={sendMessage}>Send</Button>
            </div>
          </>
        )}
      </main>
    </div>
  );
};

export default ChatInterface;
