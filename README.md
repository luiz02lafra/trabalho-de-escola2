# Hotel Quadrivago

Sistema interno de operação hoteleira, construído em Flask e SQLite.

## Recursos

- Login com senha protegida por PBKDF2.
- Perfis: Funcionário, Gerente, Administrador (Fiscal) e Dono.
- Painel com status dos quartos e ocorrências.
- Cadastro de quartos, reservas/hóspedes e ocorrências.
- Gestão da equipe exclusiva do Dono.
- Registro de ações em auditoria.
- Links inexistentes exibem uma página em branco com o layout padrão do site.

## Executar

```powershell
py -m pip install -r requirements.txt
py app.py
```

Abra `http://127.0.0.1:5000`.

## Contas de demonstração

| Perfil | E-mail |
| --- | --- |
| Dono | `dono@quadrivago.com` |
| Gerente | `gerente@quadrivago.com` |
| Administrador (Fiscal) | `fiscal@quadrivago.com` |
| Funcionário | `funcionario@quadrivago.com` |

Senha para todas as contas: `Hotel@123`.

Em produção, defina uma `SECRET_KEY` forte no ambiente e troque ou remova as contas de demonstração.


PROMPTS USADOS:

Utilizando esse código de base faça algumas alterações, como remover tudo que tenha a ver com escola, transforme em um site de hotel para os funcionários, mantendo a mesma base do site.
o nome do site e hotel será Hotel Quadrivago.
Os cargos devem ser Fúncionarios, Gerente, Administradores (serão como fiscais) e o Dono.

Substitua as guias que levam a uma pagina de erro, para uma página do site, mas uma página em branco que tenha o layout padrão, mas o conteudo que originalmente teria naquela página estará em branco.
após editar os arquivos, modifique o projeto trocando as pelas antigas páginas, mas sem mudar o que já esta completo e envie.
