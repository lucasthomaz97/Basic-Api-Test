# Basic API Consistency Test

[🇧🇷 Português](#Português) | [🇺🇸 English](#English)

## English

A simple project created when I was a junior QA to demonstrate API testing through code to manual QAs who didn't know how to program.

Created to be a first step into test automation for other QAs. Written in a simple way so anyone could understand the logic behind API testing.

> **Disclaimer:** The API on which the tests were originally performed has been changed or discontinued. Because of this, it was necessary to modify the original code, and newer versions of Python and the required packages are also being used.

### What does this project do?

It makes requests to the Zelda API and validates that the returned data is consistent. Checks if the `name` field contains the expected value.

### How to run

```bash
# Install dependencies
uv sync

# Run the tests
uv run pytest
```

### Understanding the code

| Part | What it does |
|------|--------------|
| `make_request()` | Makes an HTTP GET request to the API and returns the response |
| `test_validate_return()` | The main test. Validates that the data returned matches what was requested |
| `@pytest.mark.parametrize` | Allows running the same test with different data (games, staff) |

---

## Português

Um projeto simples que criei quando era QA junior para demonstrar testes de API via código para QAs especializados em testes manuais que não sabiam programar.

Criado para ser um primeiro passo na área de automação de testes para outros QAs. Escrito de forma simples para que qualquer pessoa pudesse entender a lógica por trás dos testes de API.

> **Aviso:** A API em que o teste foi originalmente feito foi alterada ou descontinuada. Por isso, foi necessário alterar o código original, e também estão sendo usadas versões mais atuais do Python e dos pacotes requeridos.

### O que este projeto faz?

Ele faz requisições para a API do Zelda e valida que os dados retornados são consistentes. Verifica se o campo `name` contém o valor esperado.

### Como executar

```bash
# Instalar dependências
uv sync

# Rodar os testes
uv run pytest
```

### Entendendo o código

| Parte | O que faz |
|-------|-----------|
| `make_request()` | Faz uma requisição HTTP GET para a API e retorna a resposta |
| `test_validate_return()` | O teste principal. Valida que os dados retornados correspondem ao que foi solicitado |
| `@pytest.mark.parametrize` | Permite executar o mesmo teste com dados diferentes (games, staff) |