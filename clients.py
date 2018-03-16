 from celery_app import task1, task2

 result1 = task1.add.apply_async(args=[2, 8])
 result2 = task2.multiply.apply_async(args=[2, 8])
 print 'hello world'
 print result1.get()
 print result2.get()
