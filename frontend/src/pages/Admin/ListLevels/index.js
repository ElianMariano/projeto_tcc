import React, {useState, useEffect} from "react";
import {Link} from 'react-router-dom';
import api from "../../../services/api";

export default function ListLevels(){
    const [levels, setLevels] = useState([]);

    useEffect(() => {
        api.get('level').then(res => {
            setLevels(res.data['success']);
        })
        .catch(err => {
            alert(err);
        })
    }, [])

    return (
        <div classname="container-md mx-auto mt-2">
            <h1 className="mb-3">Escolha o nível: </h1>

            <Link to='/criar-nivel'><button type="button" class="btn btn-success">Criar nível</button></Link>

            {
                levels.map(level => (
                    <Link to={`/criar-nivel/${level.id}`} className="row"><button type="button" class="btn btn-primary m-2">{`Nível ${level.id}`}</button></Link>
                ))
            }
        </div>
    )
}