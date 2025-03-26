import { useEffect, useState } from "react";
import { AppBar, Toolbar, Typography, Container, Paper, Grid, Card, CardMedia, CardContent, Button } from "@mui/material";
import { useLocation } from "react-router-dom";
import "./FourthPage.css"; // Import the CSS file
import staticImage from "./resources/img/25473.png";
import ReactMarkdown from 'react-markdown';

export default function FourthPage() {
  const location = useLocation();
  const [preferredProducts, setPreferredProducts] = useState([]);
  const [reason, setReason] = useState("");
  const [selectedProduct, setSelectedProduct] = useState(null);

  useEffect(() => {
    if (location.state && location.state.preferredProducts) {
      setPreferredProducts(location.state.preferredProducts.response);
      setReason(location.state.preferredProducts.reason);
    }
  }, [location.state]);

  const handleSelect = (product) => {
    alert(`Thank you for selecting ${product.productName}`);
  };

  const handleDelete = (product) => {
    setPreferredProducts(preferredProducts.filter(p => p !== product));
    setSelectedProduct(null);
  };

  return (
    <div>
      <div className="navbar">DLTA Recommendation System</div>

      <Container maxWidth="lg" style={{ marginTop: "20px" }}>
        <Typography variant="h4" style={{ marginBottom: "20px", textAlign: "center" }}>
          Preferred Products
        </Typography>
        <Grid container spacing={4}>
          {preferredProducts.map((product, index) => (
            <Grid item key={index} xs={12} sm={6} md={4}>
              <Card className="card" onClick={() => setSelectedProduct(product)}>
                <CardMedia
                  component="img"
                  height="140"
                  image={staticImage}
                  alt={product.productName}
                  className="card-media"
                />
                <CardContent className="card-content">
                  <Typography variant="h6">{product.productName}</Typography>
                </CardContent>

                <div className="action-buttons">
                  <Button variant="contained" color="primary" onClick={() => handleSelect(product)}>
                    Select
                  </Button>
                  <Button variant="contained" color="secondary" onClick={() => handleDelete(product)}>
                    Delete
                  </Button>
                </div>
              </Card>
            </Grid>
          ))}
        </Grid>
      </Container>
      <div className="reason-section">
          <h2 className="reason-header">Reason for Preferred Products:</h2>
        <div className="reason-content">
          <ReactMarkdown >{reason}</ReactMarkdown>
          </div>
        </div>
    </div>
  );
}