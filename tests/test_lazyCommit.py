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
        mock_data = [
            {"style": "funny", "messages": [
                "Fixed a typo that nobody noticed.",
                "Added a space. Hope this helps."
            ]},
            {"style": "serious", "messages": ["Fix bug", "Refactor code", "Update docs"]}
        ]

        mock_collection.find.return_value = mock_data

        # Patch lazyCommit.db to return the mock collection
        lazyCommit.db.commitMessages = mock_collection
        
        return mock_collection

    # Test functions

    #--------------------------------------------------RANDOM COMMIT MESSAGE ---------------------------------------

    def test_random_commit_message_with_data(self, mock_db):
        """
        Test case when commit messages exist in the database.
        """
        result = lazyCommit.random_commit_message()
        assert result in ["Fixed a typo that nobody noticed.", "Added a space. Hope this helps.", "Fix bug", "Refactor code", "Update docs"], \
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
        # Run the function multiple times to check if all styles of messages appear
        retrieved_messages = set(lazyCommit.random_commit_message() for i in range(100))

        expected_messages = {
            "Fixed a typo that nobody noticed.",
            "Added a space. Hope this helps.",
            "Fix bug", 
            "Refactor code", 
            "Update docs"
        }

        assert retrieved_messages == expected_messages, (
            f"Expected messages {expected_messages} but got {retrieved_messages}"
        )

#-------------------------------------------GENERATE COMMIT MESSAGE-------------------------------------------

    def test_generate_commit_message_retrieves_correct_style(self, mock_db):
        """
        Test case to ensure that when a user requests a specific style,
        only messages from that style are retrieved.
        """

        # Simulate MongoDB behavior: filter messages by style
        def mock_find(query):
            return [doc for doc in mock_db.find.return_value if doc["style"] == query.get("style")]

        # Override the default behavior of find() to simulate MongoDB filtering when a user inputs a style query
        mock_db.find.side_effect = mock_find 

        # Testing style: funny
        result = lazyCommit.generate_commit_message("funny")
        expected_messages = ["Fixed a typo that nobody noticed.", "Added a space. Hope this helps."]
        assert result in expected_messages, (f"Expected a message from 'funny' style but got '{result}'")

        # Testing style: serious
        result_serious = lazyCommit.generate_commit_message("serious")
        expected_serious_messages = ["Fix bug", "Refactor code", "Update docs"]
        assert result_serious in expected_serious_messages, (f"Expected a message from 'serious' style but got '{result_serious}'")

    def test_generate_commit_message_no_matching_style(self, mock_db):
        """
        Test case to ensure that when a user requests a style that does not exist,
        the function returns the appropriate message.
        """
        # Simulate MongoDB behavior: filter messages by style
        def mock_find(query):
            return [doc for doc in mock_db.find.return_value if doc["style"] == query.get("style")]

        # Override the default behavior of find() to simulate MongoDB filtering
        mock_db.find.side_effect = mock_find 

        # Testing a non-existent style: "nostalgic"
        result = lazyCommit.generate_commit_message("nostalgic")
        expected_message = "No commit messages found for style: nostalgic"

        assert result == expected_message, (f"Expected '{expected_message}' but got '{result}'")
    
    def test_generate_commit_message_empty_messages(self, mock_db):
        """
        Test case to ensure that when a style exists but has no messages,
        the function correctly returns the expected message.
        """
        def mock_find(query):
            return [{"style": "empty_style", "messages": []}]  

        mock_db.find.side_effect = mock_find 

        result = lazyCommit.generate_commit_message("empty_style")
        expected_message = "No commit messages found for style: empty_style"

        assert result == expected_message, (f"Expected '{expected_message}' but got '{result}'")