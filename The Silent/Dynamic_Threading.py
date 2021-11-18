#"code" must be a string
def dthread(code):
    try:
        hyper_thread = threading.Thread(target = code)
        hyper_thread.start()
        threads.append(hyper_thread)

    except:
        pass
