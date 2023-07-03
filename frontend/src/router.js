import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Layout from './pages/Layout';
import Login from './pages/Login';
import Home from './pages/Home';
import CrudAccount from './pages/CrudAccount';
import CrudLevel from './pages/Admin/CrudLevel';
import CrudQuestion from './pages/Admin/CrudQuestion';
import CrudOption from './pages/Admin/CrudOption';
import ListLevels from './pages/Admin/ListLevels';
import ListQuestions from './pages/Admin/ListQuestions';
import ListOptions from './pages/Admin/ListOptions';
import Admin from './pages/Admin';
import AnswerQuestion from './pages/AnswerQuestion';
import Report from './pages/Report';

export default function Router(){
    return (
        <BrowserRouter>
            <Routes>
                <Route element={<Layout/>} path='/'>
                    <Route element={<Login/>} index/>
                    <Route element={<Home/>} path='/home'/>
                    <Route element={<CrudAccount/>} path='/criar-conta'/>
                    <Route element={<Admin/>} path='/admin'/>
                    <Route element={<CrudLevel/>} path='/criar-nivel/:id?'/>
                    <Route element={<CrudQuestion/>} path='/criar-pergunta/:id?'/>
                    <Route element={<CrudOption/>} path='/criar-opcao/:id?'/>
                    <Route element={<ListLevels/>} path='/listar-niveis'/>
                    <Route element={<ListQuestions/>} path='/listar-perguntas'/>
                    <Route element={<ListOptions/>} path='/listar-opcoes'/>
                    <Route element={<AnswerQuestion/>} path='/responder-perguntas/:id'/>
                    <Route element={<Report/>} path='/relatorio'/>
                </Route>
            </Routes>
        </BrowserRouter>
    );
}