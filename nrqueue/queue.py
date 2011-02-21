import json
import time

from redis import Redis
from uuid import uuid4

class Queue(object):
  
  def __init__(self, name, prefix='', **kwargs):
    self.prefix = prefix
    self.name = name
    self._redis = Redis(**kwargs)

  def id_key(self):
    return self.prefix + 'id:' + self.name

  def name_key(self):
    return self.prefix + 'queue:' + self.name

  def push(self, payload=''):
    packet = json.dumps({
      'id': str(uuid4()),
      'payload': payload,
      'error_count': 0,
      'errors': [],
      'modified': int(time.time() * 1000)
    })
    
    self._redis.rpush(self.name_key(), packet)
