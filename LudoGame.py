# Description: a class called LudoGame that allows two to four people to play a simplified version of the game, Ludo.
# The LudoGame class communicates with the Player class.


class Player:
    """
    The Player object represents the player who plays the game at a certain position. Contains the position (referred to
    here as the team) the player chooses (A, B, C, D), start and end space, current position of the player's two tokens,
    and current state of the player. Each get and set method communicates with the LudoGame class to access and update
    the location of the player's tokens.
    """

    def __init__(self, team):
        """
        The constructor for Player class. Takes team (which the readme refers to as position) as a parameter.
        Initializes the required data members and all data members are private.
        """
        self._team = team  # team the player is on, A, B, C, or D (also the position the player chooses)

        # initialize self._start to the start and end space for a player on four teams
        if team == 'A':
            self._start = 1  # start space for this player
            self._end = 50  # end space for this player
        elif team == 'B':
            self._start = 15
            self._end = 8
        elif team == 'C':
            self._start = 29
            self._end = 22
        elif team == 'D':
            self._start = 43
            self._end = 36

        # H for Home Yard, R for Ready to Go, E for Finished Position, and any number space
        self._current_position = ['H', 'H']

        # if all games are complete or not complete, then the default is False
        self._current_state = False  # whether the player has won, finished, or is still playing

        # Reset these two step_counts every time token is kicked back at home position
        # initialize p_step_count to -1 at Home Yard position
        self._token_p_step_count = -1

        # initialize q_step_count to -1 at Home Yard position
        self._token_q_step_count = -1

    def get_completed(self):
        """
        Gets player's completion status. Takes no parameters and returns True if the player has finished the game or
        returns False if the player has not finished the game.
        """
        # Check if player is on the Finished position and return True if both tokens are on the E.
        if self._current_position == ['E', 'E']:
            return True

        else:
            return False

    def get_token_p_step_count(self):
        """
        Returns the total steps that token p has taken on the board as an integer.
        Takes no parameters and returns the total steps the token p has taken on the board (use steps = -1 for home
        yard position and steps = 0 for ready to go position).
        """
        return self._token_p_step_count

    def get_token_q_step_count(self):
        """
        Returns the total steps that token q had taken on the board as an integer.
        Takes no parameters and returns the total steps the token q has taken on the board (use steps = -1 for home yard
        position and steps = 0 for ready to go position).
        """
        return self._token_q_step_count

    def get_space_name(self, total_steps):
        """
        Gets the space name of where the token has landed on on the board as a string. Takes as a parameter the total
        steps (integer) of the token. It should be able to return the home yard position (‘H’) and the ready to go
        position (‘R’) as well. Includes 'E' (finished position). Must reset total steps of each token to -1 once it
        goes back home (in token_p and token_q).
        """
        if total_steps == -1:
            return 'H'
        elif total_steps == 0:
            return 'R'
        elif total_steps == 57:
            return 'E'

        # when entering the home squares on the way to 'E' (different from Home Yard)
        # elif 51 <= total_steps and total_steps <= 56:  # chained comparisons are ok in Python
        elif 51 <= total_steps <= 56:
            return self._team + str(total_steps - 50)

        # otherwise, calculate by start space for team
        if self._start == 1:  # team A
            return str(self._start + total_steps - 1)

        if self._start == 15:  # team B
            if 1 <= total_steps <= 42:
                return str(self._start + total_steps - 1)

            elif 43 <= total_steps <= 50:
                return str((self._start + total_steps - 1) - 56)

        if self._start == 29:  # team C
            if 1 <= total_steps <= 28:
                return str(self._start + total_steps - 1)

            elif 29 <= total_steps <= 50:
                return str((self._start + total_steps - 1) - 56)

        if self._start == 43:  # team D
            if 1 <= total_steps <= 14:
                return str(self._start + total_steps - 1)

            elif 15 <= total_steps <= 50:
                return str((self._start + total_steps - 1) - 56)

    def get_team(self):
        """
        Returns the player's team (referred to in the readme as position), which is 'A', 'B', 'C', or 'D'.
        The start and end position for each team is different on the board.
        """
        return self._team

    def get_player_token_p_position(self):
        """
        Returns the position of token p team as a string, like 'H' or '26.'
        """
        return self._current_position[0]

    def get_player_token_q_position(self):
        """
        Returns the position of token q team as a string, like 'H' or '26.'
        """
        return self._current_position[1]

    def set_token_p_step_count(self, steps):
        """
        Sets the token p step count to a new value as an integer. Takes steps (integer) as a parameter.
        The total step should not be larger than 57. Please note that if the token is bounced back in the home squares,
        this bounced part should be subtracted from the step count. For example, when token p is at space A5, the total
        step is 55 now. If it moves 5 steps and bounces back to A4, the total step should be 54, not 60.
        """
        if steps > 57:
            steps = 57 - (steps - 57)
        space = self.get_space_name(steps)
        self._current_position[0] = space
        self._token_p_step_count = steps

    def set_token_q_step_count(self, steps):
        """
        Sets the token q step count to a new value as an integer. Takes steps (integer) as a parameter.
        The total step should not be larger than 57.
        """
        if steps > 57:
            steps = 57 - (steps - 57)
        space = self.get_space_name(steps)
        self._current_position[1] = space
        self._token_q_step_count = steps

    def get_current_position(self):
        """
        Returns current position for a player. Example, ['H', 'H'].
        """
        return self._current_position

    def get_next_p_space(self, steps):
        """
        Returns the next space on the board that a player's token p could land on; use this for kick off priority.
        """
        return self.get_space_name(self.get_token_p_step_count() + steps)

    def get_next_q_space(self, steps):
        """
        Returns the next space on the board that a player's token q could land on; use this for kick off priority.
        """
        return self.get_space_name(self.get_token_q_step_count() + steps)


class LudoGame:
    """
    The LudoGame object represents the game as played. Contains information about the players and the board. Game is
    played by two, three, or four players. Communicates with Player class to use and update those data members that
    contain information about the location of the player's tokens.
    """

    def __init__(self):
        """
        The constructor for the LudoGame class. Takes no parameters. Initializes the required data members and all data
        members are private.
        """
        self._players_list = []  # store Player objects

    def get_player_by_position(self, player_position):
        """
        Gets the player position; returns the player object. Takes a parameter representing the player’s position as a
        string and returns the player object. For an invalid string parameter, it will return "Player not found!"
        Purpose: checks if the player exists or not.
        """
        # get player by team name
        for player in self._players_list:
            if player.get_team() == player_position:
                return player

        return "Player not found!"

    def move_token(self, player_object, token_name, token_step_count):
        """
        Takes three parameters, the player object, the token name (‘p’ or ‘q’) as strings, and the steps the token will
        move on the board (integer). Purpose: this method will take care of one token moving on the board. It will also
        update the token’s total steps, and it will take care of kicking out other opponent tokens as needed.
        The play_game method will use this method to move the token.
        """
        if player_object.get_completed():
            return

        # access Player class
        p_step_count = player_object.get_token_p_step_count()
        q_step_count = player_object.get_token_q_step_count()

        if token_name == 'p':
            # if token is on H and player rolls 6, move to ready to go
            if p_step_count == -1 and token_step_count == 6:
                # update to ready to go square
                player_object.set_token_p_step_count(0)

            # if token is making a normal move after moving off H
            elif p_step_count >= 0:
                # update the token step count, add p_step_count and token_step_count
                player_object.set_token_p_step_count(p_step_count + token_step_count)
                # stack tokens; do not stack on R
                if p_step_count > 0 and p_step_count == q_step_count:
                    player_object.set_token_q_step_count(p_step_count + token_step_count)

        elif token_name == 'q':
            # if token is on H and player rolls 6, move to ready to go
            if q_step_count == -1 and token_step_count == 6:
                # update to ready to go square
                player_object.set_token_q_step_count(0)

            # if token is making a normal move after moving off H
            elif q_step_count >= 0:
                # update the token step count, add q_step_count and token_step_count
                player_object.set_token_q_step_count(q_step_count + token_step_count)
                # stack tokens; do not stack on R
                if q_step_count > 0 and p_step_count == q_step_count:
                    player_object.set_token_p_step_count(q_step_count + token_step_count)

        # loop through each player in players list
        for player in self._players_list:

            # same player, don't kick off
            if player.get_team() == player_object.get_team():
                continue

            # kick off the token back to -1 if tokens from different teams land on same board square
            if token_name == 'p':
                # do not kick off a token on R
                if player.get_player_token_p_position() == "R":
                    return
                if player.get_player_token_p_position() == player_object.get_player_token_p_position():
                    player.set_token_p_step_count(-1)

                if player.get_player_token_q_position() == player_object.get_player_token_p_position():
                    player.set_token_q_step_count(-1)

            elif token_name == 'q':
                # do not kick off a token on R
                if player.get_player_token_q_position() == "R":
                    return
                if player.get_player_token_q_position() == player_object.get_player_token_q_position():
                    player.set_token_q_step_count(-1)

                if player.get_player_token_p_position() == player_object.get_player_token_q_position():
                    player.set_token_p_step_count(-1)

    def current_spaces(self):
        """
        Helper method for play_game. Returns a list of current spaces.
        """
        # initialize a list of current spaces to return
        spaces = []
        # loop through players_list (list of player objects)
        for player in self._players_list:
            # add current space and current position and assigns result to current_spaces
            spaces += player.get_current_position()
        return spaces

    def play_game(self, players, turns):
        """
        Takes two parameters, the players list, and the turns list. Returns a list of strings representing the current
        spaces of all of the tokens for each player in the list after moving the tokens following the priority rules.
            * param 1: players is the list of team positions players ['A', 'B', 'C', 'D']
            * param 2: turns is the list of tuples, each tuple is a roll for one player [('A', 6), ('A', 4), ('C', 5)]
        Purpose: this method will create the player list first using the players list pass in, and then move the
        tokens according to the turns list following the priority rule and update the tokens position and the player’s
        game state (whether finished the game or not).
        """
        # loop through the players list
        for player_name in players:
            new_player_object = Player(player_name)  # create a new player object
            self._players_list.append(new_player_object)  # add the new object to the players_list

        # loop through the turns list, extract data from the tuple
        for turn in turns:
            # print(turn)
            player = turn[0]
            total_steps = turn[1]

            # access the player object through self._get_player_by_position
            player_object = self.get_player_by_position(player)

            # call the decision-making algorithm
            token = self.decision_making_algo(total_steps, player_object)
            # print("token:", token)

            # call move_token method
            self.move_token(player_object, token, total_steps)
            # print(self.current_spaces())

        return self.current_spaces()

    def decision_making_algo(self, step, player_object):
        """
        Returns a token name (p or q). Takes two parameters, step (integer) and player_object (object). The play_game
        method will use this method.
        Purpose: helps decide which token is appropriate to pass to the move_token method that will be called in the
        play_game method using the priority rules outlined in the readme.
        """
        # prevent token from moving off 'H' before rolling a 6 by moving the opposite token
        if step < 6 and player_object.get_player_token_p_position() == 'H':
            return 'q'
        if step < 6 and player_object.get_player_token_q_position() == 'H':
            return 'p'

        # Rule 1: If the die roll is 6, try to let the token that still in the home yard get out of the home yard (if
        # both tokens are in the home yard, choose the first one ‘p’)
        if step == 6:
            # for p token
            if player_object.get_player_token_p_position() == 'H':
                return 'p'

            # for q token
            elif player_object.get_player_token_q_position() == 'H':
                return 'q'

        # Rule 2: If one token is already in the home square and the step number is exactly what is needed to reach the
        # end square, let that token move and finish
        # if 51 <= player_object.get_token_p_step_count() and player_object.get_token_p_step_count() <= 56:
        # chained comparisons ok
        if 51 <= player_object.get_token_p_step_count() <= 56:
            if player_object.get_token_p_step_count() + step == 57:
                return 'p'

        # elif 51 <= player_object.get_token_q_step_count() and player_object.get_token_q_step_count() <= 56:
        # chained comparison ok
        elif 51 <= player_object.get_token_q_step_count() <= 56:
            if player_object.get_token_q_step_count() + step == 57:
                return 'q'

        # Rule 3: If one token can move and kick out an opponent token, then move that token
        # are players/teams different? if yes, is the position the same? if yes, then move that token
        # print("Next p space: ", player_object.get_next_p_space(step))

        for player in self._players_list:
            if player_object is not player:
                if player_object.get_next_p_space(step) in player.get_current_position():
                    return 'p'
                if player_object.get_next_q_space(step) in player.get_current_position():
                    return 'q'

        # Rule 4: Move the token that is further away from the finishing square ('E' or '57')
        # the step count tells how far the token is away from the finishing square
        if player_object.get_token_p_step_count() < player_object.get_token_q_step_count():
            return 'p'

        # else: move q because other conditions should be caught my higher priority rules
        else:
            return 'q'


# # # Below for testing functionality only # # #
def main():
    # # # # # Case 9
    players_9 = ['A', 'B']
    turns_9 = [('A', 6), ('A', 4), ('A', 4), ('A', 4), ('A', 6), ('A', 5), ('A', 3), ('B', 6), ('B', 2), ('A', 2),
               ('A', 4)]
    # # output_9 = ['16', '10', 'H', 'H']

    # creates a game object
    game = LudoGame()

    # calls to methods
    current_tokens_space = game.play_game(players_9, turns_9)  # read the list, check output
    #
    print("--- Start of readme print statements (compare w/ expected output):")
    # returns current string
    print(current_tokens_space)  # H, R, E, or 1-56, A1-A5, B1-B5, C1-C5, D1-D5

    player_A = game.get_player_by_position('A')
    print("Ap:", player_A.get_token_p_step_count())
    print("Aq:", player_A.get_token_q_step_count())

    player_B = game.get_player_by_position('B')
    print("Bq:", player_B.get_token_q_step_count())

    # True if completed or False if not completed
    print(player_A.get_completed())
    # returns the name of the space the token has landed on on the board as a string
    print(player_B.get_space_name(5))
    print("--- End of readme print statements")

    # And the output will be:
    print("Case 9: Expected output:")
    print("['16', '10', 'H', 'H']")
    print("-1 # Bq step count for player B, token p on H")
    print("False, game isn't over")
    print("19  # Player B took 5 steps and is on space 19 (either p or q, doesn't matter))")

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # players_6 = ['A', 'B']
    # turns_6 = [('A', 6), ('A', 2), ('A', 2), ('A', 6), ('A', 4), ('A', 5), ('A', 4), ('A', 4), ('B', 6), ('B', 3),
    #            ('A', 6), ('A', 3)]
    # # output_6 = ['3', 'H', '17', 'H']
    #
    # # creates a game object
    # game = LudoGame()
    #
    # # calls to methods
    # current_tokens_space = game.play_game(players_6, turns_6)  # read the list, check output
    # #
    # print("--- Start of readme print statements (compare w/ expected output):")
    # # returns current string
    # print(current_tokens_space)  # H, R, E, or 1-56, A1-A5, B1-B5, C1-C5, D1-D5
    #
    # player_A = game.get_player_by_position('A')
    # print("Ap:", player_A.get_token_p_step_count())
    # print("Aq:", player_A.get_token_q_step_count())
    #
    # player_B = game.get_player_by_position('B')
    # # returns the total steps the token p has taken on the board for player B
    # print("Bp:", player_B.get_token_p_step_count(), "-- why is this printing 3 here when it's 17 above?")
    # print("Bq:", player_B.get_token_q_step_count())
    #
    # # True if completed or False if not completed
    # print(player_A.get_completed())
    # # returns the name of the space the token has landed on on the board as a string
    # print(player_B.get_space_name(5))
    # print("--- End of readme print statements")
    #
    # # And the output will be:
    # print("Case 6: Expected output:")
    # print("['3', 'H', '17', 'H']")
    # print("17 # Bp step count for player B, token p on 17")
    # print("False, game isn't over")
    # print("19  # Player B is on space 1 (either p or q, doesn't matter))")

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # players_5 = ['A', 'B']
    # turns_5 = [('A', 6), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 6), ('A', 4), ('A', 6), ('A', 4), ('A', 6),
    #            ('A', 6), ('A', 4), ('A', 6), ('A',4), ('A', 6), ('A', 6), ('A', 4), ('A', 6), ('A', 6), ('A', 4),
    #            ('A', 6), ('A', 6), ('A', 4), ('A', 6), ('A', 3), ('A', 6), ('B', 6), ('A', 6)]
    #
    # # output_5 = ['E', 'E', 'R', 'H']
    #
    # # creates a game object
    # game = LudoGame()
    #
    # # calls to methods
    # current_tokens_space = game.play_game(players_5, turns_5)  # read the list, check output
    # #
    # print("--- Start of readme print statements (compare w/ expected output):")
    # # returns current string
    # print(current_tokens_space)  # H, R, E, or 1-56, A1-A5, B1-B5, C1-C5, D1-D5
    #
    # player_A = game.get_player_by_position('A')
    # print(player_A.get_token_p_step_count())
    # print(player_A.get_token_q_step_count())
    #
    # player_B = game.get_player_by_position('B')
    # # returns the total steps the token p has taken on the board for player B
    # print(player_B.get_token_p_step_count())
    # print(player_B.get_token_q_step_count())
    #
    # # True if completed or False if not completed
    # print(player_A.get_completed())
    # # returns the name of the space the token has landed on on the board as a string
    # print(player_B.get_space_name(5))
    # print("--- End of readme print statements")
    #
    # # And the output will be:
    # print("Case 5: Expected output:")
    # print("['E', 'E', 'R', 'H']")
    # print("57 # Ap step count for player A, token p on E")
    # print("True # game is completed for Player A")
    # print("19  # Player B is on space 19 (either p or q, doesn't matter))")

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # Case 4:
    # players_4 = ['A', 'C']
    # turns_4 = [('A', 6), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 6), ('A', 4), ('A', 6), ('A', 4), ('A', 6),
    #          ('A', 6), ('A', 6), ('A', 4), ('A',
    #                                         6), ('A', 6), ('C', 6), ('C', 4)]
    # # # output_ 4 = ['33', 'H', '32', 'H']
    #
    # # creates a game object
    # game = LudoGame()
    #
    # # calls to methods
    # current_tokens_space = game.play_game(players_4, turns_4)  # read the list, check output
    # #
    # print("--- Start of readme print statements (compare w/ expected output):")
    # # returns current string
    # print(current_tokens_space)  # H, R, E, or 1-56, A1-A5, B1-B5, C1-C5, D1-D5
    #
    # player_A = game.get_player_by_position('A')
    # print(player_A.get_token_p_step_count())
    # print(player_A.get_token_q_step_count())
    #
    # player_C = game.get_player_by_position('C')
    # # returns the total steps the token p has taken on the board for player B
    # print(player_C.get_token_p_step_count())
    # print(player_C.get_token_q_step_count())
    #
    # # True if completed or False if not completed
    # print(player_A.get_completed())
    # # returns the name of the space the token has landed on on the board as a string
    # print(player_C.get_space_name(1))
    # print("--- End of readme print statements")
    #
    # # And the output will be:
    # print("Case 4: Expected output:")
    # print("['33', 'H', '32', 'H']")
    # print("-1  # Cq step count for player C, token p on H")
    # print("False  # game is not completed for Player A")
    # print("29  # Player C is on space 1 (either p or q, doesn't matter))")

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # Case_2:
    # players_2 = ['A', 'B']
    # turns_2 = [('B', 6), ('B', 4), ('B', 5), ('B', 4), ('B', 4), ('B', 3), ('B', 4), ('B', 5), ('B', 4), ('B', 4),
    #            ('B', 5), ('B', 4), ('B', 1), ('B', 4), ('B', 5), ('B', 5), ('B', 5)]
    # # output_2 = ['H', 'H', 'B6', 'H']
    #
    # # creates a game object
    # game = LudoGame()
    #
    # # calls to methods
    # current_tokens_space = game.play_game(players_2, turns_2)  # read the list, check output
    # #
    # print("--- Start of readme print statements:")
    # # returns current string
    # print(current_tokens_space)  # H, R, E, or 1-56, A1-A5, B1-B5, C1-C5, D1-D5
    #
    # player_A = game.get_player_by_position('A')
    # print(player_A.get_token_p_step_count())
    # print(player_A.get_token_q_step_count())
    #
    # player_B = game.get_player_by_position('B')
    # # returns the total steps the token p has taken on the board for player B
    # print(player_B.get_token_p_step_count())
    # print(player_B.get_token_q_step_count())
    #
    # # True if completed or False if not completed
    # print(player_A.get_completed())
    # # returns the name of the space the token has landed on on the board as a string
    # print(player_B.get_space_name(1))
    # print("--- End of readme print statements")
    #
    # # And the output will be:
    # print("Case 2: Expected output:")
    # print("['H', 'H', 'B6', 'H']")
    # print("56  # Bp step count for player B, token p on B6")
    # print("False  # game is not completed for Player A")
    # print("15  # Player B is on space 1 (either p or q, doesn't matter))")

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # Case 0 (from readme)
    # players = ['A', 'B']
    # turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4), ('B', 1), ('B', 2), ('A', 6), ('A', 4),
    #          ('A', 6), ('A', 3), ('A', 5), ('A', 1), ('A', 5), ('A', 4)]
    #
    # # creates a game object
    # game = LudoGame()
    #
    # # calls to methods
    # current_tokens_space = game.play_game(players, turns)  # read the list, check output
    #
    # player_A = game.get_player_by_position('A')
    # #
    # # print(game.decision_making_algo(6, player_A))  # move p out of home to space 1
    # # game.move_token(player_A, 'p', 6)
    # # print(player_A.get_player_token_p_position())  # should be R
    # # print(player_A.get_player_token_q_position())  # should be H
    # # print(game.decision_making_algo(4, player_A))  # should be p, moved to 4
    # #
    # print("--- Start of readme print statements:")
    # # True if completed or False if not completed
    # print(player_A.get_completed())
    #
    # # returns the total steps the token p has taken on the board for player A
    # print(player_A.get_token_p_step_count())
    #
    # print(current_tokens_space)  # H, R, E, or 1-56, A1-A5, B1-B5, C1-C5, D1-D5
    #
    # player_B = game.get_player_by_position('B')
    #
    # # returns the name of the space the token has landed on on the board as a string
    # print(player_B.get_space_name(55))
    # print("--- End of readme print statements")
    # #
    # # And the output will be:
    # print()
    # print("Expected output:")
    # print("False  # game is not completed for Player A")
    # print("28  # Ap step count for player A, token p")
    # print("[‘28’, ‘28’, ‘21’, ‘H’]  # current token spaces are Ap on 28, Aq on 28, Bp on 21, Bq on Home Yard")
    # print("B5  # Player B is on space 55 (either p or q, doesn't matter))")
    #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # Case 1:
    # players_1 = ['A', 'B', 'C', 'D']
    # turns_1 = [('A', 6), ('A', 1), ('B', 6), ('B', 2), ('C', 6), ('C', 3), ('D', 6), ('D', 4)]
    # # output_1 = ['1', 'H', '16', 'H', '31', 'H', '46', 'H']
    # #
    # game = LudoGame()
    # current_tokens_space = game.play_game(players_1, turns_1)
    # player_A = game.get_player_by_position('A')
    # print(player_A.get_completed())
    # print(player_A.get_token_p_step_count())
    # print(current_tokens_space)
    # player_B = game.get_player_by_position('B')
    # player_C = game.get_player_by_position('C')
    # player_D = game.get_player_by_position('D')
    # print(player_D.get_space_name(3))

    # # # Case_2:
    # players_2 = ['A', 'B']
    # turns_2 = [('B', 6), ('B', 4), ('B', 5), ('B', 4), ('B', 4), ('B', 3), ('B', 4), ('B', 5), ('B', 4), ('B', 4),
    #            ('B', 5), ('B', 4), ('B', 1), ('B', 4), ('B', 5), ('B', 5), ('B', 5)]
    # # output_2 = ['H', 'H', 'B6', 'H']
    #
    # # # Case 3:
    # players_3 = ['A', 'B']
    # turns_3 = [('A', 6), ('A', 3), ('A', 6), ('A', 3), ('A', 6), ('A', 5), ('A', 4), ('A', 6), ('A', 4)]
    # # output_3 = ['28', '28', 'H', 'H']
    #
    # # # Case 4:
    # players_4 = ['A', 'C']
    # turns_4 = [('A', 6), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 6), ('A', 4), ('A', 6), ('A', 4), ('A', 6),
    #          ('A', 6), ('A', 6), ('A', 4), ('A',
    #                                         6), ('A', 6), ('C', 6), ('C', 4)]
    # # output_ 4 = ['33', 'H', '32', 'H']
    #
    # # # Case 5:
    # players_5 = ['A', 'B']
    # turns_5 = [('A', 6), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 6), ('A', 4), ('A', 6), ('A', 4), ('A', 6),
    #            ('A', 6), ('A', 4), ('A', 6), ('A',4), ('A', 6), ('A', 6), ('A', 4), ('A', 6), ('A', 6), ('A', 4),
    #            ('A', 6), ('A', 6), ('A', 4), ('A', 6), ('A', 3), ('A', 6), ('B', 6), ('A', 6)]
    # # output_5 = ['E', 'E', 'R', 'H']
    #
    # # # Case 6:
    # players_6 = ['A', 'B']
    # turns_6 = [('A', 6), ('A', 2), ('A', 2), ('A', 6), ('A', 4), ('A', 5), ('A', 4), ('A', 4), ('B', 6), ('B', 3),
    #            ('A', 6), ('A', 3)]
    # # output_6 = ['3', 'H', '17', 'H']
    #
    # # # Case 7:
    # players_7 = ['A', 'B']
    # turns_7 = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 4), ('A', 5), ('A', 5),
    #            ('A', 3), ('A', 5), ('A', 3), ('A', 6)]
    # # output_7 ['A1', 'R', 'H', 'H']
    #
    # # # Case 8:
    # players_8 = ['A', 'B']
    # turns_8 = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 4), ('A', 5), ('A', 5),
    #            ('A', 3), ('A', 5), ('A', 5), ('A',
    #                                           6), ('A', 5), ('A', 5), ('A', 3), ('B', 6), ('B', 3), ('A', 4)]
    # # output_8 = ['E', '13', '17', 'H']
    #
    # # # Case 9:
    # players_9 = ['A', 'B']
    # turns_9 = [('A', 6), ('A', 4), ('A', 4), ('A', 4), ('A', 6), ('A', 5), ('A', 3), ('B', 6), ('B', 2), ('A', 2),
    #            ('A', 4)]
    # # output_9 = ['16', '10', 'H', 'H']

    # # get space name tests
    # # # test for C
    # game = LudoGame()
    # players = ['A', 'B', 'C', 'D']
    # turns = []
    # game.play_game(players, turns)
    # player_C = game.get_player_by_position('C')
    # test1 = player_C.get_space_name(1)  # this should return 29, and it looks like it is!
    # test5 = player_C.get_space_name(5)
    # test10 = player_C.get_space_name(10)
    # test15 = player_C.get_space_name(15)
    # test20 = player_C.get_space_name(20)
    # test25 = player_C.get_space_name(25)
    # test28 = player_C.get_space_name(28)
    # test29 = player_C.get_space_name(29)
    # test30 = player_C.get_space_name(30)
    # test35 = player_C.get_space_name(35)
    # test40 = player_C.get_space_name(40)
    # test45 = player_C.get_space_name(45)  # fixed this should return 17, prev: THIS IS THE ONE THAT'S FAILING
    # test50 = player_C.get_space_name(50)  # this should be 22
    # test54 = player_C.get_space_name(54)  # this should be C4
    # test55 = player_C.get_space_name(55)
    # test56 = player_C.get_space_name(56)
    # test57 = player_C.get_space_name(57)
    #
    # print("test 1, return 29:", test1)
    # print("test 5, return 33:", test5)
    # print("test 10, return 38:", test10)
    # print("test 15, return 43:", test15)
    # print("test 20, return 48:", test20)
    # print("test 25, return 53:", test25)
    # print("test 28, return 56:", test28)  # last good one
    # print("test 29, return 1:", test29)  # fixed, prev wrong return of 57
    # print("test 30, return 2:", test30)  # fixed, prev wrong return of 58
    # print("test 35, return 7:", test35)  # fixed, prev wrong return of 63
    # print("test 40, return 12:", test40)  # fixed, prev wrong return of 68
    # print("test 45, return 17:", test45)
    # print("test 50, return 22:", test50)
    # print("test 54, return C4:", test54)
    # print("test 55, return C5:", test55)
    # print("test 56, return C6:", test56)
    # print("test 57, return E:", test57)

    # # # tests for A
    # game = LudoGame()
    # players = ['A', 'B', 'C', 'D']
    # turns = []
    # game.play_game(players, turns)
    # player_A = game.get_player_by_position('A')
    # test3 = player_A.get_space_name(1)  # this should return 1
    # test4 = player_A.get_space_name(45)  # this should return 45
    #
    # print("test 3:", test3)
    # print("test 4:", test4)
    #
    # # # tests for B
    # game = LudoGame()
    # players = ['A', 'B', 'C', 'D']
    # turns = []
    # game.play_game(players, turns)
    # player_B = game.get_player_by_position('B')
    # test1 = player_B.get_space_name(1)  # this should return 29, and it looks like it is!
    # test5 = player_B.get_space_name(5)
    # test10 = player_B.get_space_name(10)
    # test15 = player_B.get_space_name(15)
    # test20 = player_B.get_space_name(20)
    # test25 = player_B.get_space_name(25)
    # test28 = player_B.get_space_name(28)
    # test29 = player_B.get_space_name(29)
    # test30 = player_B.get_space_name(30)
    # test35 = player_B.get_space_name(35)
    # test40 = player_B.get_space_name(40)
    # test45 = player_B.get_space_name(45)  # fixed this should return 17, prev: THIS IS THE ONE THAT'S FAILING
    # test50 = player_B.get_space_name(50)  # this should be 22
    # test54 = player_B.get_space_name(54)  # this should be C4
    # test55 = player_B.get_space_name(55)
    # test56 = player_B.get_space_name(56)
    # test57 = player_B.get_space_name(57)
    #
    # print("test 1, return 15:", test1)
    # print("test 5, return 19:", test5)
    # print("test 10, return 24:", test10)
    # print("test 15, return 29:", test15)
    # print("test 20, return 34:", test20)
    # print("test 25, return 39:", test25)
    # print("test 28, return 42:", test28)
    # print("test 29, return 43:", test29)
    # print("test 30, return 44:", test30)
    # print("test 35, return 49:", test35)
    # print("test 40, return 54:", test40)
    # print("test 45, return 3:", test45)
    # print("test 50, return 8:", test50)
    # print("test 54, return B4:", test54)
    # print("test 55, return B5:", test55)
    # print("test 56, return B6:", test56)
    # print("test 57, return E:", test57)

    # # # tests for D
    # game = LudoGame()
    # players = ['A', 'B', 'C', 'D']
    # turns = []
    # game.play_game(players, turns)
    # player_D = game.get_player_by_position('D')
    # test1 = player_D.get_space_name(1)
    # test5 = player_D.get_space_name(5)
    # test10 = player_D.get_space_name(10)
    # test14 = player_D.get_space_name(14)
    # test15 = player_D.get_space_name(15)
    # test20 = player_D.get_space_name(20)
    # test25 = player_D.get_space_name(25)
    # test30 = player_D.get_space_name(30)
    # test34 = player_D.get_space_name(34)
    # test40 = player_D.get_space_name(40)
    # test50 = player_D.get_space_name(50)
    # test55 = player_D.get_space_name(55)
    # test57 = player_D.get_space_name(57)
    #
    # print("test 1, return 43:", test1)
    # print("test 5, return 47:", test5)
    # print("test 10, return 52:", test10)
    # print("test 14, return 56:", test14)
    # print("test 15, return 1:", test15)  # fixed,prev wrong return of 57
    # print("test 20, return 6:", test20)  # fixed, prev wrong return of 62
    # print("test 25, return 11:", test25)  # fixed, prev wrong return of 72
    # print("test 30, return 16:", test30)  # fixed, prev wrong return of 76
    # print("test 34, return 20:", test34)  # fixed, prev wrong return of 76
    # print("test 40, return 26:", test40)  # fixed, prev wrong return of 82
    # print("test 50, return 36:", test50)
    # print("test 55, return D5:", test55)
    # print("test 57, return E:", test57)

    # test1d = player_D.get_space_name(1)  # this should return 43
    # test2d = player_D.get_space_name(45)  # this should return 31
    # test3d = player_D.get_space_name(50)  # this should return 36
    # test4d = player_D.get_space_name(52)  # this should return D2
    #
    # print("test 1d:", test1d)
    # print("test 2d:", test2d)
    # print("test 3d:", test3d)
    # print("test 4d:", test4d)


if __name__ == '__main__':
    main()
