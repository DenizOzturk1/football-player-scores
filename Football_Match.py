class Team:
    def __init__(self, name, league, city, country, manager_name, conference):
        self.name = name
        self.league = league
        self.city = city
        self.country = country
        self.manager_name = manager_name
        self.conference = conference


class Player:
    def __init__(self, first_name, last_name, team):
        self.first_name = first_name
        self.last_name = last_name
        self.team = team

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Match:
    def __init__(self, home_team, away_team, date):
        self.home_team = home_team
        self.away_team = away_team
        self.date = date
        self.home_scores = {}
        self.away_scores = {}

    def home_score(self):
        return sum(self.home_scores.values())

    def away_score(self):
        return sum(self.away_scores.values())

    def winner(self):
        home_score = self.home_score()
        away_score = self.away_score()
        if home_score > away_score:
            return self.home_team
        elif away_score > home_score:
            return self.away_team
        else:
            return None

    def add_score(self, player, score):
        team = player.team
        if team == self.home_team:
            scores = self.home_scores
        elif team == self.away_team:
            scores = self.away_scores
        else:
            return

        if player.full_name() in scores:
            scores[player.full_name()] += score
        else:
            scores[player.full_name()] = score


# Teams
team1 = Team("Team A", "League X", "City A", "Country X", "Manager A", "Conference X")
team2 = Team("Team B", "League X", "City B", "Country X", "Manager B", "Conference X")
team3 = Team("Team C", "League Y", "City C", "Country Y", "Manager C", "Conference Y")

# Players
player1 = Player("Lionel", "Messi", team1)
player2 = Player("Erling", "Haaland", team2)
player3 = Player("Kylian", "Mbappe", team3)

# Matches
matches = []

match1 = Match(team1, team2, "01/06/2023")
match1.add_score(player1, 2)
match1.add_score(player2, 1)
matches.append(match1)

match2 = Match(team1, team3, "04/06/2023")
match2.add_score(player1, 3)
match2.add_score(player3, 2)
matches.append(match2)


# Helper functions
def city(match):
    return match.home_team.city


def country(match):
    return match.home_team.country


def highest_score():
    max_score = 0
    max_score_details = None
    for match in matches:
        for player, score in match.home_scores.items():
            if score > max_score:
                max_score = score
                max_score_details = (player, match.home_team.name, match.date, score)

        for player, score in match.away_scores.items():
            if score > max_score:
                max_score = score
                max_score_details = (player, match.away_team.name, match.date, score)

    return max_score_details


def highest_score_for_player(player):
    max_score = 0
    max_score_details = None
    for match in matches:
        if player.full_name() in match.home_scores:
            score = match.home_scores[player.full_name()]
            if score > max_score:
                max_score = score
                max_score_details = (player.full_name(), match.home_team.name, match.date, score)

        if player.full_name() in match.away_scores:
            score = match.away_scores[player.full_name()]
            if score > max_score:
                max_score = score
                max_score_details = (player.full_name(), match.away_team.name, match.date, score)

    return max_score_details


def highest_scorer():
    player_scores = {}

    for match in matches:
        for player, score in match.home_scores.items():
            player_scores[player] = player_scores.get(player, 0) + score
        for player, score in match.away_scores.items():
            player_scores[player] = player_scores.get(player, 0) + score

    highest_scorer = max(player_scores, key=player_scores.get)
    return highest_scorer, player_scores[highest_scorer]


def highest_average_scorer():
    player_scores = {}
    player_matches = {}

    for match in matches:
        for player, score in match.home_scores.items():
            player_scores[player] = player_scores.get(player, 0) + score
            player_matches[player] = player_matches.get(player, 0) + 1

        for player, score in match.away_scores.items():
            player_scores[player] = player_scores.get(player, 0) + score
            player_matches[player] = player_matches.get(player, 0) + 1

    highest_average = 0
    highest_average_scorer = None

    for player in player_scores:
        average_score = player_scores[player] / player_matches[player]
        if average_score > highest_average:
            highest_average = average_score
            highest_average_scorer = player

    return highest_average_scorer, highest_average

# En yüksek gol atan oyuncuyu ekrana yazdır
print("En yüksek gol atan oyuncu:", highest_scorer())

# En çok gol atan oyuncunun ortalaması
print("En yüksek ortalama gol atan oyuncu:", highest_average_scorer())

# En fazla gol atan oyuncunun bilgileri
print("Maç başına en yüksek gol:", highest_score())


                