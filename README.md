Siga os passos abaixo para configurar e rodar o projeto:

### 1. Clone o repositório

Utilize o Git para clonar o repositório para sua máquina local. Execute o seguinte comando no terminal:

```bash
git clone https://github.com/David0102/todo-list.git
```

### 2. Entre na pasta do projeto:

```bash
cd todo-list
```

### 3. Crie um ambiente virtual:

```bash
python -m venv venv
```

### 4. Ative o ambiente virtual:

<li>Windows
  
```bash
venv\Scripts\activate

```
<li>Linux
  
```bash
source venv/bin/activate
```

### 5. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 6. Faça as migrações:

```bash
python manage.py migrate
```

### 7. Inicie o servidor:

```bash
python manage.py runserver

```


