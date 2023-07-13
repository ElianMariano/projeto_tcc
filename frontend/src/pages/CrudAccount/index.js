import React, {useState, useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../../services/api';

export default function CrudAccount(){
    const navigate = useNavigate();

    const [name, setName] = useState('');
    const [birth, setBirth] = useState('');
    const [address, setAddress] = useState('');
    const [cpf, setCpf] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [rpassword, setRpassword] = useState('');
    const [paciente, setPaciente] = useState(false);

    const [fonos, setFonos] = useState([]);
    const [fono, setFono] = useState(0);

    useEffect(() => {
        api.get('/fono').then(res => {
            setFonos(res.data['success']);
        })
        .catch(err => {
            alert(err);
        })
    }, [])

    function submit(e){
        e.preventDefault();
        if (name === '' || birth === '' || cpf === '' || email === '' || password === '' || rpassword === '' || address === ''){
            alert('Preencha todos os dados');
            return;
        }

        if (password !== rpassword){
            alert('As senhas devem ser iguais');
            return;
        }

        const data = fonos.filter(e => e.id === fono);
        if (data.length === 0 && paciente){
            alert('Selecione um fonoaudiólogo');
            return;
        }

        if (paciente){
            api.post('/pacient', {
                name,
                birth,
                password,
                address,
                email,
                fono_id: fono
            })
            .then(res => {
                navigate('/');
            })
            .catch(err => {
                alert(err);
            });
        }
        else{
            api.post('/fono', {
                name,
                birth,
                password,
                cpf,
                email,
                address
            })
            .then(res => {
                navigate('/');
            })
            .catch(err => {
                alert(err);
            });
        }
    }

    return (
        <>
            <div className='container-sm mx-auto mt-2'>
                <h1>Cadastro</h1>

                <div className="mb-3">
                    <label for="name" className="form-label">Nome</label>
                    <input type="label" className="form-control" placeholder="" id='name' value={name} onChange={e => setName(e.target.value)}/>
                </div>

                <div className="mb-3">
                    <label for="birth" className="form-label">Nascimento</label>
                    <input type="date" className="form-control" placeholder="" id='birth' value={birth} onChange={e => setBirth(e.target.value)}/>
                </div>

                <div className="mb-3">
                    <label for="name" className="form-label">Endereço</label>
                    <input type="label" className="form-control" placeholder="" id='name' value={address} onChange={e => setAddress(e.target.value)}/>
                </div>

                {
                    !paciente && (
                        <div className="mb-3">
                            <label for="cpf" className="form-label">CPF</label>
                            <input type="label" className="form-control" placeholder="" id='cpf' value={cpf} onChange={e => setCpf(e.target.value)}/>
                        </div>
                    )
                }

                <div className="mb-3">
                    <label for="email" className="form-label">Email</label>
                    <input type="email" className="form-control" placeholder="seunome@email.com" id='email' value={email} onChange={e => setEmail(e.target.value)}/>
                </div>

                <div className="form-check mt-2">
                    <input className="form-check-input" type="checkbox" value={paciente} id="right" onChange={e => setPaciente(e.target.checked)}/>
                    <label className="form-check-label" htmlFor="right">
                        É paciente?
                    </label>
                </div>

                {
                    (fonos.length > 0 && paciente) && (
                        <select className="form-select" aria-label="Default select example" value={fono} onChange={e => setFono(e.target.value)}>
                            <option value={0} selected>Selecione um fono</option>
                            {
                                fonos.map(fono => (
                                    <option key={`q${fono.id}`} value={fono.id} selected>{`Fono ${fono.id}: ${fono.name}`}</option>
                                ))
                            }
                        </select>
                    )
                }

                <div className="mb-3">
                    <label for="password" className="form-label">Senha</label>
                    <input type="password" className="form-control" placeholder="Senha" id='password' value={password} onChange={e => setPassword(e.target.value)}/>
                </div>

                <div className="mb-3">
                    <label for="cpassword" className="form-label">Confirmar senha</label>
                    <input type="password" className="form-control" placeholder="Senha" id='cpassword' value={rpassword} onChange={e => setRpassword(e.target.value)}/>
                </div>

                <button type='button' className='btn btn-primary' onClick={e => submit(e)}>Criar conta</button>

                {(fonos.length == 0 && paciente) && (
                    <div class="alert alert-danger mt-2" role="alert">
                        Não é possível criar um paciente sem um fonoaudiólogo!
                    </div>                  
                )}
            </div>
        </>
    );
}