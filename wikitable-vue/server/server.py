# app.py
import tornado.ioloop
import tornado.web
import json


class MainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")
    def get(self):
        self.write("Welcome to the Tornado Server!")

class DataHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")

    def get(self):
        papername = self.get_argument('papername')
        print(papername)
        # self.set_header("Content-Type", "application/json")
        data = {}
        self.write(json.dumps(data))

class UserHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")
    def get(self):
        code = self.get_argument('code')
        print(code)
        self.write(code)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/data", DataHandler),
        (r"/user", UserHandler),
    ], debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)  # 监听8888端口
    print("Server is running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
