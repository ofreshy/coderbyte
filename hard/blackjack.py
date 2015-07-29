cvs = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'jack': 11,
        'queen': 12,
        'king': 13,
    }


def blackjack(hand):
    val = 0
    aces = 0
    mcv = 0
    max_card = None
    for card in hand:
        if card == 'ace':
            aces += 1
            continue
        cv = cvs[card]
        if cv > mcv:
            mcv = cv
            max_card = card
        val += min(cv, 10)

    if aces:
        if aces > 1:
            val += (aces-1) * 1
        if val + 11 <= 21:
            max_card = 'ace'
            val += 11
        else:
            val += 1

    if max_card == 'one':
        max_card = 'ace'

    if val < 21:
        return 'below %s' % max_card
    elif val > 21:
        return 'above %s' % max_card
    else:
        return 'blackjack %s' % max_card



assert blackjack(["one","one","one"])  == 'below ace'
assert blackjack(["four","ace","ten"]) == 'below ten'
assert blackjack(["two","three","ace","king"]) == 'below king'
assert blackjack(["four","ten","king","ace"]) == 'above king'
assert blackjack(["two","king","ace","ace"]) == 'below king'

