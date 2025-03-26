import { useEffect, useState } from "react";
import { AppBar, Toolbar, Typography, Button, Container, Paper } from "@mui/material";
import { useLocation, useNavigate } from "react-router-dom";
import "./ThirdPage.css"; // Import the CSS file

export default function ThirdPage() {
  const location = useLocation();
  const [jsonData, setJsonData] = useState({});
  const [loading, setLoading] = useState(false); // New loading state
  const navigate = useNavigate();

  useEffect(() => {
    if (location.state && location.state.responseData) {
      //if the key in responseData has underscore replace it with space
      let data = location.state.responseData;
      let newData = {};
      for (let key in data) {
        if (key !== "Loan_Purpose") {
          let newKey = key.replace(/_/g, " ");
          if (key === "Annual_Income")
            newData[newKey] = "$" + parseInt(data[key]).toLocaleString();
          else
            newData[newKey] = data[key];
        }
      }
      setJsonData(newData);
      // setJsonData(location.state.responseData);
    }
  }, [location.state]);

  const handleSubmit = async () => {
    setLoading(true); // Set loading to true when submit is clicked

    const response = await fetch("http://localhost:6969/preferedProducts", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ userInfo: jsonData, customerID: location.state.customerID, userSummary: location.state.userSummary }),
    });

    const result = await response.json();
    console.log("Server Response:", result);

    // Simulate loading time (you can remove this later)
    setTimeout(() => {
      setLoading(false); // Set loading to false when the response is received
      navigate("/fourth", { state: { preferredProducts: result } });
    }, 2000); // Adjust the timeout for how long you want the loading bar to show
  };

  return (
    <div>
      <div className="navbar">DLTA Recommendation System</div>

      <Container maxWidth="md" style={{ marginTop: "20px" }}>
        <Paper elevation={3} className="paper">
          <Typography
            variant="h2"
            className="header"
            style={{ fontWeight: 'bold', marginBottom: '30px', fontSize: '1.5rem', font: 'Varela' }}
          >
            Here is what we know about you:
          </Typography>
          <div className="key-value-pairs">
            {Object.entries(jsonData).map(([key, value], index) => (
              <div key={index} className="key-value-pair">
                <div className="key">{key}:</div>
                <div className="value">{value}</div>
              </div>
            ))}
          </div>
          <div className="button-container">
            <Button
              className="buttonsubmit"
              variant="contained"
              color="primary"
              onClick={handleSubmit}
            >
              Submit
            </Button>
          </div>
        </Paper>
      </Container>

      {/* Loading bar */}
      {loading && (
        <div className="loading-container">
          <div className="loading-bar"></div>
        </div>
      )}
    </div>
  );
}
