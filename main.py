class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams = {}

        # for s in strs:
        #     # Create a counter for the string
        #     counter = Counter(s)

        #     # Convert the counter to a tuple so it can be used as a dictionary key
        #     counter_tuple = tuple(sorted(counter.items()))
            
        #     if counter_tuple in anagrams:
        #         anagrams[counter_tuple].append(s)
        #     else:
        #         anagrams[counter_tuple] = [s]
            
        # return list(anagrams.values())

        # anagrams = defaultdict(list) #  # No need to check if 'key' exists so we use defaultdict

        # for s in strs:
        #     sorted_word = ''.join(sorted(s))
        #     anagrams[sorted_word].append(s)


        # return list(anagrams.values())

        anagrams = {}
        for s in strs:

            sorted_word = ''.join(sorted(s))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(s)
            else:
                anagrams[sorted_word] = [s]    
            

        return list(anagrams.values())


        
