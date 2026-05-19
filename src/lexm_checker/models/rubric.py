class Rubric(object):
    def __init__(self, filename: str = None, line_data: list[str]= None):
        self.filename = filename
        if filename is not None:
            with open(filename) as f:
                self.lines = f.readlines()
        elif line_data is not None:
            self.lines = []
            for line in line_data:
                self.lines.append(line)
        else:
            self.lines = []

    def quick_compare(self, output: list[str]) -> bool:
        if len(self.lines) != len(output):
            return False
        else:
            for i, line in enumerate(self.lines):
                if output[i] != line:
                    return False
        return True