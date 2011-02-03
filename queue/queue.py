from redis import Redis
import json
import time

class Queue(object):
  
  def __init__(self, prefix='', name='', **kwargs):
    self.prefix = prefix
    self.name = name
    self.__redis = Redis(**kwargs)
  
  def push(self, payload=''):
    id = self.__redis.incr(self.prefix + 'id:' + self.name);
    self.__redis.rpush(self.prefix + 'queue:' + self.name, json.dumps({
      'id': id,
      'payload': payload,
      'error_count': 0,
      'errors': [],
      'modified': int(time.time() * 1000)
    }));