def hello():
    return b" Hello!"


def world():
    return "World!"


urlpatterns = {
    '/hello/': hello,
    '/world/': world,
}


def app(environ, start_response):
    path = environ['RAW_URI']
    view_func = urlpatterns.get(path)

    if view_func is None:
        data = b"Not found"
        start_response("404 NOT found", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])

    data = view_func()
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
