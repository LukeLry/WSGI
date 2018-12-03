#-*-coding:utf-8-*-

from wsgiref.simple_server import make_server
from webob import Request, Response  # 后面介绍这个模块


class APPTest(object):
    def __call__(self, environ, start_response):
        urll = ['%s : %s' % (key, value) for key, value in environ.items()]  # 传递进来的environ环境变量

        print '\n'.join(urll)
        print '\n\n\n'

        req = Request(environ)  # 处理环境变量，生成Request对象，代表客户端HTTP请求传递而来的环境变量
        print req

        print '\n\n\n'
        return self.test(environ, start_response)

    def test(self, environ, start_response):
        urll = ['%s : %s' % (key, value) for key, value in environ.items()]

        print '\n'.join(urll)
        print '\n\n\n'

        res = Response() #Response类类型的实例对象res，实现__call__函数可以直接作为函数调用，对于HTTP响应header和body的封装
        print res
        print '\n\n\n'
        print type(res)

        res.status = 200
        res.body = 'hello world'
        return res(environ, start_response)


application = APPTest()

httpd = make_server('127.0.0.1', 8000, application)
print 'Listen on port 8000....'
httpd.serve_forever()