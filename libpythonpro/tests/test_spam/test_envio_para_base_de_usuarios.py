from unittest.mock import Mock

import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Juliano', email='juliano_nj@hotmail.com'),
            Usuario(nome='Luciano', email='luciano_nj@hotmail.com')
        ],
        [
            Usuario(nome='Juliano', email='juliano_nj@hotmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'juliano_nj@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Juliano', email='juliano_nj@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano_nj@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'luciano_nj@hotmail.com',
        'juliano_nj@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
