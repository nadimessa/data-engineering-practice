def get_filename(uri):
    
    last_slash = uri.rfind("/")
    
    return uri[last_slash+1:]


def show_error_files():
    print(failed_uris)