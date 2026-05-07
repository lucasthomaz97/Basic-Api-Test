# Basic API Consistency Test

[🇧🇷 Português](#português) | [🇺🇸 English](#english)

---

## English

During my time as a junior QA, I presented this project at the company's QA chapter, a regular meeting where QAs share knowledge and experiences with each other. At that point in my career, I was already working with both manual and automated testing.

The audience was mostly junior QAs who came from manual testing backgrounds and had no programming experience. The goal was simple: show them that getting started with test automation doesn't have to be intimidating. No complex frameworks, no advanced concepts. Just a straightforward example of how to make an HTTP request, validate the response, and run it with pytest.

### What this project does

It makes requests to a public API and validates that the returned data is consistent, checking if the `name` field contains the expected value. This is the kind of validation you'd typically do manually in API testing, but automated.

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
| `test_validate_return()` | The main test that validates the returned data matches what was requested |
| `@pytest.mark.parametrize` | Allows running the same test with different data (games, staff) |

> **Disclaimer:** The API used in the original version of this project has been changed or discontinued, so the code was updated to work with newer versions of Python and dependencies.

---

## Português

Durante meu tempo como QA júnior, apresentei esse projeto no QA chapter da empresa, uma reunião regular onde QAs compartilham conhecimento e experiências entre si. Nessa fase da minha carreira, eu já trabalhava tanto com testes manuais quanto com testes automatizados.

O público era composto principalmente por QAs júniors que vinham de backgrounds de testes manuais e não tinham experiência com programação. O objetivo era simples: mostrar que começar na automação de testes não precisa ser intimidante. Sem frameworks complexos, sem conceitos avançados. Apenas um exemplo direto de como fazer uma requisição HTTP, validar a resposta e executar com pytest.

### O que este projeto faz

Ele faz requisições para uma API pública e valida que os dados retornados são consistentes, verificando se o campo `name` contém o valor esperado. É o tipo de validação que você normalmente faria manualmente em testes de API, mas automatizado.

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
| `test_validate_return()` | O teste principal que valida que os dados retornados correspondem ao solicitado |
| `@pytest.mark.parametrize` | Permite executar o mesmo teste com dados diferentes (games, staff) |

> **Aviso:** A API usada na versão original deste projeto foi alterada ou descontinuada, então o código foi atualizado para funcionar com versões mais recentes do Python e das dependências.