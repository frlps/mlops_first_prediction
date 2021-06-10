#Versão slim de uma imagem de container do Python 3.7
FROM python:3.7-slim 

#Variáveis de ambiente (muito vulnerável)
#ENV BASIC_AUTH_USERNAME=usuario
#ENV BASIC_AUTH_PASSWORD=senha

#Variáveis de ambiente (bom) roda na execução do DockeFile
ARG USERNAME_ARG
ARG PASSWORD_ARG

ENV BASIC_AUTH_USERNAME=${USERNAME_ARG}
ENV BASIC_AUTH_PASSWORD=${PASSWORD_ARG}
#ENV PORT=5001

#Copiando arquivos
COPY ./requirements.txt /usr/requirements.txt

#Diretório de trabalho
WORKDIR /usr

#Comandos iniciais
#RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

#Copiando mais pastas
COPY ./src /usr/src
COPY ./models /usr/models 

#Start
ENTRYPOINT [ "python3" ]
#ENTRYPOINT [ "gunicorn" ]

#Complemento
CMD [ "src/app/main.py" ]
#CMD [ "-b :$PORT  main:app" ]

#Using the port
#EXPOSE $PORT


