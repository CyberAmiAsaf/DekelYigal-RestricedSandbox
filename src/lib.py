import utils
import consts
import logging

logging.getLogger().setLevel(logging.INFO)


class ProcessPremissionManager(object):
    def __init__(self, user=None, group=consts.GROUP_DEFAULT):
        """
        :type user: str | None
        :type group: str
        """
        self.user = user or utils.random_str(10)
        self.group = group

        logging.info('Created user %s of group %s', self.user, self.group)
