import React, { useState } from 'react';
import './App.css';

function App() {
  const [quote, setQuote] = useState("Get Quote");

  
  const handleGetQuote = async () => {
    try {
      
      const response = await fetch('/api/quote'); 
      
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      setQuote(data.quote); 
    } catch (error) {
      console.error("Error fetching quote:", error);
      setQuote("Oops! Could not fetch a quote.");
    }
  };

  return (
    <div className="App" style={{ textAlign: 'center', marginTop: '50px' }}>
      
      <h1>Quote of the Day</h1>

      
      <button 
        onClick={handleGetQuote} 
        style={{ padding: '10px 20px', fontSize: '16px', cursor: 'pointer' }}
      >
        Get Quote
      </button>

      {/* The Text Box */}
      <div style={{
        marginTop: '20px',
        borderRadius: '8px',
        padding: '20px',
        display: 'block',
        margin: '20px auto',
        maxWidth: '500px',
        minHeight: '50px',
        backgroundColor: '#f9f9f9'
      }}>
        {quote}
      </div>
    </div>
  );
}

export default App;