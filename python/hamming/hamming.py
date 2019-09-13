# Library with various useful difference methods
# import difflib

def distance(strand_a, strand_b):
    diff_count = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("The strands doesn't have the same length")
    else:
        if (len(strand_a) == 1) and (len(strand_b) == 1):
            if strand_a != strand_b:
                diff_count += 1
            return diff_count
        else:
            for index_a, char_a in enumerate(strand_a):
                char_b = strand_b[index_a]
                if char_a != char_b:
                    diff_count += 1
            return diff_count



# This sollution doesn't pass 1 of the assert tests
# def distance(strand_a, strand_b):
#     if len(strand_a) != len(strand_b):
#         raise ValueError("The Strands doesn't have the same length")
#     else:
#
#         # Create a list with just the difference results, it creates one item per difference
#         difference_occurrences = [x for x in difflib.ndiff(strand_a, strand_b) if x[0] != ' ']
#
#         # We need to div by 2 because the ndiff method returns dhe difference character for each lists
#         difference = len(difference_occurrences) // 2
#
#         return difference


# This method also doesn't pass the Assert test
# def distance(strand_a, strand_b):
#     difference = 0
#
#     # Raise exception if the strands doesn't have the same length
#     if len(strand_a) != len(strand_b):
#         raise ValueError("The Strands doesn't have the same length")
#     else:
#         # Verify if the strands have length == 1, so the comparison is easy
#         if (len(strand_a) == 1) and (len(strand_b) == 1):
#             if strand_a != strand_b:
#                 difference = 1
#             return difference
#         else:
#             # Initialize dicts to store que char count
#             strand_dict_a = {}
#             strand_dict_b = {}
#
#             # Count the char
#             for word in strand_a:
#                 strand_dict_a.update({word: strand_a.count(word)})
#
#             for word in strand_b:
#                 strand_dict_b.update({word: strand_b.count(word)})
#
#             # Iterate through dicts counting the differences
#             for key_a, value_a in strand_dict_a.items():
#                 if value_a != strand_dict_b[key_a]:
#                     difference += 1
#
#             return difference
