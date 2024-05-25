import React from 'react';
import ReactDOM from 'react-dom';
import myImage from './assets/my-image.png'; // パスを明示的に変更
import './index.css';

function App() {
  return (
    <div>
      <h1>Hello World</h1>
      <img src={myImage} alt="My Image" />
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
