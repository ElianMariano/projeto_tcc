import React, {useState, useEffect} from 'react';
import CardLevel from './components/CardLevel';
import './styles.scss';
import api from '../../services/api';

export default function Home(){
    const [levels, setLevels] = useState([]);

    useEffect(() => {
        api.get('/level').then(res => {
            setLevels(res.data['success']);
        })
        .catch(err => {
            alert(err);
        })
    }, [])

    return (
        <>
            <div className='container-sm'>
                <h1 className='ml-4'>Níveis</h1>

                {levels.map(level => (
                    <CardLevel id={level.id} pontos={level.pontos} dificuldade={level.dificuldade}/>
                ))}

                {levels.length == 0 && <h3>Você não possui nenhum nível ainda.</h3>}
            </div>
        </>
    );
}