import React from 'react';
import ReactDOM from 'react-dom';

const element = React.createElement(
    'div',
    { classname: 'greeting' },
    'Hello',
    React.createElement('div', {}, 'test!!!'),
    'world!',
);

const element1 = <div className="divClass"> Hello <div> мир </div>! </div>;

ReactDOM.render(
    element1,
    document.getElementById('root')
);