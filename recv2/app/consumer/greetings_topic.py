

def process_hello_topics(ch, method, properties, body):
    print("RCV2 [Hello] %r" % body)
    pass

def process_greet_topics(ch, method, properties, body):
    print("RCV2 [Greet] %r" % body)
    pass