import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./FirstPage.css"; // Import the CSS file

export default function ChatUI() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false); // New loading state
  const navigate = useNavigate();

  const handleAdd = () => {
    if (input.trim() !== "") {
      setMessages([...messages, { text: input, isUser: true }]); // Add user message with flag
      setInput("");
    }
  };

  const handleSubmit = async () => {
    if (input.trim() !== "") {
      setMessages([...messages, { text: input, isUser: true }]);
    }

    if (messages.length === 0 && input.trim() === "") return;

    setLoading(true); // Set loading to true when submit is clicked

    const response = await fetch("http://localhost:6969/gatherInfo", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ userInfo: [...messages.map(msg => msg.text), input.trim()] }),
    });

    const data = await response.json();
    console.log("Server Response:", data);

    // Simulate loading time (you can remove this later)
    setTimeout(() => {
      setLoading(false); // Set loading to false when the response is received
      navigate("/second", { state: { initialResponse: data } });
    }, 2000); // Adjust the timeout for how long you want the loading bar to show
  };

  return (
    <>
      <div className="navbar">DLTA Recommendation System</div>
      <div className="container">
        <div className="chat-box">
          <h2 className="header">Please tell us about your requirements</h2>
          <div className="message-list">
            {messages.map((msg, index) => (
              <div
                key={index}
                className={`message ${msg.isUser ? "user-message" : "system-message"}`}
              >
                {msg.text}
              </div>
            ))}
          </div>
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            className={`input-box ${input.trim() !== "" ? "input-box-filled" : ""}`}
            placeholder="Enter text..."
          />
          <div className="button-group">
            <button onClick={handleAdd} className="button button-add">
              ADD
            </button>
            <button onClick={handleSubmit} className="button button-submit">
              SUBMIT
            </button>
          </div>

          {/* Loading bar */}
          {loading && (
            <div className="loading-container">
              <div className="loading-bar"></div>
            </div>
          )}
        </div>
      </div>
    </>
  );
}
