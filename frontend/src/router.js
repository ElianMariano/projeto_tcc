import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Layout from './pages/Layout';
import Login from './pages/Login';
import Home from './pages/Home';
import CrudAccount from './pages/CrudAccount';
import CrudLevel from './pages/CrudLevel';
import CrudQuestion from './pages/CrudQuestion';

export default function Router(){
    return (
        <BrowserRouter>
            <Routes>
                <Route element={<Layout/>} path='/'>
                    <Route element={<Login/>} index/>
                    <Route element={<Home/>} path='/home'/>
                    <Route element={<CrudAccount/>} path='/criar-conta'/>
                    <Route element={<CrudLevel/>} path='/criar-nivel'/>
                    <Route element={<CrudQuestion/>} path='/criar-pergunta'/>
                </Route>
            </Routes>
        </BrowserRouter>
    );
}