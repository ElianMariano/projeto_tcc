import React from 'react';

export default function CrudLevel(){
    return (
        <>
            <div className='container-sm mx-auto mt-2'>
                <div className="mb-3">
                    <label for="points" className="form-label">Pontos</label>
                    <input type="label" className="form-control" placeholder="0" id='points'/>
                </div>

                <select className="form-select" aria-label="Default select example">
                    <option selected>Selecione a dificuldade</option>
                    <option value="1">Fácil</option>
                    <option value="2">Normal</option>
                    <option value="3">Difícil</option>
                </select>

                <button type='button' className='btn btn-primary mt-3'>Criar nível</button>
            </div>
        </>
    );
}