#!/usr/bin/env python3

"""
Do a local practice grading.
The score you recieve here is not an actual score,
but gives you an idea on how prepared you are to submit to the autograder.
"""

import os
import sys

import cse40.question
import cse40.assignment
import cse40.style
import cse40.utils

class Q1(cse40.question.Question):
    """
    Checks if function returns True
    """

    def __init__(self):
        super().__init__("Q1", 100)

    def score_question(self, submission):
        result = submission.my_function()
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, bool)):
            self.fail("Function must return a boolean value.")
            return

        self.full_credit()

def grade(path):
    submission = cse40.utils.prepare_submission(path)

    questions = [
        Q1(),
        cse40.style.Style(path, max_points = 0),
    ]

    assignment = cse40.assignment.Assignment('Practice Grading for Hands-On 0', questions)
    assignment.grade(submission)

    return assignment

def main(path):
    assignment = grade(path)
    print(assignment.report())

def _load_args(args):
    exe = args.pop(0)
    if (len(args) != 1 or ({'h', 'help'} & {arg.lower().strip().replace('-', '') for arg in args})):
        print("USAGE: python3 %s <submission path (.py or .ipynb)>" % (exe), file = sys.stderr)
        sys.exit(1)

    path = os.path.abspath(args.pop(0))

    return path

if (__name__ == '__main__'):
    main(_load_args(sys.argv))
