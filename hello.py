def wsgi_processor_make_file(environ, start_response):
    query = environ["QUERY_STRING"]
    document = query.replace('&', '\n').encode('utf-8') # ??

    headers = [
        ('Content-Type', 'text/plain')
    ]
    status = "200 OK"

    start_response(status, headers)
    return [document]

