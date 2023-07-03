import React, {useState, useEffect} from 'react';
import { useParams } from 'react-router-dom';
import api from '../../services/api';

export default function AnswerQuestion(){
    const [level, setLevel] = useState();
    const {id} = useParams();

    useEffect(() => {
        api.get(`/level-all/${id}`).then(res => {
            console.log(res.data['success']);
            setLevel(res.data['success']);
        })
        .catch(err => {
            alert(err);
        });
    }, []);

    function submit(){
        // api.post()
    }

    return (
        <>
            <div className='container-sm mx-auto mt-2'>
                {
                    (level != undefined && level != null) && level.perguntas.map(pergunta => (
                        <div>
                            <h3>Pergunta {pergunta.id}</h3>

                            <section>
                                {pergunta.opcoes.map(opcao => (
                                    <div className="form-check mt-2">
                                        <input className="form-check-input" type="checkbox"/>
                                        <label className="form-check-label" htmlFor="right">
                                            {opcao.texto}
                                        </label>
                                    </div>
                                ))}
                            </section>
                        </div>
                    ))
                }

                <button type='button' className='btn btn-primary mt-3'>Responder</button>
            </div>
        </>
    );
}