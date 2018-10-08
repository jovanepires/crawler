## Crawler

O teste consiste em acessar uma página que contém um formulário, com um botão que retorna uma resposta ao ser clicado pelo usuário. 

Ao utilizar a tecnica de simular o acesso via código, precisamos considerar alguns critérios: 

* A página possui validação de CSRF
* A página de resposta valida o token, precisamos enviar o mesmo token retornado no primeiro acesso (GET).
* Para funcionar, os acessos realizados precisam estar em um mesmo contexto, ou seja, na mesma sessão de usuário.

## Dependências

* Python 3.7.0
* Pip 10.0.1

** Recomendo a utilização um ```virtualenv``` 
https://virtualenv.pypa.io/en/stable/

## Configuração

```$ pip install -r requirements.txt```


## Execução

```$ python test.py```

Irá iniciar uma thread com intervalo de 0.1s, exibindo a resposta da ação simulada pelo script.