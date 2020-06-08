from kafka-python import KafkaProducer

#TODO
#
Class Producer:

    def __init__(self, **kwargs):
   
        self._client = KafkaProducer( bootstrap_server = kwargs['bootstrap_server'] )

    # Todo
    def send(self, topic, message):

        self._client.send(topic, message)
