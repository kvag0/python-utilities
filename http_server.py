import socket

# Define o endereço do servidor (localhost) e uma porta
HOST = '127.0.0.1'
PORT = 8888

# Cria o objeto socket do servidor usando o protocolo TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Esta opção permite que o endereço seja reutilizado imediatamente após o servidor fechar
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Associa o nosso socket ao endereço e porta definidos
server_socket.bind((HOST, PORT))

# Coloca o servidor em modo de escuta, pronto para aceitar conexões
server_socket.listen(1)

print(f"✅ Servidor simples a escutar em http://{HOST}:{PORT}")
print("Pressione Ctrl+C para fechar o servidor.")

# Loop infinito para o servidor ficar sempre a correr e a aceitar novas conexões
while True:
    try:
        # Pausa a execução e espera por uma conexão de um cliente (ex: um navegador)
        # Quando um cliente se conecta, ele retorna um novo socket para essa conversa específica
        # e o endereço do cliente.
        client_connection, client_address = server_socket.accept()
        print(f"\nNova conexão de {client_address}")

        # Lê os dados enviados pelo cliente (o pedido HTTP cru)
        request_data = client_connection.recv(1024).decode('utf-8')

        # Imprime o pedido cru no terminal para podermos ver como ele é
        print("--- Pedido HTTP Recebido ---")
        print(request_data)
        print("--------------------------")

        # Analisa a primeira linha para descobrir o caminho (path) pedido
        first_line = request_data.split('\n')[0]
        path = first_line.split()[1] if len(first_line.split()) > 1 else '/'

        # Define uma resposta com base no caminho
        if path == '/':
            response_body = "<h1>Página Principal</h1><p>Bem-vindo ao nosso servidor HTTP raiz!</p>"
            status_line = "HTTP/1.1 200 OK"
        elif path == '/sobre':
            response_body = "<h1>Página Sobre</h1><p>Este servidor foi construído com a biblioteca de sockets do Python.</p>"
        else:
            response_body = "<h1>Erro 404</h1><p>Página não encontrada.</p>"
            status_line = "HTTP/1.1 404 Not Found"

        # Monta a resposta HTTP completa
        # É crucial ter uma linha em branco entre os cabeçalhos e o corpo!
        http_response = f"""{status_line}
Content-Type: text/html; charset=utf-8
Content-Length: {len(response_body.encode('utf-8'))}

{response_body}"""

        # Envia a resposta HTTP de volta para o cliente (codificada em bytes)
        client_connection.sendall(http_response.encode('utf-8'))

        # Fecha a conexão com este cliente específico
        client_connection.close()

    except KeyboardInterrupt:
        # Permite-nos fechar o servidor de forma limpa com Ctrl+C
        print("\n👋 A fechar o servidor... Adeus!")
        break

# Fecha o socket principal do servidor
server_socket.close()
