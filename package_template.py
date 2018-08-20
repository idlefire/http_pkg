pkg_template = {
    "default_pkg":
    "%(action)s %(rela_url)s HTTP/1.1\r\n" + "Host: %(host)s\r\n" +
    "Accept-Encoding: %(accept-encode)s\r\n" + "Accept: %(accept)s\r\n" +
    "Accept-Language: %(accept-language)s\r\n" +
    "User-agent: %(user_agent)s\r\n" + "Connection: %(conn)s\r\n"
}

header_template = {
    "cookie" : "Cookie: %(cookie)s \r\n",
    "request_body": "\r\n%(request_body)s"
}

