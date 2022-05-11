"""Tests for the main.py file"""

# pylint: disable = import-error

import unittest
from mock import mock_open, patch
import main as m
import users as u
import user_status as us

# pylint: disable=R0904


class MainTestCase(unittest.TestCase):
    """Here's the Class Docstring."""

    def test_load_users_fails(self):
        """Tests the function which fails to open a CSV file with user data and
        adds it to an existing instance of UserCollection.
        """
        self.assertEqual(False, m.load_users('bad_file',
                                            m.init_status_collection())
                         )

    @patch('main.csv.DictWriter.writerow')
    def test_save_users_success(self, mock_writerow):
        """Saves all users in user_collection into a CSV file."""
        tmp_user = u.Users('fake_user_id',
                           'fake_email',
                           'fake_user_name',
                           'fake_user_last_name'
                           )
        tmp_user_collection = m.init_user_collection()
        tmp_user_collection.add_user(
            tmp_user.user_id,
            tmp_user.email,
            tmp_user.user_name,
            tmp_user.user_last_name
        )
        with patch('__main__.open', mock_open()):
            self.assertEqual(True,
                             m.save_users(filename='fileName',
                                          user_collection=
                                          tmp_user_collection)
                             )
            self.assertTrue(mock_writerow.called)

    def test_load_status_updates_fails(self):
        """Tests a function which opens a CSV file with status data and adds it
        to an existing instance of UserStatusCollection.
        """
        self.assertEqual(False,
                         m.load_status_updates('bad_file',
                                               m.init_status_collection()
                                               )
                         )

    @patch('main.csv.DictWriter.writerow')
    def test_save_status_updates_success(self, mock_writerow):
        """Tests a function which saves all statuses in status_collection into
        a CSV file.
        """
        tmp_user_status = us.UserStatus('fake_status_id',
                                        'fake_user_id',
                                        'fake_status_text')
        tmp_status_collection = m.init_status_collection()
        tmp_status_collection.add_status(
            tmp_user_status.status_id,
            tmp_user_status.user_id,
            tmp_user_status.status_text
        )
        with patch('__main__.open', mock_open()):
            self.assertEqual(True,
                             m.save_status_updates(filename='fileName',
                                                   status_collection=
                                                   tmp_status_collection)
                             )
            self.assertTrue(mock_writerow.called)

    def test_add_user_fails(self):
        """Tests a function which creates a new instance of User and stores it
        in user_collection."""
        tmp_user = u.Users('fake_user_id',
                           'fake_email',
                           'fake_user_name',
                           'fake_user_last_name'
                           )
        tmp_user_collection = m.init_user_collection()
        tmp_user_collection.add_user(
            tmp_user.user_id,
            tmp_user.email,
            tmp_user.user_name,
            tmp_user.user_last_name
        )
        self.assertEqual(False,
                         m.add_user('fake_user_id',
                                    'fake_email',
                                    'fake_user_name',
                                    'fake_user_last_name',
                                    tmp_user_collection
                                    )
                         )

    def test_add_user_success(self):
        """Tests a function which creates a new instance of User and stores it
        in user_collection."""
        self.assertEqual(True, m.add_user("fake_user_id",
                                          "fake_email",
                                          "fake_user_name",
                                          "fake_user_last_name",
                                          m.init_user_collection()
                                          )
                         )

    def test_modify_user_fails(self):
        """Tests a function which modifies the values of an existing user."""
        self.assertEqual(False, m.modify_user("fake_user_id",
                                              "fake_email",
                                              "fake_user_name",
                                              "fake_user_last_name",
                                              m.init_user_collection()
                                              )
                         )

    def test_modify_user_success(self):
        """Tests a function which modifies the values of an existing user."""
        tmp_user = u.Users('fake_user_id',
                           'fake_email',
                           'fake_user_name',
                           'fake_user_last_name'
                           )
        tmp_user_collection = m.init_user_collection()
        tmp_user_collection.add_user(
            tmp_user.user_id,
            tmp_user.email,
            tmp_user.user_name,
            tmp_user.user_last_name
        )
        self.assertEqual(True,
                         m.modify_user(tmp_user.user_id,
                                       tmp_user.email,
                                       tmp_user.user_name,
                                       tmp_user.user_last_name,
                                       tmp_user_collection
                                       )
                         )

    def test_delete_user_fails(self):
        """Tests a function which deletes a user from user_collection."""
        self.assertEqual(False,
                         m.delete_user("fake_user_id", m.init_user_collection()
                                       )
                         )

    def test_delete_user_success(self):
        """Tests a function which deletes a user from user_collection."""
        tmp_user = u.Users('fake_user_id',
                           'fake_email',
                           'fake_user_name',
                           'fake_user_last_name'
                           )
        tmp_user_collection = m.init_user_collection()
        tmp_user_collection.add_user(
            tmp_user.user_id,
            tmp_user.email,
            tmp_user.user_name,
            tmp_user.user_last_name
        )
        self.assertEqual(True,
                         m.delete_user(tmp_user.user_id,
                                       tmp_user_collection
                                       )
                         )

    def test_search_user_none(self):
        """Tests a function which searches for a user in user_collection(which
        is an instance of UserCollection).
        """
        self.assertEqual(None, m.search_user("fake_user_id",
                                             m.init_user_collection()
                                             )
                         )

    def test_search_user_results(self):
        """
        Tests searching for a user in a user_collection, and getting a
        result.
        """
        tmp_user = u.Users('fake_user_id',
                           'fake_email',
                           'fake_user_name',
                           'fake_user_last_name'
                           )
        tmp_user_collection = m.init_user_collection()
        tmp_user_collection.add_user(
            tmp_user.user_id,
            tmp_user.email,
            tmp_user.user_name,
            tmp_user.user_last_name
        )
        self.assertEqual(tmp_user.user_id,
                         m.search_user(tmp_user.user_id,
                                       tmp_user_collection
                                       ).user_id
                         )

    def test_add_status_fails(self):
        """Tests a function which creates a new instance of UserStatus and
        stores it in status_collection(which is an instance of
        UserStatusCollection).
        """
        tmp_user_status = us.UserStatus('fake_status_id',
                                        'fake_user_id',
                                        'fake_status_text')
        tmp_user_status_collection = m.init_status_collection()
        tmp_user_status_collection.add_status(
            tmp_user_status.status_id,
            tmp_user_status.user_id,
            tmp_user_status.status_text
        )
        self.assertEqual(False,
                         m.add_status('fake_status_id',
                                      'fake_user_id',
                                      'fake_status_text',
                                      tmp_user_status_collection
                                      )
                         )

    def test_add_status_success(self):
        """Tests a function which creates a new instance of UserStatus and
        stores it in status_collection(which is an instance of
        UserStatusCollection).
        """
        tmp_user_status = us.UserStatus('fake_status_id',
                                        'fake_user_id',
                                        'fake_status_text')
        self.assertEqual(True,
                         m.add_status(tmp_user_status.status_id,
                                      tmp_user_status.user_id,
                                      tmp_user_status.status_text,
                                      m.init_status_collection()
                                      )
                         )

    def test_modify_status_fails(self):
        """Tests a function which modifies the values of an existing
        status_id.
        """
        self.assertEqual(False, m.modify_status("fake_status_id",
                                                "fake_user_id",
                                                "fake_status text",
                                                m.init_status_collection()
                                                )
                         )

    def test_modify_status_success(self):
        """Tests a function which modifies the values of an existing
        status_id.
        """
        tmp_user_status = us.UserStatus('fake_status_id',
                                        'fake_user_id',
                                        'fake_status_text')
        tmp_user_status_collection = m.init_status_collection()
        tmp_user_status_collection.add_status(
            tmp_user_status.status_id,
            tmp_user_status.user_id,
            tmp_user_status.status_text
        )
        self.assertEqual(True,
                         m.modify_status(tmp_user_status.status_id,
                                         tmp_user_status.user_id,
                                         tmp_user_status.status_text,
                                         tmp_user_status_collection
                                         )
                         )

    def test_delete_status_false(self):
        """
        Tests searching for a status_id in status_collection, and deleting
        any result.
        """
        self.assertEqual(False, m.delete_status("fake_status_id",
                                                m.init_status_collection()
                                                )
                         )

    def test_delete_status_results(self):
        """
        Tests searching for a status_id in status_collection, and not
        getting a result.
        """
        tmp_user_status = us.UserStatus('fake_status_id',
                                        'fake_user_id',
                                        'fake_status_text')
        tmp_user_status_collection = m.init_status_collection()
        tmp_user_status_collection.add_status(
            tmp_user_status.status_id,
            tmp_user_status.user_id,
            tmp_user_status.status_text
        )
        self.assertEqual(True,
                         m.delete_status(tmp_user_status.status_id,
                                         tmp_user_status_collection
                                         )
                         )

    def test_search_status_none(self):
        """
        Tests searching for a status in status_collection, and not
        finding any results.
        """
        self.assertEqual(None, m.search_status("fake_status_id",
                                               m.init_status_collection()
                                               )
                         )

    def test_search_status_results(self):
        """
        Tests searching for a status in status_collection, and getting a
        result.
        """
        tmp_user_status = us.UserStatus('fake_status_id',
                                        'fake_user_id',
                                        'fake_status_text')
        tmp_user_status_collection = m.init_status_collection()
        tmp_user_status_collection.add_status(
            tmp_user_status.status_id,
            tmp_user_status.user_id,
            tmp_user_status.status_text
        )
        self.assertEqual(tmp_user_status.status_text,
                         m.search_status(tmp_user_status.status_id,
                                         tmp_user_status_collection
                                         ).status_text
                         )


if __name__ == '__main__':
    unittest.main()
