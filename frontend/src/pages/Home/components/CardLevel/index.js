import Game from '../../../../assets/game.svg';
import '../../../../bootstrap.scss';
import './styles.scss';

export default function CardLevel(){
    return (
        <div className='card-level-container'>
            <div className='card-body'>
                <div>
                    <h4 className='fw-normal text-red'>Nome do nivel</h4>

                    <h5 className='subtitle text-sm text-muted mb-0'>0 pontos</h5>
                </div>

                <img src={Game} alt="Icone controle" />
            </div>

            <div className='card-footer'>
                <p>Terminado</p>
            </div>
        </div>
    );
}