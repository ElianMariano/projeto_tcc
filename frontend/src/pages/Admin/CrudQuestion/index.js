import React, {useState, useEffect} from 'react';
import {useParams, useNavigate} from 'react-router-dom';
import api from '../../../services/api';

export default function CrudQuestion(){
    const [levels, setLevels] = useState([]);
    const [question, setQuestion] = useState({});
    const [level, setLevel] = useState(0);
    const [text, setText] = useState('');
    const navigate = useNavigate();
    const {id} = useParams();

    useEffect(() => {
        api.get('/level').then(res => {
            setLevels(res.data['success']);
        })
        .catch(err => {
            alert(err);
        });

        if (id !== undefined && id !== null){
            api.get(`/questions/${id}`).then(res => {
                setQuestion(res.data['success']);
                setText(res.data['success']['texto']);
                setLevel(res.data['success']['nivel_id']);
            })
            .catch(err => {
                alert(err);
            });
        }
    }, []);

    function submit(e){
        e.preventDefault();

        const data = levels.filter(e => e.id == level);
        if (data.length == 0){
            alert('Selecione um nível');
            return;
        }

        if (text == ''){
            alert('Escreva um texto');
            return;
        }

        if (id !== undefined && id !== null){
            api.post(`/questions/${id}`, {
                text: text,
                level_id: data[0].id
            })
            .then(res => {
                navigate('/listar-perguntas');
            })
            .catch(err => {
                alert(err);
            });
            return;
        }

        api.post('/questions', {
            text: text,
            level_id: data[0].id
        })
        .then(res => {
            navigate('/listar-perguntas');
        })
        .catch(err => {
            alert(err);
        });
    }

    function onDelete(){

    }

    return (
        <>
            <div className='container-sm mx-auto mt-2'>
                {
                   (id !== undefined && id !== null) && <button type="button" class="btn btn-danger mb-3" onClick={e => onDelete()}>Excluir</button>
                }

                <div className="mb-3">
                    <label for="text" className="form-label">Texto</label>
                    <input type="label" className="form-control" placeholder="" id='text' value={text} onChange={e => setText(e.target.value)}/>
                </div>

                <select className="form-select" aria-label="Default select example" value={level} onChange={e => setLevel(e.target.value)}>
                    <option value={0} selected>Selecione o nível</option>
                    {
                        levels.map(level => (
                            <option key={`q${level.id}`} value={level.id} selected>{`Nivel ${level.id}`}</option>
                        ))
                    }
                </select>

                <button type='button' className='btn btn-primary mt-3' onClick={e => submit(e)}>{id !== undefined && id !== null ? 'Atualizar' : 'Criar'} Pergunta</button>
            </div>
        </>
    );
}