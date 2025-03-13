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
        mock_collection = MagicMock()  # Create a mock collection
        mock_collection.find.return_value = [
            {"messages": ["Fix bug", "Refactor code", "Update docs"]}
        ]

        # Patch lazyCommit.db to return the mock collection
        # mocker.patch.object(lazyCommit, "db", return_value={"commitMessages": mock_collection})
        lazyCommit.db.commitMessages = mock_collection
        
        return mock_collection

    # Test functions

    #--------------------------------------------------RANDOM COMMIT MESSAGE ---------------------------------------

    def test_random_commit_message_with_data(self, mock_db):
        """
        Test case when commit messages exist in the database.
        """
        result = lazyCommit.random_commit_message()
        assert result in ["Fix bug", "Refactor code", "Update docs"], \
            f"Expected a valid commit message but got '{result}'"

    def test_random_commit_message_no_data(self, mock_db):
        """
        Test case when no commit messages exist.
        """
        mock_db.find.return_value = []  # Simulate no commit messages

        result = lazyCommit.random_commit_message()
        assert result == "No commit messages found!", \
            f"Expected 'No commit messages found!' but got '{result}'"

    def test_random_commit_message_aggregates_all_messages(self, mock_db):
        """
        Test case to verify that all commit messages from different styles are aggregated before selection.
        """
        mock_db.find.return_value = [
            {"style": "funny", "messages": [
                "Fixed a typo that nobody noticed.",
                "Added a space. Hope this helps."
            ]},
            {"style": "serious", "messages": ["Refactored authentication module."]}
        ]

        # Run the function multiple times to check if all messages appear
        retrieved_messages = set(lazyCommit.random_commit_message() for i in range(100))

        expected_messages = {
            "Fixed a typo that nobody noticed.",
            "Added a space. Hope this helps.",
            "Refactored authentication module."
        }

        assert retrieved_messages == expected_messages, (
            f"Expected messages {expected_messages} but got {retrieved_messages}"
        )