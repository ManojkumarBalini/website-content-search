import React, { useState } from 'react';

const SearchForm = ({ onSearch }) => {
  const [url, setUrl] = useState('');
  const [query, setQuery] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (url && query) {
      onSearch(url, query);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="form-group">
        <label htmlFor="url">Website URL</label>
        <input
          type="url"
          id="url"
          className="form-control"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="https://example.com"
          required
        />
      </div>
      
      <div className="form-group">
        <label htmlFor="query">Search Query</label>
        <input
          type="text"
          id="query"
          className="form-control"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Enter your search query"
          required
        />
      </div>
      
      <button type="submit" className="btn">
        Search
      </button>
    </form>
  );
};

export default SearchForm;