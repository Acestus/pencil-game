from hstest import *


class LastPencilTest(StageTest):
    @dynamic_test
    def test(self):
        main = TestedProgram()
        output = main.start().lower()
        lines = output.strip().split('\n')

        lines_non_empty = [s for s in lines if len(s) != 0]

        if len(lines_non_empty) != 2:
            raise WrongAnswer(f"Your program should print 2 non-empty lines.")

        check_pencils = [s for s in lines if '|' in s]

        if len(check_pencils) == 0:
            raise WrongAnswer("The output should include one line with several vertical bar "
                              "symbols ('|') representing pencils.")
        if len(check_pencils) > 1:
            raise WrongAnswer("The output should include only one line with several vertical bar "
                              "symbols ('|') representing pencils.")
        if len(list(set(check_pencils[0]))) != 1:
            raise WrongAnswer("The line with pencils should not contain any symbols other than the '|' symbol.")

        check_turn = any("your turn" in s for s in lines)

        if not check_turn:
            raise WrongAnswer("The output should include one line with the \"Your turn\" string")

        return CheckResult.correct()


if __name__ == '__main__':
    LastPencilTest().run_tests()