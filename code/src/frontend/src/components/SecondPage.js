import { useState, useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import "./SecondPage.css"; // Import the CSS file

export default function SecondPage() {
  const location = useLocation();
  const [text, setText] = useState("");
  const [customerID, setCustomerID] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    if (location.state && location.state.initialResponse) {
      setText(location.state.initialResponse.response);
    }
  }, [location.state]);

  const handleSubmit = async () => {
    if (!text.trim() || !customerID.trim()) return;

    const response = await fetch("http://localhost:6969/columnData", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ userInfo: text, customerID }),
    });

    const data = await response.json();
    console.log("Server Response:", data);

    // Navigate to third page after submission with response data
    navigate("/third", { state: { responseData: data, userSummary: location.state.initialResponse, customerID } });
  };

  return (
    <>
      <div className="navbar">DLTA Recommendation System</div>
      <div className="container">
        <div className="customer-id">
          <strong>Customer ID:</strong>
          <input
            type="text"
            value={customerID}
            onChange={(e) => setCustomerID(e.target.value)}
            className="customer-id-input"
          />
        </div>
        <div className="textarea-box">
          <h2 className="header">Here's what we understand about you:</h2> {/* Add this line */}
          <textarea
            className="textarea"
            value={text}
            onChange={(e) => setText(e.target.value)}
            rows={5}
          />
          <button
            onClick={handleSubmit}
            className="button"
          >
            Submit
          </button>
        </div>
      </div>
    </>
  );
}