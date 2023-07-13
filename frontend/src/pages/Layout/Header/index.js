import React, {useState, useEffect} from "react";
import { useNavigate } from "react-router-dom";
import {Link} from 'react-router-dom';

export default function Header({logged, fono}){
    const navigate = useNavigate();

    function logout(){
        localStorage.clear();
        navigate('/');
    }

    return (
        <>
            <nav className="navbar navbar-expand-lg bg-body-tertiary">
                <div className="container-fluid">
                    <Link className="navbar-brand" to='/'>ASR</Link>
                    
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    
                    <div className="collapse navbar-collapse" id="navbarNav">
                        <ul className="navbar-nav">
                            {
                                logged && (
                                    <li className="nav-item">
                                        <Link className="nav-link active" to='/home'>Home</Link>
                                    </li>
                                )
                            }

                            {
                                fono && (
                                    <li className="nav-item">
                                        <Link className="nav-link active" to='/admin'>Relatórios</Link>
                                    </li>
                                )
                            }

                            {
                                logged && (
                                    <li className="nav-item">
                                        <button className="nav-link active" onClick={e => logout()}>Sair</button>
                                    </li>
                                )
                            }
                        </ul>
                    </div>
                </div>
            </nav>
        </>
    );
}