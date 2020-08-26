class MyltipleDefinitionInDatabaseException(Exception):
    def __init__(self, bad_query):
        super(MyltipleDefinitionInDatabaseException, self).__init__()
        self.query = bad_query

    def __str__(self):
        return 'MyltipleDefinition on: {}'.format(self.query)
