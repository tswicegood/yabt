import datetime, hashlib
import pickle
import os

class Index(object):
    def __init__(self, file_name):
        try :
            self.file_name = file_name
            self.load()
        except EOFError:
            self.new()
        except IOError:
            self.new()

    def load(self):
        f = open(self.file_name, "rb")
        self.data = pickle.load(f)

    def new(self):
        self.data = {}
        self.save()

    def has(self, subject):
        return self.data.has_key(subject)

    def add(self, id, subject):
        self.data[subject] = id

    def addTask(self, task):
        self.add(task.id, task.subject)

    def get(self, subject):
        return self.data[subject]

    def save(self):
        f = open(self.file_name, "wb")
        pickle.dump(self.data, f)
        f.close()

    def __iter__(self):
        return iter(self.data)

class Task(object):
    def __init__(self, subject = ""):
        self.new()
        self.is_locked = False

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

    def get_id(self):
        return self.data["YABT-ID"]

    def set_id(self, id):
        if self.is_locked is True:
            raise AttributeError("Task is already locked")
        self.data["YABT-ID"] = id
        self.is_locked = True

    id = property(get_id, set_id)

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
        path = os.path.join(os.getcwd(), ".yabt")
        f = open(os.path.join(path, 'tickets', self.id), "w")
        f.write(str(self));
        f.close()

    def generateId(self):
        sha = hashlib.sha1()
        sha.update("Created-On: " + str(self.data["Created-On"]))
        sha.update("Creator: " + self.creator)
        sha.update("Subject: " + self.subject)
        return sha.hexdigest()

class TaskFactory(object):
    def byId(self, task_id):
        path = os.path.join(os.getcwd(), '.yabt')
        f = open(os.path.join(path, 'tickets', task_id), 'r')
        to_body_yet = False
        task = Task()
        for line in f:
            if line.strip() == "":
                to_body_yet = True
                body = ""
                continue
            if to_body_yet == True:
                task.body += line
            else:
                break_point = line.index(":")
                name = line[0:break_point].lower().strip()
                if name[0:5] == "yabt-" :
                    name = name[5:]
                task.__setattr__(name, line[break_point + 1:].strip())
        return task

