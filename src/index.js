import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

function App() {
  return (
    <div>
      <h1>Hello World</h1>
      <img src={require('./assets/my-image.png')} alt="My Image" />
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
