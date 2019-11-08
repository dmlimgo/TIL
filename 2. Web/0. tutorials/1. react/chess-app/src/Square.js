import React from 'react'

console.log('Squarejs 실행')

export default function Square({black, children}) {
    const fill = black ? 'black':'white'
    const stroke = black ? 'white':'black'

    return (
        <div
            style={{
                backgroundColor: fill,
                color: stroke,
                width: '100%',
                height: '100%',
                textAlign: 'center',
            }}
        >
            {children}
        </div>
    ) 
}