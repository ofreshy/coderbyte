import random
import itertools


class Campaign():
    """An ad campaign we can serve to users."""

    def __init__(self, name, bid_price, target_keywords_list):
        """
        :param name: unique name for this campaign, e.g. "Nike Shoes Summer 2014"
        :param bid_price: amount to bid on any auctions when serving this campaign, e.g. 0.5
        :param target_keywords_list: list of keywords we are targeting for this campaign
        """
        self.name = name
        self.bid_price = bid_price
        self.target_key_words = set(target_keywords_list)


def choose_best_campaign_for_user(search_terms_list, campaigns):
    """Returns the best campaign to serve for a given user or None if
    no campaigns are applicable. A user can be served a campaign if they
    have searched for at least one keyword configured for the campaign.
    The "best" campaign to serve is the one with the most search term
    matches.
    If two or more campaigns have the same number of matches then the
    one with the highest bid_price should be served.
    If two or more campaigns have the same number of matches and the
    same bid_price then it should be a random pick between these campaigns.
    """
    search_terms_list = set(search_terms_list)
    best_score = -1, -1
    best_campaigns = []
    for campaign in campaigns:
        score = len(campaign.target_key_words & search_terms_list), campaign.bid_price

        if score[0] < best_score[0] or (score[0] == best_score[0] and score[1] < best_score[1]):
            continue

        if score[0] > best_score[0] or score[1] > best_score[1]:
            best_campaigns = [campaign]
        else:
            best_campaigns.append(campaign)
        best_score = score

    return random.choice(best_campaigns)


def choose_best_campaign_for_user_comparator(search_terms_list, campaigns):
    """Returns the best campaign to serve for a given user or None if
    no campaigns are applicable. A user can be served a campaign if they
    have searched for at least one keyword configured for the campaign.
    The "best" campaign to serve is the one with the most search term
    matches.
    If two or more campaigns have the same number of matches then the
    one with the highest bid_price should be served.
    If two or more campaigns have the same number of matches and the
    same bid_price then it should be a random pick between these campaigns.
    """
    search_terms_list = set(search_terms_list)
    decorated = [(len(c.target_key_words & search_terms_list), c.bid_price, i) for i, c in enumerate(campaigns)]
    sorted_campaigns = sorted(decorated, reverse=True)
    match, bid_price = sorted_campaigns[0][0], sorted_campaigns[0][1]
    best_campaigns = list(itertools.takewhile(lambda x: x[0] == match and x[1] == bid_price, sorted_campaigns))
    return campaigns[random.choice(best_campaigns)[2]]

campaigns = [
    Campaign("a", 5, ["Mac", "iPhone"]),
    Campaign("b", 5, ["Mac", "iPhone"]),
    Campaign("c", 4, ["Mac", "iPhone"]),

    Campaign("d", 4, ["PC", "Android", "JellyBean"]),
    Campaign("e", 4, ["PC", "Android"]),
    Campaign("f", 5, ["PC", "Android"]),
]

APPLE_ST = ["iPhone", "Mac", "OS", "iOS"]
PC_ST = ["PC", "Android", "Windows", "JellyBean"]


assert choose_best_campaign_for_user(APPLE_ST, campaigns).name in "ab"
assert choose_best_campaign_for_user(PC_ST, campaigns).name == "d"


assert choose_best_campaign_for_user_comparator(APPLE_ST, campaigns).name in "ab"
assert choose_best_campaign_for_user_comparator(PC_ST, campaigns).name == "d"
