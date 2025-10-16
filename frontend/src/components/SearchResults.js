import React, { useState } from 'react';

const SearchResults = ({ results }) => {
  const [selectedHtml, setSelectedHtml] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleViewHtml = (htmlContent) => {
    setSelectedHtml(htmlContent);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setSelectedHtml(null);
  };

  const formatHtml = (html) => {
    if (!html) return '';
    
    let formatted = html
      .replace(/>\s*</g, '>\n<')
      .replace(/(<\/[^>]+>)/g, '$1\n')
      .replace(/(<[^/>][^>]*>)/g, '$1');
    
    let indentLevel = 0;
    const lines = formatted.split('\n');
    const formattedLines = lines.map(line => {
      line = line.trim();
      if (!line) return '';
      
      if (line.startsWith('</')) {
        indentLevel--;
      }
      
      const indentedLine = '  '.repeat(Math.max(0, indentLevel)) + line;
      
      if (line.startsWith('<') && !line.startsWith('</') && !line.endsWith('/>') && !line.includes('</')) {
        indentLevel++;
      }
      
      return indentedLine;
    });
    
    return formattedLines.filter(line => line).join('\n');
  };

  return (
    <div className="search-results">
      <h2>Search Results</h2>
      <div className="results-list">
        {results.map((result, index) => (
          <div key={index} className="result-card">
            <div className="result-header">
              <div className="result-content">
                <div 
                  dangerouslySetInnerHTML={{ 
                    __html: result.content
                  }} 
                />
              </div>
              <span className="match-score">{result.match_score}% match</span>
            </div>
            <div className="result-footer">
              <span className="path">Path: {result.path}</span>
              <button 
                className="view-html-btn"
                onClick={() => handleViewHtml(result.html_content)}
              >
                View HTML
              </button>
            </div>
          </div>
        ))}
      </div>

      {isModalOpen && (
        <div className="modal">
          <div className="modal-content">
            <div className="modal-header">
              <h3>HTML Source Code</h3>
              <button className="close-btn" onClick={closeModal}>
                Close
              </button>
            </div>
            <pre className="html-content">
              <code>{selectedHtml ? formatHtml(selectedHtml) : 'No HTML content available'}</code>
            </pre>
          </div>
        </div>
      )}
    </div>
  );
};

export default SearchResults;