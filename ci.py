import math

class ConfigurationItem():
    """Simulates a CI"""
    def __init__(self, name, type, identifier, version=0):
        self.name = name
        self.type = type
        self.identifier = identifier
        self.version = version
        self.doc_number = self.type.upper() + '-' + self.identifier + '001'
        # numbering type and minor allowed are not implemented yet. May be implemented at a later time
        # self.numbering_type = 'standard'
        # self.minor_allowed = True
        self.minor_version = 0
        self.released = False
        self.pending = True


    def update_ci(self, level=3):
        """updates the version of a CI"""
        # Establish if currently released version is minor or not.
        if self.released != True:
            print("*" * 50)
            print("Sorry. Can't create a new version until previous version")
            print(f'({self.doc_number}) is released.')
            exit()
        minor_test = self.version - int(self.version)
        if minor_test != 0:
            prior_is_minor = True
        else:
            prior_is_minor = False
        # Check to make sure previous version was a major version
        if level > 2 and not prior_is_minor :
            self.version += 1
            self.minor_version = 0
        # TODO: identify item in database with the latest version currently existing

        # Check if previous version was minor
        elif level > 2 and prior_is_minor:
            self.vesion = math.floor(self.version)
            self.version += 1
            self.alpha_version = get_alpha(int(self.version))
            self.minor_version = 0
        else:
            self.minor_version += 1
        self.alpha_version = get_alpha(int(self.version))
        # Update doc number depending on whether or not the item is minor.
        if level >2:
            self.doc_number = self.type.upper() + '-' + self.identifier + '001' + self.alpha_version
        else:        # self.minor_version = ""
            self.doc_number = self.type.upper() + '-' + self.identifier + '001' + self.alpha_version + "." + str(self.minor_version)

        self.released = False
        self.pending = True

    def release(self):
        self.released = True
        self.pending = False
        # Optional - check that all changes have been accepted. Check that no
        # comments in the document or throw up an error if there are.
        # Optional - release on SharePoint
        # TODO: update database
    def view_ci(self):
        """Displays data on the CI"""
        print(f"{self.name} \n\tType- {self.type}")
        print(f"\tIdentifier - {self.identifier}")
        print(f"\tVersion - {self.version}.{self.minor_version}")
        print(f"\tDocNo - {self.doc_number}")
        if self.released == True:
            print("\tThis version has been released")
        elif self.pending == True:
            print("\tThis version is scheduled to be released")
        else:
            print("\tSomething went wrong.")
        # TODO: check to see a particular ci in the program
        # TODO: check to see a list of all cis in the program
        # TODO: get released version

    def change_numbering_type(self, type):
        """Used to change the numbering type of a CI"""
        # TODO: This is a low prioroty item that could be added at a later time.
        pass
    def numbering(self, type):
        """Numbers CI based on the numbering type selected."""
        # TODO: This is a low prioroty item that could be added at a later time.
        pass

    def update_db(self, table):
        pass



def get_alpha(number):
    """Generates version numbering in sequential alpha characters
    skipping 'I' and 'O'"""
    alphas = ['A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q',
                    'R','S','T','U','V','W','X','Y','Z']
    alpha_index = {d: i for i, d in enumerate(alphas,1)}
    N = len(alphas)

    if number == 0:
        return ""
    else:
        key, value = divmod(number -1, N)
        return get_alpha(key) + alphas[value]



def create_ci():
    pass
