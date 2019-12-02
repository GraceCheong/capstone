class dbInfo():
    host = ''
    port = 3306
    name = ''
    user = ''
    pw = ''

    def infoInit(self, name, host, port, user, pw):
        self.host = host
        self.port = port
        self.name = name
        self.user = user
        self.pw = pw

        return self

    '''def infoInit(self, db):
        self.host = db.host
        self.port = db.port
        self.name = db.name
        self.user = db.user
        self.pw = db.pw

        return self'''

    def Init(self):
        return self
