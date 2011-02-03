import json
import time

from redis import Redis

class Queue(object):
  
  def __init__(self, name, prefix='', **kwargs):
    self.prefix = prefix
    self.name = name
    self.__redis = Redis(**kwargs)
  
  def push(self, payload=''):
    id = self.__redis.incr(self.prefix + 'id:' + self.name);
    packet = json.dumps({
      'id': id,
      'payload': payload,
      'error_count': 0,
      'errors': [],
      'modified': int(time.time() * 1000)
    })
    
    self.__redis.rpush(self.prefix + 'queue:' + self.name, packet);