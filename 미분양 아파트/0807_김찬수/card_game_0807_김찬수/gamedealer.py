from card import Card
from player import plat
import random

class GameDealer:
    def __init__(self, players):
        self.__deck=[];
        self.__players =players

    def make_deck(self):
        card_suits = ["♠", "♥", "♣", "◆"]
        card_numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for suit in card_suits:
            for num in card_numbers:
                self.__deck.append(Card(suit, num))  # Card 클래스의 생성자 호출

    def shuffle_deck(self):
        random.shuffle(self.__deck)

    def send_cards(self,send_size=10):
        for player in self.__players:
            for i in range(send_size):
                card = self.__deck.pop()
                player.add_card(card)

    def print_cards(self):
        print("[GameDealer] 딜러가 가진 카드 수: %d"%len(self.__deck))
        count=0
        if(len(self.__deck)==0):
            return
        while True:
            print(self.__deck[count],sep=" ",end =" ")

            count+=1
            if(count%13==0):
                print()
            if(count==len(self.__deck)):
                break

        print()
