from json import dumps
from redis import Redis
from time import time
from uuid import uuid4

class Queue(object):
  def __init__(self, name, prefix='', **kwargs):
    self.prefix = prefix
    self.name = name
    self.queue_name = self.prefix + 'queue:' + self.name
    self._redis = Redis(**kwargs)

  def push(self, payload=''):
    packet = dumps({
      'id': str(uuid4()),
      'payload': payload,
      'error_count': 0,
      'errors': [],
      'modified': int(time() * 1000)
    })
    
    self._redis.rpush(self.queue_name, packet)
