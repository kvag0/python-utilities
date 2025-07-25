# 1. Importar a biblioteca que acabámos de instalar
import qrcode
import os

# 2. Função principal do nosso programa
def generate_qr_code():
    print("--- Gerador de QR Code ---")
    # Pedir os dados ao utilizador através do terminal
    data = input("➡️  Digite o texto ou URL para gerar o QR Code: ")
    file_name = input("➡️  Digite o nome do ficheiro para salvar a imagem (ex: meu_site.png): ")

    # Validar se o nome do ficheiro termina com .png
    if not file_name.endswith('.png'):
        file_name += '.png'

    try:
        # 3. Criar e configurar o objeto QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # 4. Adicionar os dados do utilizador ao objeto
        qr.add_data(data)
        qr.make(fit=True)

        # 5. Criar a imagem a partir do objeto QR Code
        img = qr.make_image(fill_color="black", back_color="white")

        # 6. Salvar a imagem no ficheiro especificado
        img.save(file_name)

        # Obter o caminho completo do ficheiro para mostrar uma mensagem útil
        full_path = os.path.abspath(file_name)
        print(f"\n✅ QR Code gerado com sucesso!")
        print(f"✅ Imagem salva em: {full_path}")

    except Exception as e:
        print(f"\n❌ Ocorreu um erro: {e}")

# 7. Ponto de entrada do script: Executa a função principal
if __name__ == '__main__':
    generate_qr_code()
