FROM gcc:8
WORKDIR /app/
COPY program.c ./
RUN gcc program.c -o program
RUN chmod +x program
