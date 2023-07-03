import React from "react";
import {Link} from 'react-router-dom';

export default function Admin(){
    return (
        <>
            <div classname="container-md mx-auto mt-2">
                <h1 className="mb-3">Escolha o que editar: </h1>

                <Link to='/listar-niveis' className="row"><button type="button" class="btn btn-primary m-2">Níveis</button></Link>
                <Link to='/listar-perguntas' className="row"><button type="button" class="btn btn-primary m-2">Perguntas</button></Link>
                <Link to='/listar-opcoes' className="row"><button type="button" class="btn btn-primary m-2">Opções para perguntas</button></Link>
            </div>
        </>
    )
}