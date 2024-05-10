import logging

import canvas.api.common

BASE_ENDPOINT = "/api/v1/courses/{course}/group_categories?per_page={page_size}"

DEFAULT_KEYS = [
    'id',
    'name',
]

def request(server = None, token = None, course = None,
        keys = DEFAULT_KEYS, **kwargs):
    server = canvas.api.common.validate_param(server, 'server')
    token = canvas.api.common.validate_param(token, 'token')
    course = canvas.api.common.validate_param(course, 'course', param_type = int)

    logging.info("Fetching course ('%s') groups from '%s'." % (str(course), server))

    url = server + BASE_ENDPOINT.format(course = course, page_size = canvas.api.common.DEFAULT_PAGE_SIZE)
    headers = canvas.api.common.standard_headers(token)

    return canvas.api.common.make_get_request_list(url, headers, keys = keys)
