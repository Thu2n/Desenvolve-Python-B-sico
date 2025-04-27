import emoji

# Lista de emojis disponíveis para uso

emoji_lista = {
    ":sorriso:": "😃",
    ":triste:": "😢",
    ":festa:": "🥳",
    ":dedao_para_cima:": "👍",
    ":coração:": "❤️",
    ":fogo:": "🔥",
}

# Exibe a lista de emojis disponíveis
print("Lista de emojis disponíveis:")
for codigo, simbolo in emoji_lista.items():
    print(f"{codigo} -> {simbolo}")

# Solicita ao usuário uma frase codificada
frase_codificada = input("\nDigite uma frase usando os códigos de emoji acima: ")

# Substitui os códigos pelos emojis correspondentes
frase_emojizada = emoji.emojize(frase_codificada, language="alias")

# Exibe a frase convertida
print(f"\nSua frase com emojis: {frase_emojizada}")