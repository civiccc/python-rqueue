import json
from redis import Redis
from time import time
from uuid import uuid4

class RqueueObject(object):
  def __init__(self, name, prefix='', **kwargs):
    """The RqueueObject class is a base class for Queue's and Worker's"""
    self.prefix    = prefix
    self.name      = name
    self._redis    = Redis(**kwargs)
    self.queue_key = self.prefix + 'queue:' + self.name

class Queue(RqueueObject):
  def push(self, payload=''):
    """Push a new item to the queue"""
    packet = json.dumps({
      'id': str(uuid4()),
      'payload': payload,
      'error_count': 0,
      'errors': [],
      'modified': int(time() * 1000)
    })
    
    self._redis.rpush(self.queue_key, packet)

class Item(object):
  def __init__(self, worker, data):
    """Python object representing a queue item"""
    self.id          = data['id']
    self.payload     = data['payload']
    self.error_count = data['error_count']
    self.errors      = data['errors']
    self.modified    = data['modified']
    # Used for retry()
    self._redis      = worker._redis

  def report_error(self, error):
    """Add an error to a queue item."""
    self.error_count = self.error_count + 1
    self.errors.append(str(error))

  def retry(self):
    """Unimplemented: Put the item back on to the queue"""
    pass

  def toObject(self):
    """Returns a json.dumps-able object"""
    return {
      'id':          self.id,
      'payload':     self.payload,
      'error_count': self.error_count,
      'errors':      self.errors,
      'modified':    self.modified
    }

class Worker(RqueueObject):
  def poll(self, count=1):
    """Check the queue for pending items.
       The `count` parameter allows you to decide how many items to batch. -1 empties the entire queue.
       Returns False if no items are pending."""
    items = []

    # Load and parse the queue items.
    try:
      item = self._redis.lpop(self.queue_key)
      while item:
        items.append(Item(self, json.loads(item)))
        if count != -1 and len(items) >= count:
          break
        item = self._redis.lpop(self.queue_key)
    except Exception, e:
      raise e

    # Return the items
    if len(items) == 0:
      return False
    else:
      return items
