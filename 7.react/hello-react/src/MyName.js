import React from 'react';

const MyName = ({ name = '홍길동' }) => {
    return (
        <div>
            안녕하세요 제 이름은 <b>{name}</b> 입니다.
        </div>
    )
}

export default MyName;