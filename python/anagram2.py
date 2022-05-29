# Don't forget to run the tests (and create some of your own)

def anagrams_for(word, list_of_words):
		lowercase_strings = []
		sorted_strings = []
		final_list = []
		test_word = word.lower()
		split_test_word = []

		for i in range(0, len(list_of_words)):
			lowercase_strings.append(list_of_words[i].lower())
		
		for x in range(0, len(lowercase_strings)):
			indiviual_letters = []
			for a in range(0, len(lowercase_strings[x])):
				indiviual_letters.append(lowercase_strings[x][a])
			sorted_strings.append(indiviual_letters)
		for i in range(0, len(sorted_strings)):
			sorted_strings[i].sort()
		for a in range(0, len(test_word)):
			split_test_word.append(test_word[a])
		split_test_word.sort()
		final_word = "".join(split_test_word)
		for b in range(0, len(sorted_strings)):
			# testing_area = "".join(sorted_strings[b])
			if final_word == "".join(sorted_strings[b]):
				final_list.append(list_of_words[b])
		# print(final_word)
		
		# print(indiviual_letters)
		# print(final_list)
		return final_list

# print(anagrams_for("threads", ["threads", "trashed", "hardest", "hatreds", "hounds"]))
