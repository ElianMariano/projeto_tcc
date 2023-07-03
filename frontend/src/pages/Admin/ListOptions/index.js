import React, { useState, useEffect } from 'react';
import {Link} from 'react-router-dom';
import api from '../../../services/api';

export default function ListOptions(){
    const [levels, setLevels] = useState([]);
    const [options, setOptions] = useState([]);

    useEffect(() => {
        api.get('/level').then(res => {
            setLevels(res.data['success']);
        })
        .catch(err => {
            alert(err);
        })
    }, []);

    function onChange(){
        api.get('/option').then(res => {
            console.log(res.data);
            setOptions(res.data['success']);
        })
        .catch(err => {
            alert(err);
        });
    }

    return (
        <div classname="container-md mx-auto mt-2">
            <h1 className="mb-3">Escolha o nível: </h1>

            <Link to='/criar-opcao'><button type="button" class="btn btn-success mb-3">Criar opção para pergunta</button></Link>

            <select className="form-select" aria-label="Default select example" defaultValue={'empty'} onChange={e => onChange()}>
                <option value='empty' selected>Selecione o nível</option>
                {
                    levels.map(level => (
                        <option key={`q${level.id}`} value={level.id} selected>{`Nivel ${level.id}`}</option>
                    ))
                }
            </select>

            {
                options.map(option => (
                    <Link to={`/criar-opcao/${option.id}`} className='row'><button type="button" class="btn btn-primary m-2">{`Opção ${option.id}: ${option.texto}`}</button></Link>
                ))
            }
        </div>
    )
}