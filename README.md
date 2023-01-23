# Desafio técnico Transfeera

O primeiro passo após clonar o repositório, é  criar um ambiente virtual para rodar o nosso código, isso não é obrigatório, porém é uma boa prática e 
evita dor de cabeça com projetos futuros ao instalar as dependências direto na máquina. Para criar o ambiente virtual eu utilizei virtualenv, 
então, dentro do diretório do projeto iremos rodar:

    virtualenv <nome_do_environment>
    source nome_do_environment/bin/activate

Agora podemos instalar as dependencias do projeto, para isso existem algumas ferramentas que podem ser utilizadas, eu optei pelo pip o 
gerenciador de pacotes mais utilizado do Python, então, dentro do diretório do projeto iremos utilizar o arquivo requirements.txt com o comando:
    
    pip install -r requirements.txt

Instaladas as dependências, devemos setar as variáveis de ambiente em um arquivo .env, isso ocorre por questões de segurança, já que algumas
configurações do projeto não devem ficar expostas direto no código em produção, abaixo segue uma configuração de ambiente local para facilitar

    SECRET_KEY=django-insecure-r=-nia^sb_m@_cugtcn_ej&@ep+i3h#lh0%-zgq5!n#2$r6dsi
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost
    
Lembrando que não estou passando uma configuração de banco de dados, pois estou utilizando a configuração que cria um banco sqlite para utilização local, 
caso não exista uma configuração previa nas variáveis de ambiente. O qual, inclusive, já está dentro da pasta do projeto com os usuários pré-cadastrados. 
Caso não estivesse, o próximo passo seria rodar o comando para criar as tabelas do banco:

    python manage.py migrate
    
Porém, como já temos o banco, podemos rodar os testes com:

    python manage.py test

E finalmente subir o servidor com:

    python manage.py runserver
 
Agora o servidor já está no ar :)

Existem basicamente cinco endpoints acessiveis no projeto:

| Endpoint  | Função                |
|-----------|-----------------------|
| admin/    | Acessa o Django admin |
| receiver/ | Endpoint do Recebedor |
| account/  | Endpoint da Conta     |
| agency/   | Endpoint da Agência   |
| bank/     | Endpoint do Banco     |

Em todos os endpoints, estão habilitados os métodos `GET`, `POST`, `PUT` e `DELETE`, ao abrir a API, 
você irá notar que o Django REST framework possuí uma interface gráfica, o que facilita bastante os testes,
porém, para uma experiência melhor de usuário, é possível acessar o admin do Django com as credenciais:

| Usuário | Senha |
|---------|-------|
| admin   | admin |

Embora o django admin **não possua as mesmas validações da API** ele torna mais fácil entender como os modelos
estão organizados.