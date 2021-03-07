import random
import time


class PuKe:
    nums = [str(i) for i in range(2, 11)] + list('AJQK')
    suits = [chr(9824), chr(9829), chr(9827), chr(9830)]

    def __init__(self):
        self._cards = [(num, suit) for num in self.nums for suit in self.suits] + ['鬼']

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def xipai(self):
        return random.shuffle(self._cards)


class Players:
    def __init__(self, name):
        self._puke = []
        self.name = '玩家' + str(name)

    def get_puke(self, card):
        self._puke.append(card)

    def puke_nums(self):
        return len(self._puke)

    def showpuke(self):
        return self._puke

    def paibiao(self):
        return list(range(self.puke_nums()))

    def duipai(self, n):
        for i in self._puke:
            if n[0] == i[0]:
                self._puke.remove(i)
                return True
        self._puke.append(n)
        random.shuffle(self._puke)
        return False

    def xupai(self):
        l = []
        ll = [0]
        for i in self._puke:
            if i[0] not in ll:
                l.append(i)
                ll.append(i[0])
            else:
                l.remove(l[ll.index(i[0]) - 1])
                ll.remove(i[0])
        self._puke = l
        return self._puke


class Game:
    def __init__(self):
        self.players = []

    def get_winer(self, p):
        if p.puke_nums() == 0:
            self.players.remove(p)
            return True
        return False

    def get_player(self, p):
        for i in self.players:
            if p == i.name[-1]:
                return i

    def get_all_players(self):
        l = []
        for i in self.players:
            l.append(i.name)
        return l

    def get_index(self, n):
        l = []
        for i in self.players:
            l.append(i.name[-1])
        l.remove(n[-1])
        return l


def fliter(s, ss, a, b):
    val = input(s.format(list(range(a, b + 1))))
    while True:
        if val.isdigit():
            val = int(val)
            if a - 1 < val < b + 1:
                break
        val = input(ss.format(list(range(a, b + 1))))
    return val


def main():
    n = fliter('请输入玩家数量{}:', '请输入有效数字{}:', 3, 6)
    print('创建玩家中。。。')
    game = Game()
    for i in range(n):
        game.players.append(Players(i))
    time.sleep(1)
    print(game.get_all_players())
    puke = PuKe()
    print('洗牌....')
    puke.xipai()
    time.sleep(1)
    print('发牌。。。。')
    time.sleep(1)
    try:
        for i in range(53 // n + 1):
            for j in range(n):
                game.players[j].get_puke(puke._cards.pop())
    except:
        pass
    print('发牌完成。。。')
    print('你的手牌一共%d张' % game.players[0].puke_nums())
    print('你的手牌：', game.players[0].showpuke())
    time.sleep(1)
    print('对牌，除去相同的牌。。。')
    time.sleep(1)
    for i in range(n):
        game.players[i].xupai()
        print('\033[0;33m {}还有{}手牌\033[0m'.format(game.players[i].name, game.players[i].puke_nums()))
    print('你是玩家0')
    print('对牌完成，游戏开始！')
    while len(game.players) - 1 != 0:
        for i in game.players:
            n = i
            i = i.name
            if i == '玩家0':
                while True:
                    b_p = game.get_all_players()
                    b_p.remove(i)
                    print('你的手牌：', game.players[0].showpuke())
                    p = input('请选择被抽牌玩家{}(输入数字):'.format(b_p))
                    if p in game.get_index(i):
                        break
                by_player = game.get_player(p)
                other_puke = fliter('请选择玩家的手牌{}:', '请选择被抽牌玩家{},且输入正确数字:', 0, by_player.puke_nums() - 1)
                pai = by_player.showpuke().pop(other_puke)
                if game.get_winer(by_player):
                    print('\033[0;34m {}手牌被抽空，已经赢了 \033[0m'.format(by_player.name))
                print('你抽到%s的手牌：' % by_player.name, pai)
                pan_t = game.players[0].duipai(pai)
                if game.get_winer(game.players[0]):
                    print('\033[0;34m {}手牌被抽空，已经赢了 \033[0m'.format('玩家0'))
                while pan_t:
                    if len(game.players) == 1:
                        break
                    if by_player not in game.players:
                        while True:
                            b_p = game.get_all_players()
                            b_p.remove(i)
                            p = input('玩家{}已经获胜，请再选一位玩家抽取{}:'.format(by_player.name, b_p))
                            if p in game.get_index(i):
                                by_player = game.get_player(p)
                                break
                    other_puke = fliter('你抽中了，请再抽一张{}：', '请正确选择玩家的手牌{}:', 0, by_player.puke_nums() - 1)
                    pai = by_player.showpuke().pop(other_puke)
                    if game.get_winer(by_player):
                        print('\033[0;34m {}手牌被抽空，已经赢了 \033[0m'.format(by_player.name))
                    print('你抽到%s的手牌：' % by_player.name, pai)
                    pan_t = game.players[0].duipai(pai)
                    if game.get_winer(game.players[0]):
                        print('\033[0;34m {}手牌被抽空，已经赢了 \033[0m'.format('玩家0'))
                    time.sleep(1)
                if len(game.players) == 1:
                    break
                print('你没有抽中，轮到下一位玩家。')
                print('你的手牌：', game.players[0].showpuke())
                time.sleep(1)
            else:
                print('轮到%s' % i)
                by_player = random.choice(game.players)
                while by_player.name == i:
                    by_player = random.choice(game.players)
                ttt = True
                while ttt:
                    if len(game.players) == 1 or n not in game.players:
                        break
                    if by_player not in game.players:
                        by_player = random.choice(game.players)
                        while by_player.name == i:
                            by_player = random.choice(game.players)
                    puke_index = random.choice(by_player.paibiao())
                    pai = by_player.showpuke().pop(puke_index)
                    print('{}抽了{}的牌'.format(i, by_player.name))
                    if game.get_winer(by_player):
                        print('\033[0;34m {}手牌被抽空，已经赢了 \033[0m'.format(by_player.name))
                    ttt = n.duipai(pai)
                    if ttt:
                        print('{}抽中了{}'.format(i, pai))
                    if game.get_winer(n):
                        print('\033[0;34m {}手牌已经没有了手牌，已经赢了 \033[0m'.format(n.name))
                    time.sleep(1)
                if len(game.players) == 1 or n not in game.players:
                    break
                print('%s没抽中，轮到下一位玩家' % i)
                print('\033[0;33m {}还有{}张手牌\033[0m'.format(i, len(n._puke)))
                time.sleep(1)
    print('%s输了' % game.players[0].name)
    print('{}的手牌{}'.format(game.players[0].name, game.players[0].showpuke()))


main()
