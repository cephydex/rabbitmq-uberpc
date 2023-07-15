
'''
Handle message retrieved from broker/queue
'''
def process_hello_topics(ch, method, properties, body):
    print("RCV [Hello] %r" % body)
    pass

'''
Handle message retrieved from broker/queue
'''
def process_greet_topics(ch, method, properties, body):
    print("RCV [Greet] %r" % body)
    pass