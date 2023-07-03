import React, {useState, useEffect} from "react";
import { useNavigate, useParams } from "react-router-dom";
import api from '../../../services/api';

export default function CrudOption(){
    const navigate = useNavigate();
    const {id} = useParams();

    const [questions, setQuestions] = useState([]);
    const [question, setQuestion] = useState(0);
    const [text, setText] = useState('');
    const [right, setRight] = useState(false);
    const [file, setFile] = useState({});

    const [option, setOption] = useState({});

    useEffect(() => {
        if (id !== undefined && id !== null){
            api.get(`/option/${id}`).then(res => {
                setOption(res.data['success']);
                setText(res.data['success']['texto']);
                setRight(res.data['success']['correta']);
                setQuestion(res.data['success']['pergunta_id']);
            })
            .catch(err => {
                alert(err);
            });
        }

        api.get('questions').then(res => {
            setQuestions(res.data['success']);
        })
        .catch(err => {
            alert(err);
        })
    }, []);

    function handleSubmit(e){
        e.preventDefault();

        const data = questions.filter(e => e.id == question);
        if (data.length == 0){
            alert('Selecione uma pergunta');
            return;
        }

        if (file == {}){
            alert('Selecione um arquivo');
            return;
        }

        if (text == ''){
            alert('Escreva um texto');
            return;
        }

        if (id !== undefined && id !== null){
            api.put(`/option/${id}`, {
                text: text,
                right: right,
            })
            .then(res => {
                navigate('/listar-opcoes');
            })
            .catch(err => {
                alert(err);
            })
            return;
        }

        let formData = new FormData();
        formData.append('text', text);
        formData.append('right', right);
        formData.append('file', file);
        formData.append('pergunta_id', question);
    
        const config = {     
            headers: { 'content-type': 'multipart/form-data' }
        }
        
        api.post("/option", formData, config)
        .then (res => {
            navigate('/listar-opcoes');
        })
        .catch(err => {
            alert(err);
        });
    }

    function onDelete(){
        api.delete(`/option/${id}`)
        .then(res => {
            navigate('/listar-opcoes');
        })
        .catch(err => {
            alert(err);
        })
    }

    return <>
            <div className='container-sm mx-auto mt-2'>
                {(id !== undefined && id !== null) && <button type="button" class="btn btn-danger mb-3" onClick={e => onDelete()}>Excluir</button>}
                <div className="mb-3">
                    <label htmlFor="text" className="form-label">Texto</label>
                    <input type="label" className="form-control" placeholder="" id='text' value={text} onChange={e => setText(e.target.value)}/>
                </div>

                <select className="form-select" aria-label="Default select example" value={question} onChange={e => setQuestion(e.target.value)}>
                    <option value={0} selected>Selecione a pergunta</option>
                    {
                        questions.map(question => (
                            <option key={`q${question.id}`} value={question.id} selected>{`Pergunta ${question.id}: ${question.texto}`}</option>
                        ))
                    }
                </select>

                <section>
                    <div className="form-check mt-2">
                        <input className="form-check-input" type="checkbox" value={right} id="right" onChange={e => setRight(e.target.checked)}/>
                        <label className="form-check-label" htmlFor="right">
                            É a opção correta
                        </label>
                    </div>
                    
                    {
                        (id === undefined || id === null) &&
                        <div className="input-group mb-3 mt-3">
                            <label className="input-group-text" htmlFor="inputGroupFile01">Upload</label>
                            <input type="file" className="form-control" id="inputGroupFile01" onChange={e => setFile(e.target.files[0])}/>
                        </div>
                    }
                </section>

                <button type='button' className='btn btn-primary mt-3' onClick={e => handleSubmit(e)}>{id !== undefined && id !== null ? 'Atualizar' : 'Criar'} Opção</button>
            </div>
        </>;
}