import MySQLdb


class MySqlAgent:
    def __init__(self):
        self.db = None
        self.cur = None

    def start_db(self, database_name="ub_example"):
        print("Starting db mysql")
        self.db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                                  user="root",  # your username
                                  passwd="rootuser",  # your password
                                  db=database_name)  # name of the data base
        self.cur = self.db.cursor()
        print("Mysql started")

    def execute_statement(self, statement):
        self.cur.execute(statement)
        if "select" in statement.lower() or "show" in statement.lower():
            print(">", self.cur.fetchall())

    def close(self):
        self.cur.close()
        self.db.close()


agent = MySqlAgent()
agent.start_db()
opt = ""
while opt != "exit":
    opt = input("Type query, exit to end\n")
    if opt != "exit":
        agent.execute_statement(opt)
    else:
        print("Bye!")

agent.close()

