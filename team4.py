####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team_Name' # Only 10 chars displayed.
strategy_name = 'BETRAYAL'
strategy_description = 'Betrayal only loses to another only betray'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    #Return betray to either gain 100 points from going against a collude or lose 250 points going against a betray
    if len(their_history)==0:
        return 'c'
    elif their_history-[1]=='b':
        result=BETRAYED(my_history, their_history, my_score, their_score)
        return result
    else:
        ending=We_Care(my_history, their_history, my_score, their_score)
        return ending
def BETRAYED(my_history, their_history, my_score, their_score):
    if my_score >= 1000 and len(their_history) > 1:
        return 'c'
    elif my_score < 1000 and len(their_history) > 1:
        return 'b'
    else:
        return 'c'
def We_Care(my_history, their_history, my_score, their_score):
    if len(my_history) == 1:
        return 'c'
    elif len(my_history) > 1 and their_history[-1] == 'c':
        return 'c' #BECAUSE WE CARE
    elif len(my_history) > 1 and their_history[-1] == 'b':
        return 'b' #BECAUSE WE DON'T CARE FOR HATERS
    else:
        return 'c' #Just in case all other if statements don't trigger
'''
def test_move(my_history, their_history, my_score, their_score, result):
    calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')  
              '''           