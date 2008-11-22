import datetime, hashlib

class Task(object):
    def __init__(self, subject = ""):
        self.new()

    def new(self):
        self.data = {}
        self.data["Created-On"] = datetime.datetime.now()
        self.data["Body"] = ""

    def get_creator(self):
        return self.data["Creator"]

    def set_creator(self, v):
        self.data["Creator"] = v

    creator = property(get_creator, set_creator)

    def get_subject(self):
        return self.data["Subject"]

    def set_subject(self, v):
        self.data["Subject"] = v

    subject = property(get_subject, set_subject)

    def get_body(self):
        return self.data["Body"]

    def set_body(self, body):
        self.data["Body"] = body

    body = property(get_body, set_body)

    def __str__(self):
        r = ""
        for key in self.data:
            if key is "Body":
                continue;
            try :
                value = str(self.data[key])
            except AttributeError:
                value = self.data[key]
            r += key + ": " + value + "\n"

        r += "\n" + self.data["Body"]
        return r

    def save(self):
        self.data["YABT-ID"] = self.generateId()
        print str(self)

    def generateId(self):
        sha = hashlib.sha1()
        sha.update("Created-On: " + str(self.data["Created-On"]))
        sha.update("Creator: " + self.creator)
        sha.update("Subject: " + self.subject)
        return sha.hexdigest()

