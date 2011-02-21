Python RQueue
=============

RQueue is a simplistic queue which uses Redis for storage. An RQueue is made up of two distinct components, a Queue and Workers. Queues have a single function which is to push new items into a RQueue (using an rpush in redis). Workers, on the other hand create a connection to an RQueue and listen for items in the RQueue (using an blpop in redis).


Notice
******

This package is currently functions only as a Queue for a RQueue, it does not function as an RQueue worker.

Node.js RQueue implementation
*****************************

For a compatible node.js worker and queue, see http://github.com/votizen/node-rqueue

Licensing
*********
Copyright (c) 2011 Votizen Incorporated

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.