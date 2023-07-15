

def process_register_topics(ch, method, properties, body):
    print("RCV11 [Register] %r" % body)
    pass

def process_register_topics_extra(ch, method, properties, body):
    print("RCV12 [Register] %r" % body)
    pass