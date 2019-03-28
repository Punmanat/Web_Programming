#####################################
### WELCOME TO YOUR OOP EXERCISE #####
#####################################

# ในแบบฝึกหัดนี้เราจะใช้ OOP ในการสร้างเกมส์ "War" ซึ่งมีวิธีเล่นดังนี้:
#
# มีผู้เล่น 2 คน ซึ่งจะได้รับไพ่ คนละ 26 ใบ (คนละครึ่งสำรับ)
# สลับไพ่ในมือ แล้ววางกองคว่ำไว้ แล้วหยิบไพ่ออกมาจากกองของตัวเองทีละ 1 ใบ สลับกันลงไพ่ (หันหน้าลง)
# ในแต่ละ Turn ผู้เล่นทั้ง 2 คน เปิดไพ่พร้อมกัน คนที่ถือไพ่ที่มีเลขสู่งกว่าจะเก็บไพ่ทั้ง 2 ใบคว่ำวางไว้ด้านล่างของกองตนเอง
# (สนใจแต่ตัวเลข ไม่สนใจดอก A > King > Queen > Jack > 10 ... > 2)
# แต่ถ้าไพ่ทั้งสองใบเป็นแต้มเท่ากัน จะถือว่าเกิด WAR ผู้เล่นแต่ละคนจั่วไพ่จากกองของตนเองมา 1 ใบ วางคว่ำลง แล้วจั่วอีก 1 ใบวางหงายหน้า
# คนที่แต้มสูงกว่าเก็บไพ่ทั้งหมดที่วางอยู่ (6 ใบ)
# ถ้าไพ่ที่เปิดมามีแต้มเท่ากันอีก ผู้เล่นแต่ละคนจั่วไพ่จากกองของตนเองมา 1 ใบ วางคว่ำลง แล้วจั่วอีก 1 ใบวางหงายหน้า
# คนที่แต้มสูงกว่าเก็บไพ่ทั้งหมดที่วางอยู่ (10 ใบ)
# ถ้าไพ่ที่เปิดมาแต้มเท่ากันอีกก็ทำไปเรื่อยๆ
#
# Winning condition:
# คนที่ไพ่หมดมือก่อนเป็นผู้แพ้

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    """
    Class Deck จะผลิต object ที่เป็นสำรับไพ่ 52 ใบเพื่อเริ่มเกมส์ 
    จงใช้ SUITE และ RANKS ในการสร้างสำรับไพ่
    แล้วแบ่งสำหรับนี้เป็น 2 ส่วนเพื่อแจกให้ผู้เล่น 
    Class นี้ควรมี method ที่ทำการ split สำรับเป็น 2 กองเท่า ๆ กัน และ method ที่ทำการสับไพ่
    """

    def __init__(self):
        print("Creating Deck for two player")
        self.deck = [(r, s) for r in RANKS for s in SUITE]

    def __str__(self):
        return str(self.deck)

    def shuffle(self):
        return shuffle(self.deck)

    def splitCard(self):
        return (self.deck[:26], self.deck[26:])


class Hand:
    '''
    Class Hand คือกองไพ่ในมือของผู้เล่น
    ควรมี method ในการ จั่วไพ่ออกมา และเพิ่มไพ่เข้ากอง
    '''

    def __init__(self, cards):
        self.cards = cards

    def add(self, new_card):
        self.cards.extend(new_card)

    def draw(self):
        return self.cards.pop()


class Player:
    """
    Class Player ควรเก็บชื่อผู้เล่น และ instance ของ object Hand
    ผู้เล่นควรจะสามารถเล่นไพ่ และ ตรวจสอบได้ว่าไพ่ของตัวเองหมดกองแล้วหรือยัง
    """

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        draw_card = self.hand.draw()
        print("Draw!!!")
        return draw_card

    def still_has_card(self):
        return len(self.hand.cards)


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
d1 = Deck()
d1.shuffle()
h1, h2 = d1.splitCard()
print("h1 : %d\nh2 : %d" % (len(h1), len(h2)))
# Use the 3 classes along with some logic to play a game of war!
