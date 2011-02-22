import rqueue
import json
import unittest2 as unittest

class QueueTestCase(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.testqueue  = rqueue.Queue('test')
    cls.testqueue2 = rqueue.Queue('test2')
    cls.testworker = rqueue.Worker('test2')
  
  @classmethod
  def tearDownClass(cls):
    cls.testqueue._redis.flushdb()
    for c in cls.testqueue._redis.connection_pool.get_all_connections():
      c.disconnect()
  
  def test_push(self):
    self.testqueue.push({'a':'b'})

    # ensure the item was pushed to the queue
    self.assertEquals(self.testqueue._redis.llen(self.testqueue.queue_key), 1)
    
    value = json.loads(self.testqueue._redis.lindex(self.testqueue.queue_key, '0'))
    
    self.assertEquals(value['payload'], {'a':'b'})
  
    self.testqueue.push({'a':'c'})
    self.assertEquals(self.testqueue._redis.llen(self.testqueue.queue_key), 2)
    
    value = json.loads(self.testqueue._redis.lindex(self.testqueue.queue_key, '1'))
    self.assertEquals(value['payload'], {'a':'c'})

  def test_poll(self):
    self.testqueue2.push('bacon')
    self.testqueue2.push('bacon2')
    self.testqueue2.push('bacon3')
    result = self.testworker.poll(-1)

    self.assertEquals(3, len(result));
    assert(result[0].id)
    assert(result[1].id)
    assert(result[2].id)
    self.assertEquals('bacon', result[0].payload)
    self.assertEquals('bacon2', result[1].payload)
    self.assertEquals('bacon3', result[2].payload)
