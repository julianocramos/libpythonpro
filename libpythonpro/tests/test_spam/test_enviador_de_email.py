import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente  ',
    ['juliano_nj@hotmail.com', 'foo@bar.com.br']
)
def test_remente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'ju.ramos_7@gmail.com',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'juliano']
)
def test_remente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'ju.ramos_7@gmail.com',
            'Cursos Python Pro',
            'Primeira turma Guido Von Rossum aberta'
        )
