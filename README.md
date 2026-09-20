# 💧 Consumo de Água

Sistema desenvolvido em **Python** para classificar o consumo de água de um imóvel de acordo com seu tipo e consumo mensal em metros cúbicos (m³).

## 🎯 Objetivo

O objetivo do sistema é receber o **tipo de imóvel** e o **consumo de água**, realizando uma classificação conforme regras de negócio previamente definidas.

O sistema identifica as seguintes situações:

* 🏢 **Imóvel comercial:** aplica a mensagem referente à tarifa comercial.
* 🏠 **Apartamento com consumo inferior a 10 m³:** consumo econômico.
* 🏠 **Apartamento ou casa com consumo de até 25 m³:** consumo moderado.
* ⚠️ **Demais situações:** consumo excessivo.


## 🛠️ Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-181717?logo=github\&logoColor=white)


* **Python** — linguagem utilizada no desenvolvimento.
* **GitHub** — versionamento e armazenamento do projeto.
* **Match/Case** — estrutura utilizada para implementar as regras de classificação.
* **Try/Except** — tratamento de entradas inválidas.


## 📋 Requisitos

Para executar o projeto, é necessário ter instalado:

* Python **3.10 ou superior**
* Git, caso o projeto seja clonado do GitHub

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/mateusmartinssantos/consumo-agua-py.git
```

### 2. Acesse a pasta do projeto

```bash
cd consumo-agua
```

### 3. Execute o programa

```bash
python app.py
```



## 💻 Exemplo de execução

```text
Digite o tipo de imóvel (casa, apartamento ou comercial): apartamento
Digite o consumo de água em m³: 8

Consumo econômico – excelente controle de água!
```

## 📌 Regras de negócio

| Tipo de imóvel |         Consumo | Classificação     |
| -------------- | --------------: | ----------------- |
| Comercial      |  Qualquer valor | Tarifa comercial  |
| Apartamento    |         < 10 m³ | Consumo econômico |
| Apartamento    |      10 a 25 m³ | Consumo moderado  |
| Casa           |       Até 25 m³ | Consumo moderado  |
| Outros casos   | Acima do limite | Consumo excessivo |

## 📚 Conceitos utilizados

O projeto foi desenvolvido com conceitos básicos de programação, incluindo:

* Entrada de dados com `input()`
* Conversão de tipos com `float()`
* Estruturas condicionais
* `match/case`
* Condições com `if` dentro do `case`



---

**Projeto desenvolvido para fins acadêmicos e de aprendizado em Python.**
