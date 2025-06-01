# Uno 

class Card():
    '''
    管理卡牌資訊
    >>> 第1~25張：玩家被發到的牌
    >>> 第26張：top_card
    >>> 之後的牌：抽牌堆
    '''
    def __init__(self, value, color=None):
        self.value = value
        self.color = color

    def __repr__(self): 
        color_code = {"red": 31, "yellow": 33, "green": 32, "blue": 36}
        ansi_code = color_code.get(self.color, 0)
        return f"\033[{ansi_code}m{self.value}\033[0m"
    
    def is_playable(self, top_card): # 傳入 top_card 以檢查可不可以出牌
        return (
            self.color == top_card.color or 
            self.value == top_card.value or 
            self.value in ["wild", "+4"] 
        )

class NumberCard(Card):
    def __init__(self, color, value):
        assert value.isdigit(), "NumberCard must have numeric value" 
        super().__init__(value, color)

class SkipCard(Card):
    def __init__(self, color):
        super().__init__("skip", color)

class ReverseCard(Card):
    def __init__(self, color):
        super().__init__("reverse", color)

class Draw2Card(Card):
    def __init__(self, color):
        super().__init__("+2", color)

class WildCard(Card):
    def __init__(self):
        super().__init__("wild", None)

class WildDraw4Card(Card):
    def __init__(self):
        super().__init__("+4", None)

def parse_card(card_str):
    if card_str == "wild":
        return WildCard()
    elif card_str == "+4":
        return WildDraw4Card()
    elif "-" in card_str:
        value, color = card_str.split("-")
        if value.isdigit():
            return NumberCard(color, value)
        elif value == "skip":
            return SkipCard(color)
        elif value == "reverse":
            return ReverseCard(color)
        elif value == "+2":
            return Draw2Card(color)
    # raise ValueError(f"Invalid card format: {card_str}")

class Player():
    '''管理每個玩家的牌、出牌策略'''
    def __init__(self):
        self.cards = list()
    
    def is_done(self): # 檢查是否已經沒牌
        return len(self.cards) == 0

    def add_card(self, card: Card):  # 加進手牌
        self.cards.append(card)

    def play(self, top_card: Card):
        # Rules for playing a card
        playable_cards = [card for card in self.cards if card.is_playable(top_card)] 
        # 先把手上可以打的牌都整理出來
        # print(f"playable cards:{playable_cards}")
        if not playable_cards: # 沒牌出 要抽牌
            return None
        
        def get_prior(card):
            if card.value.isdigit():
                return 0
            elif card.value == "skip":
                return 1
            elif card.value == "reverse":
                return 2
            elif card.value == "+2":
                return 3
            elif card.value == "wild":
                return 4
            elif card.value == "+4":
                return 5
            return 6

        priorities = [get_prior(card) for card in playable_cards]
        min_priority = min(priorities)

        # 按照手牌順序找出第一張具有最小 priority 的牌
        for card in self.cards:
            if card in playable_cards and get_prior(card) == min_priority:
                self.cards.remove(card)
                selected_card = card
                break

        # 出萬用卡後要選擇一個新顏色
        if selected_card.value in ["wild", "+4"]:
            color_count = {"red": 0, "yellow": 0, "green": 0, "blue": 0}
            for c in self.cards:
                if c.color:  # 如果 color 不是 None 的話
                    color_count[c.color] += 1

            if all(v == 0 for v in color_count.values()):
                # 沒有任何彩色牌 → 預設選紅色
                selected_card.color = "red"
            else:
                max_count = max(color_count.values())
                candidate_colors = [color for color, count in color_count.items() if count == max_count]
                for color in ["red", "yellow", "green", "blue"]:
                    if color in candidate_colors:
                        selected_card.color = color
                        break

        return selected_card

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)


class Game():
    def __init__(self, deck_strings, num_player: int = 5, num_init_cards: int = 5):
        self.deck = [parse_card(line.strip()) for line in deck_strings if line.strip() != 'q']
        self.num_player = num_player
        self.num_init_cards = num_init_cards
        self.players = [Player() for _ in range(num_player)]
        self.turn = 0
        self.direction = 1 # 順時針
        self.game_over = False
        self._init_game()

    def _init_game(self):
        # Operations to initialize the game
        for _ in range(self.num_init_cards):  # 每一輪發一張
            for player_idx in range(self.num_player):  # 順序給每位玩家
                if self.deck:
                    card = self.draw_card()
                    if card:
                        self.players[player_idx].add_card(card)
                else:
                    # 如果牌堆在發牌時就用完，提早跳出
                    break
            else:
                continue  # 只有當內層沒 break 才會跑這個 continue，繼續下一輪發牌
            break  # 如果有 break（表示沒牌了），則跳出整個發牌階段

        self.top_card = self.draw_card()
        if self.top_card:
            if self.top_card.color is None:
                self.top_card.color = "red"
            self.apply_card_effect(self.top_card)

    def draw_card(self):
        return self.deck.pop(0) if self.deck else None
    
    def get_next_turn(self):
        return (self.turn + self.direction) % self.num_player
    
    def apply_card_effect(self, played_card):
        if played_card.value == "reverse":
            self.direction *= -1
            if self.num_player == 2:
                self.turn = (self.turn + 2 * self.direction) % self.num_player
            else:
                self.turn = self.get_next_turn()
            return True  # 結束當前 step

        elif played_card.value == "+2":
            draw_idx = self.get_next_turn()
            for _ in range(2):
                card = self.draw_card()
                if card:
                    self.players[draw_idx].add_card(card)
            self.turn = self.get_next_turn()
            return True

        elif played_card.value == "+4":
            draw_idx = self.get_next_turn()
            for _ in range(4):
                card = self.draw_card()
                if card:
                    self.players[draw_idx].add_card(card)
            self.turn = self.get_next_turn()
            return True

        elif played_card.value == "skip":
            self.turn = (self.turn + 2 * self.direction) % self.num_player
            return True

        return False  # 沒有觸發效果
    
    def step(self):
        player = self.players[self.turn]
        played_card = player.play(self.top_card)

        # 無牌可出且牌堆為空，直接跳過
        if played_card is None and not self.deck:
            self.turn = self.get_next_turn()
            return

        # 無牌可出，嘗試抽牌
        if played_card is None:
            if self.deck:
                new_card = self.draw_card()

                if new_card.is_playable(self.top_card):
                    played_card = new_card  # 直接打出該牌
                    # wild 或 +4 要補色
                    if played_card.value in ["wild", "+4"]:
                        color_count = {"red": 0, "yellow": 0, "green": 0, "blue": 0}
                        for c in player.cards:
                            if c.color:
                                color_count[c.color] += 1
                        if all(v == 0 for v in color_count.values()):
                            played_card.color = "red"
                        else:
                            max_count = max(color_count.values())
                            candidate_colors = [color for color, count in color_count.items() if count == max_count]
                            for color in ["red", "yellow", "green", "blue"]:
                                if color in candidate_colors:
                                    played_card.color = color
                                    break
                    self.top_card = played_card

                    if self.apply_card_effect(played_card):
                        if player.is_done():
                            self.game_over = True
                            print(f"Player {self.turn} win!")
                        return
                else:
                    player.add_card(new_card)
                    self.turn = self.get_next_turn()
                    return
            else:
                self.turn = self.get_next_turn()
                return

        # 玩家已出完手牌
        if player.is_done():
            # print(self)
            print(f"Player {self.turn} win!") 
            self.game_over = True
            return
        
        if played_card is not None:
            self.top_card = played_card
            if self.apply_card_effect(played_card):
                if player.is_done():
                    print(f"Player {self.turn} win!") 
                    self.game_over = True
                return

        # 若無特殊效果影響，正常輪到下一位
        self.turn = self.get_next_turn()
        # print(self)

    def get_final_winner(self):
        # Find the final winner of the game
        for i, player in enumerate(self.players):
            if player.is_done():
                return i
        return None

    def __str__(self):
        player_str_list = []
        for i, player in enumerate(self.players):
            marker = "  <- next" if i == self.turn else ""
            player_str_list.append(f"Player {i}: {player}{marker}")

        players_str = "\n".join(player_str_list)
        game_str = f"""{"=" * 10}

Top Card: {self.top_card}

Players:
{players_str}
{"=" * 10}"""
    
        return game_str

def main():
    import sys
    deck_input = sys.stdin.read().splitlines()  # 從輸入讀取資料（結尾包含 q）
    game = Game(deck_input)

    while not game.game_over:
        game.step()

if __name__ == "__main__":
    main()