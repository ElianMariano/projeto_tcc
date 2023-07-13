import React, {useState, useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import {Link} from 'react-router-dom';
import api from '../../services/api';

export default function Login(){
    const [email, setEmail] = useState('');
    const [senha, setSenha] = useState('');
    // const [alert, setAlert] = useState(false);

    const navigate = useNavigate();

    function onsubmit(){
        if (email == '' && senha == ''){
            alert('Por favor, preencha os dados.');
            return;
        }

        api.post('/login', {
            email,
            senha
        }).then(res => {
            const data = res.data;

            if (data.hasOwnProperty('success')){
                localStorage.setItem('user', JSON.stringify(data['success']));
                navigate('/home');
                return;
            }
            else{
                alert('Erro no login. Verifique as suas credenciais.');
            }
        })
        .catch(err => {
            alert(err);
        });
    }

    return (
        <>
            <div className='container-sm mx-auto mt-2'>
                <div className="mb-3">
                    <label for="email" className="form-label">Email</label>
                    <input type="email" className="form-control" placeholder="seunome@email.com" id='email' value={email} onChange={e => setEmail(e.target.value)}/>
                </div>

                <div className="mb-3">
                    <label for="password" className="form-label">Senha</label>
                    <input type="password" className="form-control" placeholder="Senha" id='password' value={senha} onChange={e => setSenha(e.target.value)}/>
                </div>

                <div className='d-grid gap-2'>
                    <button type='button' className='btn btn-primary row' onClick={e => onsubmit()}>Login</button>
                    <Link to='/criar-conta' className='row'><button type='button' className='btn btn-secondary'>Criar conta</button></Link>
                </div>
                {/* <button type='button' className='btn btn-link'>Esqueceu a senha?</button> */}
            </div>
        </>
    );
}