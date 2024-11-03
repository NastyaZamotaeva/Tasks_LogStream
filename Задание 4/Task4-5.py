#Реализуйте итератор колоды карт (52 штуки без джокеров) 
#CardDeck. Каждая карта представлена в виде строки типа «2 Пик».
#При вызове функции next() будет представлена следующая карта.
#По окончании перебора всех элементов возникнет ошибка StopIteration.



class CardDeck:
    type = ['Пик', 'Треф', 'Бубен', 'Червей']  
    num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']  

    def __init__(self):
        self.cards = []
        for type in self.type:
            for num in self.num:
                self.cards.append(f"{num} {type}")
                
        self.i = 0  
    def __iter__(self):
        return self 

    def __next__(self):
        if self.i < len(self.cards):
            card = self.cards[self.i]  
            self.i += 1  
            return card
        else:
            raise StopIteration  

deck = CardDeck()

for card in deck:
    print(card)
