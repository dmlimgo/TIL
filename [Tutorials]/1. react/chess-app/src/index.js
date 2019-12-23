import React from 'react';
import ReactDOM from 'react-dom';
import Board from './Board';
import { observe } from './Game';
import './index.css'
// import { SSL_OP_SSLEAY_080_CLIENT_DH_BUG } from 'constants';
// import { createStore, applyMiddleware, compose } from 'redux'

// import { Provider } from 'react-redux'
// import thunk from 'redux-thunk'
// import { reduxFirestore, getFirestore } from 'redux-firestore'
// import { reactReduxFirebase, getFirebase } from 'react-redux-firebase'
// import fbConfig from './config/fbConfig'

// const store = createStore(rootReducer, 
//     compose(
//         applyMiddleware(thunk.withExtraArgument({ getFirebase, getFirestore })),
//         reduxFirestore(),
//         reactReduxFirebase()
//     )
// );

const root = document.getElementById('root')

observe(knightPosition =>
    ReactDOM.render(<Board knightPosition={knightPosition} />, root),
)
