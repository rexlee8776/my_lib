import logging


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
stream_hdlr.setLevel(logging.INFO)
LOG.addHandler(stream_hdlr)


LOG.info("this is a INFO message!")
LOG.debug("this is a DEBUG message!")