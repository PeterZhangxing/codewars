import random


class MyCard(object):

    def __init__(self,suit_id,rank_id):
        self.suit_id,self.suit = self.get_suit_info(suit_id)
        self.rank_id,self.rank,self.value = self.get_rank_info(rank_id)
        self.short_name,self.long_name = self.get_card_name()

    def get_suit_info(self,suit_id):
        if suit_id == 1:
            suit = "Diamonds"
        elif suit_id == 2:
            suit = "Hearts"
        elif suit_id == 3:
            suit = "Spades"
        elif suit_id == 4:
            suit = "Clubs"
        else:
            suit = "ErrorSuit"

        return suit_id,suit

    def get_rank_info(self,rank_id):
        if rank_id == 1:
            rank = "Ace"
            value = 1
        elif rank_id == 11:
            rank = "Jack"
            value = 10
        elif rank_id == 12:
            rank = "Queen"
            value = 10
        elif rank_id == 13:
            rank = "King"
            value = 10
        elif 2 <= rank_id <= 10:
            rank = str(rank_id)
            value = rank_id
        else:
            rank = "ErrorRank"
            value = -1

        return rank_id,rank,value

    def get_card_name(self):
        if self.rank == "10":
            short_name = self.rank + self.suit[0]
        else:
            short_name = self.rank[0] + self.suit[0]
        long_name = self.rank + " of " + self.suit

        return short_name,long_name

    def __str__(self):
        return self.short_name


class MyPoke(object):

    def __init__(self):
        self.poke = self.creat_a_poke()
        self.cards_total_num = len(self.poke)

    @property
    def left_cards_num(self):
        return len(self.poke)

    def creat_a_poke(self):
        poke_li = []
        for suit_id in range(1,5):
            for rank_id in range(1,14):
                new_card = MyCard(suit_id, rank_id)
                if rank_id == 8:
                    new_card.value = 50
                poke_li.append(new_card)

        return poke_li

    def get_random_card(self,num):
        rcards = []
        for i in range(num):
            card = random.choice(self.poke)
            rcards.append(card)
            self.poke.remove(card)

        return rcards


class MyPokeGame(object):
    confirm_choice = ['y','yes']
    deny_choice = ['n','no']
    p_total = 0
    c_total = 0

    def __init__(self):
        self.mypoke = MyPoke()
        self.deck = self.mypoke.poke

        self.p_cards = self.mypoke.get_random_card(5)
        # print(self.mypoke.left_cards_num)
        self.c_cards = self.mypoke.get_random_card(5)
        # print(self.mypoke.left_cards_num)

        # self.p_total = 0
        # self.c_total = 0

        self.up_card = self.mypoke.get_random_card(1)[0]
        self.active_suit = self.up_card.suit

        self.blocked = 0

    def show_p_cards(self):
        print('\nYour hand: ',end='')
        for card in self.p_cards:
            print(card,end=' ')
        print(' Up card: %s  Active suit: %s'%(self.up_card,self.active_suit))

    def show_c_cards(self):
        print('\nComputer hand: ',end='')
        for card in self.c_cards:
            print(card,end=' ')
        print(' Up card: %s  Active suit: %s'%(self.up_card,self.active_suit))

    def is_presponse_valid(self,response):
        action = ''
        if response.lower() == 'draw':
            # 取一张牌
            if self.mypoke.left_cards_num >= 1:
                drawcard = self.mypoke.get_random_card(1)[0]
                action = 'draw'
            else:
                self.blocked += 1
                drawcard = ''
            return drawcard,action
        else:
            if response.upper() in [ card.short_name for card in self.p_cards ]:
                action = 'give'
                for card in self.p_cards:
                    if response.upper() == card.short_name:
                        return card,action
            else:
                return response.upper(), action

    def get_new_suit(self):
        while True:
            suit = input("Pick a suit: ")
            if suit.lower() == 'd':
                self.active_suit = "Diamonds"
                break
            elif suit.lower() == 's':
                self.active_suit = "Spades"
                break
            elif suit.lower() == 'h':
                self.active_suit = "Hearts"
                break
            elif suit.lower() == 'c':
                self.active_suit = "Clubs"
                break
            else:
                print('Not a valid suit,please try again(d/s/h/c):')
        print("You picked", self.active_suit)

    def player_turn(self):
        while True:
            self.show_p_cards()
            response = input("Type a card to play or 'Draw' to take a card: ")

            card, action = self.is_presponse_valid(response)
            if action == 'draw':
                if card:
                    self.p_cards.append(card)
                    print("You got a new card %s"%card.short_name)
                break
            elif action == 'give':
                self.p_cards.remove(card)
                self.up_card = card
                if card.short_name.startswith('8'):
                    self.get_new_suit()
                else:
                    self.active_suit = card.suit
                break
            else:
                print("Not a valid option please choose again:")

    def computer_turn(self):
        # 如果计算机有可以出的牌，就出分数最大的牌
        all_options = [] # 所有可以出的牌
        options_exclude_8 = [] # 没有8的可出的牌
        options_with_8 = [] # 可以出的8

        for card in self.c_cards:
            if card.suit == self.active_suit or card.rank == self.up_card.rank:
                all_options.append(card)
            elif card.short_name.startswith('8'):
                all_options.append(card)

        for card in all_options:
            if not card.short_name.startswith('8'):
                options_exclude_8.append(card)
            else:
                options_with_8.append(card)

        if len(all_options) > 0: # 计算机有牌可以出
            if len(options_exclude_8) > 0:
                best_card = options_exclude_8[0]
                max_value = best_card.value
                for card in options_exclude_8:
                    if card.value > max_value:
                        max_value = card.value
                        best_card = card
                # best_card = max(options,key=lambda card:card.value)

                self.c_cards.remove(best_card)
                self.up_card = best_card
                self.active_suit = self.up_card.suit
                print(" Computer played ", best_card.short_name)
                self.show_c_cards()

            elif len(options_with_8) > 0:
                best_card = options_with_8[0]
                self.c_cards.remove(best_card)
                self.up_card = best_card

                # suit_dict = {'diamonds':0, 'hearts':0, 'spades':0, 'clubs':0}
                suit_dict = {}
                for card in self.c_cards:
                    suit_dict.setdefault(card.suit,1)
                    suit_dict[card.suit] += 1
                max_suit = max(suit_dict,key=lambda suit:suit_dict[suit])
                self.active_suit = max_suit
                print(" Computer changed suit to ", self.active_suit)
                self.show_c_cards()

        else: # 计算机无牌可出,尝试取牌
            if self.mypoke.left_cards_num > 0:
                next_card = self.mypoke.get_random_card(1)[0]
                self.c_cards.append(next_card)
                print(" Computer drew a card")
                self.show_c_cards()
            else:
                print(" Computer is blocked")
                self.blocked += 1
                print("Computer has %s cards left" % (len(self.c_cards)))
                self.show_c_cards()


    def get_score(self,flag):
        # 如果是玩家获胜
        total_score = 0
        if flag == 'person':
            for card in self.c_cards:
                total_score += card.value
        else:
            for card in self.p_cards:
                total_score += card.value

        return total_score

    def run_game(self):
        is_programme_over = False
        is_game_over = False

        while not is_programme_over:
            if len(self.c_cards) == 0 or len(self.p_cards) == 0 or self.blocked >=2:
                del self.mypoke
                self.__init__()
                print("="*100)

            while not is_game_over:
                # 玩家还有牌, 玩家出牌，显示状态信息
                self.player_turn()
                if len(self.p_cards) == 0: # 玩家获胜，游戏结束
                    # 结束本轮游戏循环
                    is_game_over = True
                    # 打印玩家的分数
                    p_score = self.get_score(flag='person')
                    self.p_total += p_score
                    print("You won! You got %s points for computer's hand" %p_score)

                if not is_game_over:
                    # 计算机出牌
                    self.computer_turn()

                    if len(self.c_cards) == 0: # 计算机获胜，游戏结束
                        is_game_over = True
                        # 打印计算机的分数
                        c_score = self.get_score(flag='computer')
                        self.c_total += c_score
                        print("You lost,computer win! Computer got %s points for your hand" % c_score)

                    if self.blocked >= 2: # 如果已经没有牌了，但是玩家都没出完牌
                        is_game_over = True
                        print('Both players blocked. GAME OVER.')

                        c_score = self.get_score(flag='computer')
                        p_score = self.get_score(flag='person')

                        self.c_total += c_score
                        self.p_total += p_score

                        print("You got %i points for computer's hand" % p_score)
                        print("Computer got %i points for your hand" % c_score)

            user_choice = input("Do you want to play again?(y/n)").strip().lower()
            if user_choice in self.confirm_choice:
                is_programme_over = False
                is_game_over = False
            elif user_choice in self.deny_choice:
                is_programme_over = True
                print("\n Final Score:")
                print("You: %i Computer: %i" % (self.p_total, self.c_total))
            else:
                print('invalid choice %s'%user_choice)
                continue

if __name__ == '__main__':

    # poke = MyPoke()
    # for card in poke.poke:
    #     print(card.long_name)
    # p_cards = poke.get_random_card(5)
    # print(poke.left_cards_num)
    # c_cards = poke.get_random_card(5)
    # print(poke.left_cards_num)

    # mygame = MyPokeGame()
    # mygame.show_c_cards()
    # mygame.show_p_cards()
    # if '8' in [card.short_name[0] for card in mygame.p_cards]:
    #     print('in')

    mygame = MyPokeGame()
    mygame.run_game()