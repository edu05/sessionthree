#learn how to print in different colors

#defining variables for colors for later usage, \033[93m represents yellow for example
YELLOW = '\033[93m'
DEFAULT_COLOR = '\033[0m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RED = '\033[91m'

#define functions that return a string in a color of choice
def in_color(color_mode, x) :
	return color_mode + x + DEFAULT_COLOR

def in_yellow(x) :
	return in_color(YELLOW, x)

def in_green(x) :
	return in_color(GREEN, x)

def in_blue(x):
	return in_color(BLUE, x)

def in_red(x):
	return in_color(RED, x)

#example usage
print in_blue('print this in blue')
print in_green('print this in green')
print in_red('print this in red')
print ''

#end of lesson: learn how to print in colours

#don't need to understand this function's code, try to resist the temptation to read it
#I don't understand it - I copied it from https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
#given strings s1 and s2 returns a similarity score - see the example usages below to understand what it does
#based on Levenshtein's algorithm
def calculate_similarity_score(s1, s2):
    if len(s1) < len(s2):
        return calculate_similarity_score(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

#examples usages here

def report_similarity_score(first_string, second_string) : #prints similarity score between first_string and second_string
	similarity_score = calculate_similarity_score(first_string, second_string)
	print 'The similarity score between ' + in_yellow(first_string) + ' and ' + in_yellow(second_string) + ' is ' + in_green(str(similarity_score)) 

print 'Example usages of the similarity score function, the higher the similarity the lower the score (like golf)'
report_similarity_score('the cat sat on the mat', 'the cat sat on the mat')
report_similarity_score('the cat sat on the mat', 'the cot sat on the mot')
report_similarity_score('the cat sat on the mat', 'a cot sat on a mot')
print ''

#this function returns the top three most similar names of a list of friends
def rank_by_similarity(list_of_friends, search_term) :

	friends_and_similarity_score_pairs = [] #array of (friend, score) pairs
	for next_friend in list_of_friends :
		similarity_score = calculate_similarity_score(next_friend, search_term) #calculate the similarity score between next_friend and search_term
		friend_name_and_score_pair = (next_friend, similarity_score)
		friends_and_similarity_score_pairs.append(friend_name_and_score_pair)


    #sort friends_and_similarity_score_pairs by their score
    #don't need to understand how it works for now
	friends_ranked_by_similarity = sorted(friends_and_similarity_score_pairs, key=lambda tup: tup[1])

	
	first_three_friends_ranked_by_similarity = []
	for i in range(3) : #i will take values 0, 1 and 2
	    next_name_score_pair = friends_ranked_by_similarity[i]
	    first_three_friends_ranked_by_similarity.append(next_name_score_pair[0]) # get the name, ignore the score

	return first_three_friends_ranked_by_similarity
	                            
#this function has the ability of looking for a friend in a given list of friends
def search_for_friend(list_of_friends) :
	search_term = '' #start with an empty search term
	while True : #loop forever
		next_character = raw_input('Type a new character ') #grab the next character input from the user

		if next_character == '!' : #if the input is an exclamation mark exit the loop
			break

		search_term = search_term + next_character #append the latest character to the search term
		print 'Your latest search term is ' + in_yellow(search_term)

		top_three_similar_names = rank_by_similarity(my_friends, search_term) #obtain the 3 friends with a name that's closest to the search term
		print 'This is the list of friends you\'re most likely searching for ' + in_green(str(top_three_similar_names))
		print '-------------------------------------------'

#this represents your list of friends 
my_friends = ['eduardo', 'harry', 'edward', 'edgar', 'polly', 'larry', 'molly', 'harriet', 'holly']
print 'Your friends list is ' + in_blue(str(my_friends))

search_for_friend(my_friends) #executes the search_for_friend function