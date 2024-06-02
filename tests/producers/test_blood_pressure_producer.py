import pytest
from unittest.mock import patch, MagicMock
from producers import blood_pressure_producer, callback  

@pytest.fixture
def mock_producer():
    with patch("your_module_name.Producer") as mock_producer:
        yield mock_producer

def test_say_hello(mock_producer):
    producer_instance = mock_producer.return_value
    producer_instance.produce = MagicMock()

    say_hello(producer_instance, "TestKey")

    producer_instance.produce.assert_called_once()

    expected_call = patch.call(
        'hello_topic', 
        'Hello TestKey!', 
        'TestKey', 
        on_delivery=callback
    )
    assert producer_instance.produce.call_args == expected_call

def test_callback_success():
    # Create a mock event
    event = MagicMock()
    event.topic.return_value = 'hello_topic'
    event.key.return_value = b'TestKey'
    event.value.return_value = b'Hello TestKey!'
    event.partition.return_value = 0

    # Capture the print output
    with patch('builtins.print') as mock_print:
        callback(None, event)
        mock_print.assert_called_once_with('Hello TestKey! sent to partition 0.')

def test_callback_error():
    # Create a mock event
    event = MagicMock()
    event.topic.return_value = 'hello_topic'
    event.key.return_value = b'TestKey'

    # Capture the print output
    with patch('builtins.print') as mock_print:
        callback(Exception("Error"), event)
        mock_print.assert_called_once_with('Produce to topic hello_topic failed for event: b\'TestKey\'')

if __name__ == "__main__":
    pytest.main()
