def wait_dom_ready(auto_chrome):
    expression = "document.readyState == 'complete';"
    data = auto_chrome.Runtime.evaluate(expression=expression)
    result = True if data is not None and data['result']['result']['value'] else None
    return result
