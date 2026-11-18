# 📘 Assignment: Testing Code with unittest

## 🎯 Objective

Escrever testes automatizados com o módulo `unittest` da biblioteca padrão do Python para verificar se funções se comportam como esperado.

## 📝 Tasks

### 🛠️ Test a Simple Function

#### Descrição
Baixe o arquivo `starter-code.py`, renomeie-o para `starter_code.py` (nomes com hífen não podem ser importados) e crie um arquivo `test_starter.py` no mesmo diretório. Nele, crie uma classe de testes que herda de `unittest.TestCase` e escreva testes para a função `is_even()`.

#### Requisitos
O programa concluído deve:

- Importar `unittest` e a função `is_even` a partir de `starter_code`
- Conter pelo menos dois métodos de teste que usam `self.assertEqual` ou `self.assertTrue`, um para um número par e outro para um número ímpar
- Executar com `python -m unittest test_starter` e passar em todos os testes


### 🛠️ Test Error Handling

#### Descrição
Teste o comportamento da função `average()` quando ela recebe uma lista vazia. Nesse caso, a função deve lançar `ValueError`.

#### Requisitos
O programa concluído deve:

- Conter um teste que verifica se `average([])` lança `ValueError` usando `self.assertRaises`
- Conter um teste que verifica o resultado correto de `average([2, 4, 6])`, usando `self.assertEqual`
- Passar em todos os testes ao executar `python -m unittest test_starter`


### 🛠️ Test Multiple Cases with Validation

#### Descrição
Teste a função `validate_password()` com diferentes entradas, incluindo casos válidos e inválidos.

#### Requisitos
O programa concluído deve:

- Conter um teste que verifica se uma senha válida, como `"abcdef123"`, retorna `True` com `self.assertTrue`
- Conter um teste que verifica se uma senha curta, como `"abc1"`, retorna `False` com `self.assertFalse`
- Conter um teste que verifica se uma senha sem números retorna `False`
- Passar em todos os testes ao executar `python -m unittest test_starter`
