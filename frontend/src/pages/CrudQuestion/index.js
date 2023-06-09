import React from 'react';

export default function CrudQuestion(){
    return (
        <>
            <div className='container-sm mx-auto mt-2'>
                <div className="mb-3">
                    <label for="text" className="form-label">Texto</label>
                    <input type="label" className="form-control" placeholder="seunome@email.com" id='text'/>
                </div>

                <select className="form-select" aria-label="Default select example">
                    <option selected>Selecione o nível</option>
                    <option value="1">Nível 1</option>
                    <option value="2">Nível 2</option>
                    <option value="3">Nível 3</option>
                </select>

                <section>
                    <div className="mb-3">
                        <label for="optiontext" className="form-label">Texto</label>
                        <input type="label" className="form-control" placeholder="seunome@email.com" id='optiontext'/>
                    </div>

                    <div className="form-check">
                        <input className="form-check-input" type="checkbox" value="" id="right"/>
                        <label className="form-check-label" for="right">
                            É a opção correta
                        </label>
                    </div>
                    
                    <div className="input-group mb-3 mt-3">
                        <label className="input-group-text" for="inputGroupFile01">Upload</label>
                        <input type="file" className="form-control" id="inputGroupFile01"/>
                    </div>
                </section>

                <button type='button' className='btn btn-primary'>Criar Pergunta</button>
            </div>
        </>
    );
}