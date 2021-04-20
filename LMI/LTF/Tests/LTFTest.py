import abc


class LTFTest(metaclass=abc.ABCMeta):
    testIdentifiers = ["test_"]

    def __init__(self, requirements=None):
        self.requirements = []
        self.all_functions = {}
        self.extra_tests = []
        self.test_mappings = {}
        self.has_run = False
        if requirements is not None:
            for requirement in requirements:
                self.requirements.append(requirement(self))

    def find_functions(self):
        self.all_functions = {}
        for function in self.extra_tests:
            self.all_functions["extra-"+function.__name__] = function
        for functionName in self.__class__.__dict__.keys():
            for identifier in LTFTest.testIdentifiers:
                if functionName.startswith(identifier):
                    self.all_functions[functionName] = (self.__class__.__dict__.get(functionName))
                    break

    def satisfyRequirements(self):
        for requirement in self.requirements:
            if not requirement.check_satisfied():
                requirement.satisfyRequirement()

    @abc.abstractmethod
    def run(self):
        pass
