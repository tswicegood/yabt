import datetime, hashlib
import pickle
import os
import glob

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

    def add_task(self, task):
        self.add(task.id, task.subject)

    def remove(self, subject):
        self.data.pop(subject)

    def remove_task(self, task):
        self.remove(task.subject)

    def get(self, subject):
        return self.data[subject]

    def save(self):
        f = open(self.file_name, "wb")
        pickle.dump(self.data, f)
        f.close()

    def __iter__(self):
        return iter(self.data)

class Task(object):
    def __init__(self, subject = "", data = None):
        self.is_locked = False
        self.data = {}
        self.file = TaskFile(self)
        if data is not None:
            self.__initialize(data)
        else:
            self.new()

    def __initialize(self, data):
        for key, value in data.iteritems():
            self.__setattr__(key, value)


    def new(self):
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

    def get_created_on(self):
        return self.data['Created-On']

    def set_created_on(self, data):
        if self.is_locked == True:
            raise Error, "Can't change the Created-On date after being locked"
        self.data['Created-On'] = data;

    created_on = property(get_created_on, set_created_on)

    def get_status(self):
        if self.data.has_key('YABT-Status') :
            return self.data['YABT-Status']
        else:
            return "N/A"

    def set_status(self, status):
        self.data['YABT-Status'] = status

    status = property(get_status, set_status)

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
        self.data["YABT-ID"] = self.generate_id()
        path = os.path.join(os.getcwd(), ".yabt")
        f = open(os.path.join(path, 'tickets', self.id), "w")
        f.write(str(self));
        f.close()

    def remove(self):
        self.file.remove();

    def generate_id(self):
        sha = hashlib.sha1()
        sha.update("Created-On: " + str(self.data["Created-On"]))
        sha.update("Creator: " + self.creator)
        sha.update("Subject: " + self.subject)
        return sha.hexdigest()

class TaskFile(object):
    def __init__(self, task):
        self.task = task

    def remove(self):
        task_name = self.generateTaskName()
        os.remove(task_name)

    def generateTaskName(self):
        return os.path.join(os.getcwd(), ".yabt", "tickets", self.task.id)

class TaskFactory(object):
    def find(self, criteria):
        strategies = [
            self.by_id,
            self.by_title,
            self.by_partial_id
        ]
        for strategy in strategies:
            task = strategy(criteria)
            if task is not None:
                return task
        return None

    def by_title(self, subject):
        index = Index(os.path.join(os.getcwd(), ".yabt", "index"))
        if index.has(subject):
            task_id = index.get(subject)
            return self.by_id(task_id)

    def by_id(self, task_id):
        task_file = self.__ticket_file(task_id)
        if os.path.exists(task_file) != True:
            return None;
        return self.__load_task_by_full_name(task_file)

    def by_partial_id(self, partial_id):
        tickets = glob.glob(self.__ticket_file(partial_id) + "*")
        num_of_tickets = len(tickets)
        if num_of_tickets == 1:
            return self.__load_task_by_full_name(tickets[0])
        elif num_of_tickets == 0:
            return None
        else:
            return tickets

    def __ticket_directory(self):
        return os.path.join(os.getcwd(), '.yabt', 'tickets');

    def __ticket_file(self, id):
        return os.path.join(self.__ticket_directory(), id)

    def __load_task_by_full_name(self, task_file):
        f = open(task_file, 'r')
        to_body_yet = False
        # TODO: refactor this into its own reader
        data = {}
        for line in f:
            if line.strip() == "":
                to_body_yet = True
                data["body"] = ""
                continue
            if to_body_yet == True:
                data["body"] += line
            else:
                break_point = line.index(":")
                name = line[0:break_point].lower().strip().replace("-", "_")
                if name[0:5] == "yabt_" :
                    name = name[5:]
                data[name] = line[break_point + 1:].strip()
        task = Task(data = data)
        return task


