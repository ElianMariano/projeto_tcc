import React, {useState, useEffect} from 'react';
import {useNavigate, useParams} from 'react-router-dom';
import api from '../../../services/api';

export default function CrudLevel(){
    const navigate = useNavigate();
    const {id} = useParams();
    const [dificuldade, setDificuldade] = useState({});
    const [level, setLevel] = useState({});
    const [points, setPoints] = useState(0);

    useEffect(() => {
        if (id !== undefined && id !== null){
            api.get(`/level/${id}`).then(res => {
                setLevel(res.data['success']);
            })
            .catch(err => {
                alert(err);
            });
        }
    }, [])

    function onDelete(){
        api.delete(`level/${id}`).then(res => {
            navigate('/listar-niveis');
        })
        .catch(err => {
            alert(err);
        });
    }

    function submit(){
        if (dificuldade !== 'Fácil' && dificuldade !== 'Normal' && dificuldade !== 'Difícil'){
            alert('Selecione uma dificuldade');
            return;
        }

        if (id !== undefined && id !== null){
            api.put(`/level/${id}`, {
                points: level.points,
                difficulty: dificuldade
            }).then(res => {
                navigate('/listar-niveis');
            })
            .catch(err => {
                alert(err);
            });
            return;
        }

        api.post('/level', {
            points: points,
            difficulty: dificuldade
        }).then(res => {
            navigate('/listar-niveis');
        })
        .catch(err => {
            alert(err);
        });
    }

    return (
        <>
            <div className='container-sm mx-auto mt-2'>
                {(id !== undefined && id !== null) && <button type="button" class="btn btn-danger mb-3" onClick={e => onDelete()}>Excluir</button>}

                <div className="mb-3">
                    <label htmlFor="text" className="form-label">Pontos</label>
                    <input type="number" className="form-control" placeholder="" id='text' value={points} onChange={e => setPoints(e.target.value)}/>
                </div>

                <select className="form-select" aria-label="Default select example" onChange={e => setDificuldade(e.target.value)} value={id !== undefined && id !== null ? level.dificuldade : ''}>
                    <option selected>Selecione a dificuldade</option>
                    <option value="Fácil">Fácil</option>
                    <option value="Normal">Normal</option>
                    <option value="Difícil">Difícil</option>
                </select>

                <button type='button' className='btn btn-primary mt-3' onClick={e => submit()}>{id !== undefined && id !== null ? 'Atualizar' : 'Criar'} nível</button>
            </div>
        </>
    );
}