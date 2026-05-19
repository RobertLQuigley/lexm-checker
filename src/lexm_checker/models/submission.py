import os


class Submission(object):
    def __init__(self, path: str):
        self.inputs: list[SubmissionFile] = []
        if os.path.isdir(path):
            for file in os.listdir(path):
                if os.path.isfile(os.path.join(path, file)):
                    self.inputs.append(SubmissionFile(os.path.join(path, file)))
        else:
            self.inputs.append(SubmissionFile(path))

class SubmissionFile(object):
    def __init__(self, path: str):
        self.path = path
        self.is_main = False
        self.is_test = False
        self.is_source = False