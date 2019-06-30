import React from 'react';
import ReactDOM from 'react-dom';
import Board from './Board';
import { observe } from './Game';
import './index.css'
// import { SSL_OP_SSLEAY_080_CLIENT_DH_BUG } from 'constants';

const root = document.getElementById('root')

observe(knightPosition =>
    ReactDOM.render(<Board knightPosition={knightPosition} />, root),
)
