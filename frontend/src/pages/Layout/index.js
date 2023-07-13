import React from 'react';
import Header from './Header';
import { Outlet } from 'react-router-dom'

export default function Layout({logged, fono}){
    return (
        <>
            <Header logged={logged} fono={fono}/>

            <Outlet/>
        </>
    );
}