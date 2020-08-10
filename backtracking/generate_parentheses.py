from typing import List


class Solution:
    def __init__(self):
        self.solution = set()
        self.memoize = {}

    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis = "(" * n + ")" * n
        self.generate([], parenthesis)
        return self.solution

    def valid_solution(self, option: List[str]) -> bool:
        # take a copy of the list so we don't mess up the original
        potential_solution = option[:]
        closing_brackets = []
        while len(potential_solution) > 0:
            curr = potential_solution.pop()

            if curr == "(":
                # if there is an opening bracket without a closing one we terminate
                if len(closing_brackets) == 0:
                    return False
                else:
                    # otherwise we match an opening bracket to a closing one
                    closing_brackets.pop()
            else:
                closing_brackets.append(curr)
        return len(closing_brackets) == 0

    def generate(self, option: List[str], choices: List[str]):
        if len(choices) == 0:
            # validate option
            # append to solution if valid
            if self.valid_solution(option):
                self.solution.add("".join(option))
            return

        # cross check with lookup table if the option has been explored
        # if so cut execution early
        if self.memoize.get("".join(option)) is not None:
            return

        for i in range(len(choices)):
            # make a choice
            choice = choices[i]
            new_choices = choices[:i] + choices[i + 1:]
            option.append(choice)
            # explore possibilities
            self.generate(option, new_choices)
            # add to memoize table to mark that the option has been explored
            self.memoize["".join(option)] = True
            # backtrack
            option.pop()

        return


if __name__ == "__main__":
    from pprint import pprint

    pprint(Solution().generateParenthesis(6))
