import unittest
from paramiko.ssh_exception import NoValidConnectionsError
from cmg_query import CmgQuery


class TestCmgQuery(unittest.TestCase):
    def setUp(self):
        self.cmg = CmgQuery()

    def test_login(self):
        # self.assertRaises(NoValidConnectionsError, self.cmg.connect)
        welcome_message = self.cmg.connect('127.0.0.1')
        # self.assertTrue(welcome_message.startswith("Fake SR OS Software"), "Unexpected welcome message")
        self.assertTrue(welcome_message.startswith("Fake OS Software"))
        self.cmg.disconnect()

    def test_close_connection(self):
        self.cmg.connect('127.0.0.1')
        self.cmg.disconnect()
        self.assertIsNone(self.cmg.get_client(), "SSH client should be None after closing the connection")

    def test_show_router_9999_bfd_session(self):
        self.cmg.connect('127.0.0.1')
        # ping_command = 'ping router 6203 source 10.251.74.130 10.251.74.129 count 1'
        ping_command = 'ping router 6203 source 10.251.74.130 10.251.74.129 count 1'
        cmg_output = self.cmg.cmg_output(ping_command)
        result = self.cmg.ping_result(ping_command, cmg_output)
        self.cmg.disconnect()
