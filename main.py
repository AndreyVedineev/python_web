import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def __get_html_content(self):
        return """
        <!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
</head>
<body>
<div class="container text-center">
    <div class="row mt-5">
        <div class="col-3">
            <div class="container bg-black text-white">
                <h4>Меню</h4>
                <nav class="nav flex-column">
                    <a class="nav-link" href="#">Главная</a>
                    <a class="nav-link" href="#">Категории</a>
                    <a class="nav-link" href="#">Заказы</a>
                    <a class="nav-link" href="#">Контакты</a>
                </nav>
            </div>
        </div>
        <div class="col-9">
            <div class="container text-center">
                <div class="row align-items-start">
                    <div class="col">
                        <form>
                            <div class="mb-3">
                                <label for="exampleInputText1" class="form-label">Имя</label>
                                <input name="name" type="text" class="form-control" id="exampleInputText1">
                            </div>
                            <div class="mb-3">
                                <label for="exampleInputEmail1" class="form-label">Почта</label>
                                <input name="email" type="email" class="form-control" id="exampleInputEmail1"
                                       aria-describedby="emailHelp">
                            </div>
                            <div class="mb-3">
                                <label for="exampleInputText2" class="form-label">Сообщение</label>
                                <input name="msg" type="textarea" class="form-control" id="exampleInputText2">
                            </div>
                            <button type="submit" class="btn btn-primary">Отправить</button>
                        </form>
                    </div>
                    <div class="col">
                        <div class="card">
                            <div class="card-body">
                                <h4 class="card-title">Наши контакты</h4>
                                <p class="card-text">119049 г. Москва, ул. Донская, д. 1008 стр. 345</p>
                                <p class="card-text">Тел. 222-22-222</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>
        """

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")