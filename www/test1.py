import orm
import asyncio
from Models import User, Blog, Comment

async def test(loop):
	await orm.create_pool(loop=loop, user='root',password='password',db='awesome')
	u = User(name="Test1", email='lmlmsan1@163.com', passwd='1111111', image='about:blank')
	await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.run_forever()

for x in test(loop):
    pass