import nrqueue
import json
import unittest2 as unittest

class QueueTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.client = nrqueue.Queue('test')
		cls.client._redis.flushdb()
	
	@classmethod
	def tearDownClass(cls):
		cls.client._redis.flushdb()
		for c in cls.client._redis.connection_pool.get_all_connections():
			c.disconnect()
	
	def test_push(self):
		self.client.push({'a':'b'})
		self.assertEquals(self.client._redis.llen(self.client.name_key()), 1)
		
		value = json.loads(self.client._redis.lindex(self.client.name_key(), '0'))
		
		self.assertEquals(value['id'], 1)
		self.assertEquals(value['payload'], {'a':'b'})
	
		self.client.push({'a':'c'})
		self.assertEquals(self.client._redis.llen(self.client.name_key()), 2)
		
		value = json.loads(self.client._redis.lindex(self.client.name_key(), '1'))
		
		self.assertEquals(value['id'], 2)
		self.assertEquals(value['payload'], {'a':'c'})