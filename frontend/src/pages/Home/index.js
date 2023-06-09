import React from 'react';
import CardLevel from './components/CardLevel';
import './styles.scss';

export default function Home(){
    return (
        <>
            <h1>Home</h1>

            <div className='container-sm'>
                <CardLevel/>

                <CardLevel/>

                <CardLevel/>

                <CardLevel/>

                <CardLevel/>

                <CardLevel/>
            </div>
        </>
    );
}