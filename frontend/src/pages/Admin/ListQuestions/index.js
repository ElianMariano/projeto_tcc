import React, {useState, useEffect} from "react";
import {Link} from 'react-router-dom';
import api from "../../../services/api";

export default function ListQuestion(){
    const [levels, setLevels] = useState([]);
    const [questions, setQuestions] = useState([]);

    useEffect(() => {
        api.get('/level').then(res => {
            setLevels(res.data['success']);
        })
        .catch(err => {
            alert(err);
        });
    }, []);

    async function onChange(value){
        api.get('/questions').then(res => {
            setQuestions(res.data['success']);
        })
        .catch(err => {
            alert(err);
        });
    }

    return (
        <div classname="container-md mx-auto mt-2">
            <h1 className="mb-3">Escolha as perguntas: </h1>

            <Link to='/criar-pergunta'><button type="button" class="btn btn-success mb-3">Criar pergunta</button></Link>

            <select className="form-select" aria-label="Default select example" defaultValue={'empty'} onChange={(e) => onChange(e.target.value)}>
                <option value='empty' selected>Selecione o nível</option>
                {
                    levels.map(level => (
                        <option key={`q${level.id}`} value={level.id} selected>{`Nivel ${level.id}`}</option>
                    ))
                }
            </select>

            {questions.map(question => (
                <Link to={`/criar-pergunta/${question.id}`} className="row"><button type="button" class="btn btn-primary m-2">{`Pergunta ${question.id}: ${question.texto}`}</button></Link>
            ))}
        </div>
    );
}