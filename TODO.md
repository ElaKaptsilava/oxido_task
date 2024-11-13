Twoim zadaniem jest stworzenie prostej aplikacji w Pythonie lub JavaScript (do wyboru), która:

1. Łączy się z API OpenAI;
2. Odczytuje plik tekstowy z artykułem – tu znajdziesz plik do pobrania;
3. Treść artykułu wraz z promptem przekazuje do OpenAI w celu obróbki (opisane poniżej);
4. Zapisuje otrzymany od OpenAI kod w pliku artykul.html.
   Kod artykułu wygenerowany przez AI powinien spełniać następujące wytyczne:
   • Użycie odpowiednich tagów HTML do strukturyzacji treści.
   • Określenie wspólnie z AI miejsc, gdzie warto wstawić grafiki – oznaczamy je 
   z użyciem
   tagu <img> z atrybutem src="image_placeholder.jpg". Dodaj atrybut alt do
   każdego obrazka z dokładnym promptem, który możemy użyć do wygenerowania grafiki.
   Umieść podpisy pod grafikami używając odpowiedniego tagu HTML.
   • Brak kodu CSS ani JavaScript. Zwrócony kod powinien zawierać wyłącznie zawartość do
   wstawienia pomiędzy tagami <body> i </body>. Nie dołączaj znaczników <html>, <head> ani <body>.
Wygenerowany kod HTML zapisz w pliku artykul.html – naturalnie nie będzie on
walidowalny bez nagłówków HTML czy sekcji <head>, ale to nie szkodzi.
Cały kod aplikacji, przykładowy artykuł i wygenerowany plik artykul.html wrzuć do
repozytorium. Więcej informacji w sekcji „Jak odesłać zadanie?”.