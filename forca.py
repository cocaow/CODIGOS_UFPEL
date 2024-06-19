import os

def read_secret_word(file_path):
    if not os.path.exists(file_path):
        print(f"O arquivo {file_path} não foi encontrado.")
        return None
    try:
        with open(file_path, 'r') as file:
            return file.readline().strip()
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None

def display_progress(secret_word, guessed_letters):
    display = ''
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    file_path = 'word.txt'
    print(f"Tentando ler a palavra secreta do arquivo: {file_path}")
    
    secret_word = read_secret_word(file_path)
    
    if not secret_word:
        print("Falha ao obter a palavra secreta.")
        return

    guessed_letters = set()
    attempts_remaining = 6
    correct_guesses = set()

    print("Bem-vindo ao Jogo da Forca!")
    
    while attempts_remaining > 0:
        print(f"\nPalavra: {display_progress(secret_word, guessed_letters)}")
        print(f"Tentativas restantes: {attempts_remaining}")
        print(f"Letras tentadas: {' '.join(sorted(guessed_letters))}")

        guess = input("Adivinhe uma letra: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Por favor, digite uma única letra.")
            continue

        if guess in guessed_letters:
            print("Você já tentou essa letra.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            correct_guesses.add(guess)
            print("Correto!")
        else:
            attempts_remaining -= 1
            print("Errado!")

        if set(secret_word) == correct_guesses:
            print(f"\nParabéns! Você adivinhou a palavra: {secret_word}")
            break
    else:
        print(f"\nVocê perdeu! A palavra era: {secret_word}")

if __name__ == "__main__":
    hangman()
