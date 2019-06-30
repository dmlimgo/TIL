import React from 'react'
import { ItemTypes } from './Constants'
import { useDrag, DragPreviewImage } from 'react-dnd'
import logo from './logo4.png'

console.log('Knightjs 실행')

export default function Knight() {
    const [{isDragging}, drag, preview] = useDrag({
        item: { type: ItemTypes.KNIGHT },
            collect: monitor => ({
                isDragging: !!monitor.isDragging(),
            }),
        })
    const knightImage = logo

    return (
        <>
            <DragPreviewImage connect={preview} src={knightImage} />
            <div
                ref={drag}
                style={{
                    opacity: isDragging ? 0.5 : 1,
                    fontSize: 60,
                    fontWeight: 'bold',
                    cursor: 'move',
                }}
            >
                ♘
            </div>
        </>
    )
}
    
