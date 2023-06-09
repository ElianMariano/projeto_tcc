import React from 'react';

export default function CrudAccount(){
    return (
        <>
            <div className='container-sm mx-auto mt-2'>
                <div className="mb-3">
                    <label for="name" className="form-label">Nome</label>
                    <input type="label" className="form-control" placeholder="seunome@email.com" id='name'/>
                </div>

                <div className="mb-3">
                    <label for="birth" className="form-label">Nascimento</label>
                    <input type="date" className="form-control" placeholder="seunome@email.com" id='birth'/>
                </div>

                <div className="mb-3">
                    <label for="cpf" className="form-label">CPF</label>
                    <input type="label" className="form-control" placeholder="seunome@email.com" id='cpf'/>
                </div>

                <div className="mb-3">
                    <label for="email" className="form-label">Email</label>
                    <input type="email" className="form-control" placeholder="seunome@email.com" id='email'/>
                </div>

                <div className="mb-3">
                    <label for="password" className="form-label">Senha</label>
                    <input type="password" className="form-control" placeholder="Senha" id='password'/>
                </div>

                <div className="mb-3">
                    <label for="cpassword" className="form-label">Confirmar senha</label>
                    <input type="password" className="form-control" placeholder="Senha" id='cpassword'/>
                </div>

                <button type='button' className='btn btn-primary'>Criar conta</button>
            </div>
        </>
    );
}