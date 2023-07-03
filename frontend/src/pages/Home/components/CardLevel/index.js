import {Link} from 'react-router-dom';
import Game from '../../../../assets/game.svg';
import '../../../../bootstrap.scss';
import './styles.scss';

export default function CardLevel(props){
    return (
        <Link to={`/responder-perguntas/${props.id}`}>
            <div className='card-level-container'>
                <div className='card-body'>
                    <div>
                        <h4 className='fw-normal text-red'>{`Nível ${props.id}`}</h4>

                        <h5 className='subtitle text-sm text-muted mb-0'>{`${props.pontos} pontos`}</h5>
                    </div>

                    <img src={Game} alt="Icone controle" />
                </div>

                <div className='card-footer'>
                    <p>{`${props.dificuldade}`}</p>
                </div>
            </div>
        </Link>
    );
}