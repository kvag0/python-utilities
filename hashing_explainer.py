import hashlib

def demonstrate_hashing():
    print("--- Demonstração das Propriedades do Hashing (usando SHA-256) ---\n")

    # --- Propriedade 1: Determinístico ---
    print("1. Teste de Determinismo: A mesma entrada gera sempre o mesmo hash.")
    text1 = "Ola Mundo"
    hash1 = hashlib.sha256(text1.encode('utf-8')).hexdigest()
    print(f"O hash de '{text1}' é: {hash1}")

    hash2 = hashlib.sha256(text1.encode('utf-8')).hexdigest()
    print(f"O hash de '{text1}' (de novo) é: {hash2}")
    print(f"➡️ Os hashes são iguais? {hash1 == hash2}\n")

    # --- Propriedade 2: Efeito Avalanche ---
    print("2. Teste de Efeito Avalanche: Uma pequena mudança na entrada muda drasticamente o hash.")
    text2 = "Ola Mundo." # Apenas um ponto final a mais
    hash3 = hashlib.sha256(text2.encode('utf-8')).hexdigest()
    print(f"O hash de '{text1}' é: {hash1}")
    print(f"O hash de '{text2}' é: {hash3}")
    print(f"➡️ Os hashes são iguais? {hash1 == hash3}\n")

    # --- Propriedade 3: Tamanho Fixo ---
    print("3. Teste de Tamanho Fixo: A saída tem sempre o mesmo comprimento.")
    short_text = "a"
    long_text = "Este é um texto muito, muito, muito, muito, muito, muito, muito, muito longo para ser 'hasheado'."
    short_hash = hashlib.sha256(short_text.encode('utf-8')).hexdigest()
    long_hash = hashlib.sha256(long_text.encode('utf-8')).hexdigest()
    print(f"Hash do texto curto ('{short_text}'): {short_hash} (Tamanho: {len(short_hash)})")
    print(f"Hash do texto longo: {long_hash} (Tamanho: {len(long_hash)})\n")

    # --- Propriedade 4: Mão Única ---
    print("4. Teste de Mão Única: É impossível reverter o processo.")
    print("O hash gerado foi: " + long_hash)
    print("➡️ Você consegue adivinhar o texto original a partir deste hash? Não!")
    print("    Esta é a propriedade que torna o hashing seguro para senhas.")

if __name__ == '__main__':
    demonstrate_hashing()
