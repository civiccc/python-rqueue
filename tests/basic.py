import rqueue
import json
import unittest2 as unittest

class QueueTestCase(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.testqueue = rqueue.Queue('test')
    cls.testqueue._redis.flushdb()
  
  @classmethod
  def tearDownClass(cls):
    for c in cls.testqueue._redis.connection_pool.get_all_connections():
      c.disconnect()
  
  def test_push(self):
    self.testqueue.push({'a':'b'})

		# ensure the item was pushed to the queue
    self.assertEquals(self.testqueue._redis.llen(self.testqueue.queue_name), 1)
    
    value = json.loads(self.testqueue._redis.lindex(self.testqueue.queue_name, '0'))
    
    self.assertEquals(value['payload'], {'a':'b'})
  
    self.testqueue.push({'a':'c'})
    self.assertEquals(self.testqueue._redis.llen(self.testqueue.queue_name), 2)
    
    value = json.loads(self.testqueue._redis.lindex(self.testqueue.queue_name, '1'))
    self.assertEquals(value['payload'], {'a':'c'})
