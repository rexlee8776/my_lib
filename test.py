import logging


# logging sample
LOG_PATH = 'server.log'
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
file_hdlr = logging.FileHandler(LOG_PATH)
file_hdlr.setLevel(logging.DEBUG)
fmt = "%(asctime)-15s %(filename)s:%(lineno)d [%(levelname)s] %(message)s"
formatter = logging.Formatter(fmt)
file_hdlr.setFormatter(formatter)
LOG.addHandler(file_hdlr)
stream_hdlr = logging.StreamHandler()
stream_hdlr.setFormatter(formatter)
stream_hdlr.setLevel(logging.DEBUG)
LOG.addHandler(stream_hdlr)

LOG.info("this is a INFO message!")
LOG.debug("this is a DEBUG message!")

# global variables sample

g_value = 3
LOG.debug("original g value is %s", g_value)


def func():
    g_value = 4
    LOG.debug("g value in func is %s", g_value)
    g_value = 5
    LOG.debug("g value in func is %s", g_value)


def func_global():
    global g_value
    LOG.debug("g value in func is %s", g_value)
    g_value = 5
    LOG.debug("g value in func is %s", g_value)


if __name__ == '__main__':
    func()
    LOG.debug("final g value is %s", g_value)


# print into a file
with open("abc.log", "w+") as f:
    print >> f, "hello world"
