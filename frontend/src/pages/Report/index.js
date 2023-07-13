import React, {useState, useEffect} from 'react';
import api from '../../services/api';

export default function Report(){
    const [guess, setGuess] = useState([]);
    useEffect(() => {
        api.get('/guess').then(res => {
            setGuess(res.data['success']);
        })
        .catch(err => {
            alert(err);
        })
    }, [])

    return (
        <>
            <div className='container-sm mx-auto mt-2'>
                <h1>Relatórios</h1>

                {
                    (guess.length != 0 && guess != undefined && guess != null) && guess.map(g => (
                        <h3>Paciente {g.id} fez uma tentativa no nível {g.nivel_id} e {g.correta ? 'Acertou' : 'Errou'}</h3>
                    ))
                }
            </div>
        </>
    );
}