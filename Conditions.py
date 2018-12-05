def wait_dom_ready(auto_chrome):
    expression = "document.readyState == 'complete';"
    return True if auto_chrome.Runtime.evaluate(expression=expression)['result']['result']['value'] else None
