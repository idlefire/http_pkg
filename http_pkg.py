import requests
import argparse
import urlparse
from package_template import pkg_template, header_template


def set_HOST(request_url):
    """set host function
    
    Arguments:
        request_url {str} -- url
    
    Returns:
        list -- host,path
    """
    url_parser = urlparse.urlparse(request_url)
    return url_parser.netloc, url_parser.path


def set_pkg(pkg_data):
    """set package format function
    
    Arguments:
        pkg_data {dict} -- package's data
    """
    default_template = pkg_template['default_pkg']
    pkg_format = default_template % {
        'action': pkg_data['action'].upper(),
        'rela_url': pkg_data['rela_url'],
        'host': pkg_data['host'],
        'accept-encode': pkg_data['accept-encode'],
        'accept': pkg_data['accept'],
        'accept-language': pkg_data['accept-language'],
        'user_agent': pkg_data['user_agent'],
        'conn': pkg_data['conn']
    }
    pkg_extend = ''
    for key in header_template:
        if pkg_data.has_key(key):
            pkg_extend += header_template[key] % {key: pkg_data[key]}
    pkg_format += pkg_extend
    print pkg_format


def main(request_data):
    pkg = {}
    host, path = set_HOST(request_data.url)
    pkg['action'] = request_data.action
    pkg['rela_url'] = path
    pkg['host'] = host
    pkg['accept-encode'] = request_data.accept_encoding
    pkg['accept'] = request_data.accept
    pkg['accept-language'] = request_data.accept_language
    pkg['user_agent'] = request_data.user_agent
    pkg['conn'] = request_data.connection
    for key in request_data.__dict__:
        if request_data.__getattribute__(key) != '':
            pkg[key] = request_data.__getattribute__(key)
    set_pkg(pkg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Format a Http Package.', prog='http_pkg')
    parser.add_argument('url', help='URL')
    parser.add_argument(
        '-a', '--action', default='GET', help='HTTP action.Default: GET.')
    parser.add_argument(
        '-ae',
        '--accept_encoding',
        default='gzip, deflate',
        help='HTTP Accept-Encoding.Default: gzip, deflate')
    parser.add_argument(
        '-al',
        '--accept_language',
        default='en',
        help='HTTP Accept-Language.Default: en.')
    parser.add_argument(
        '-accept', default='*/*', help='HTTP Accpet.Default: */*.')
    parser.add_argument(
        '-ua',
        '--user_agent',
        default=
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
        help='HTTP User-Agent.Default: Chrome.')
    parser.add_argument(
        '-connection', default='close', help='HTTP Connection.Default:close')
    parser.add_argument('-cookie', default='', help='HTTP Cookie.Default:')
    parser.add_argument('-request_body', default='', help='HTTP Request Body.Default:')
    request_data = parser.parse_args()
    main(request_data)