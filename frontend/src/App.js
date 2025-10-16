import React, { useState } from 'react';
import axios from 'axios';
import SearchForm from './components/SearchForm';
import SearchResults from './components/SearchResults';
import LoadingSpinner from './components/LoadingSpinner';
import './App.css';

// Use environment variable for API URL, fallback to localhost for development
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

function App() {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSearch = async (url, query) => {
    setLoading(true);
    setError('');
    setResults([]);

    try {
      const response = await axios.post(`${API_BASE_URL}/search`, {
        url,
        query
      });
      setResults(response.data.results);
    } catch (err) {
      setError(err.response?.data?.detail || 'An error occurred while searching');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <div className="container">
        <header className="app-header">
          <h1>Website Content Search</h1>
          <p>Search through website content with precision</p>
        </header>

        <div className="card">
          <SearchForm onSearch={handleSearch} />
        </div>

        {error && (
          <div className="alert alert-error">
            {error}
          </div>
        )}

        {loading && <LoadingSpinner />}

        {results.length > 0 && (
          <SearchResults results={results} />
        )}
      </div>
    </div>
  );
}

export default App;
