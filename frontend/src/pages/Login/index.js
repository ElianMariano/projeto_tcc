import React from 'react';
import {Link} from 'react-router-dom';

export default function Login(){
    return (
        <>
            <div className='container-sm mx-auto mt-2'>
                <div className="mb-3">
                    <label for="email" className="form-label">Email</label>
                    <input type="email" className="form-control" placeholder="seunome@email.com" id='email'/>
                </div>

                <div className="mb-3">
                    <label for="password" className="form-label">Senha</label>
                    <input type="password" className="form-control" placeholder="Senha" id='password'/>
                </div>

                <div className='d-grid gap-2'>
                    <button type='button' className='btn btn-primary row'>Login</button>
                    <Link to='/criar-conta' className='row'><button type='button' className='btn btn-secondary'>Criar conta</button></Link>
                </div>
                {/* <button type='button' className='btn btn-link'>Esqueceu a senha?</button> */}
            </div>
        </>
    );
}