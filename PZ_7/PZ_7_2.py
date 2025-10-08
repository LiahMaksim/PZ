#Дана строка-предложение на русском языке. Подсчитать количество содержащихся в строке знаков препинания.

def count_punctuation_marks(text):
    punctuation_marks = {'.', ',', ';', ':', '!', '?', '-', '—', '(', ')', '"', '«', '»', '…'}
    count = 0
    for char in text:
        if char in punctuation_marks:
            count += 1
    return count
print("Вывод")
russian_sentences = [
    "Привет, как дела? Все хорошо!",
    "Он сказал: «Я приду завтра...» и ушел.",
    "Мама мыла раму; папа читал газету.",
    "В лесу стояла тишина - только птицы пели.",
    "Это (конечно) очень интересно!"
]
for sentence in russian_sentences:
    result = count_punctuation_marks(sentence)
    print(f"Предложение: '{sentence}'")
    print(f"Количество знаков препинания: {result}\n")