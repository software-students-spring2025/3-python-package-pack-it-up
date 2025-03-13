import pytest
from unittest.mock import MagicMock
from commitPackage import lazyCommit

class Tests:
    #
    # Fixtures - these are functions that can do any optional setup or teardown before or after a test function is run.
    #

    @pytest.fixture
    def mock_db(self, mocker):
        """
        A pytest fixture that mocks the MongoDB collection find() method.
        """
        mock_find = mocker.patch("src.commitPackage.db.commitMessages.find")  # Mock DB query
        return mock_find

    #
    # Test functions
    #

    def test_random_commit_message_with_data(self, mock_db):
        """
        Test case when commit messages exist in the database.
        """
        mock_db.return_value = [
            {"messages": ["Fix bug", "Refactor code", "Update docs"]}
        ]

        result = random_commit_message()
        assert result in ["Fix bug", "Refactor code", "Update docs"], \
            f"Expected a valid commit message but got '{result}'"