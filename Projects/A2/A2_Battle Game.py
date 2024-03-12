class Soldier:
    def __init__(self, level, blood, direction, order):
        self.level = level
        self.blood = blood
        self.direction = direction
        self.order = order


def fight(invader, defender):
    if invader.blood > defender.blood:
        winner = Soldier(invader.level, invader.blood - 1, invader.direction, invader.order)
        return winner
    elif invader.blood < defender.blood:
        winner = Soldier(defender.level, defender.blood - 1, defender.direction, defender.order)
        return winner
    elif invader.blood == defender.blood:
        winner = Soldier(defender.level, 0, defender.direction, defender.order)
        return winner


if __name__ == "__main__":
    number_of_soldier = eval(input())
    data_set = []

    for i in range(number_of_soldier):
        level, blood, direction = input().split()
        soldier = Soldier(int(level), int(blood), direction, i)
        data_set.append(soldier)

    data_set.sort(key=lambda x: x.level)  # original data sample sorted

    home = []
    battlefield = []

    for i in data_set:
        home.append(i)

    while home:  # when all the soldiers being poped from home, the game stops
        invader = home.pop()  # always append the up most level soldier to the battlefield
        if invader.direction == 'D':
            battlefield.append(invader)  # all down won't fight
        elif invader.direction == 'U':  # fight can only happen when up happens
            if battlefield and (battlefield[-1].direction == 'D'):  # the condition for fight
                res = fight(invader, battlefield.pop())
                if res.blood != 0:
                    home.append(res)  # refresh the current level with the winner

            else:
                battlefield.append(invader)  # cannot meet the condition for fight

    answer_list = []
    while len(battlefield) != 0:
        ans = battlefield.pop()
        answer_list.append(ans)

    answer_list.sort(key=lambda x: x.order)

    for i in answer_list:
        print(i.blood)
