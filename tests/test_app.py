# tests/test_app.py
import sys
import os

# Add the root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import the summarize_text function
from app import summarize_text


def test_summarize_text():
    # Test input
    input_text = (
        "The field of artificial intelligence has seen remarkable advancements over the past decade. "
        "From natural language processing to computer vision, AI technologies are transforming industries "
        "such as healthcare, finance, and transportation."
    )

    # Call the function
    result = summarize_text(input_text)

    # Assertions
    assert isinstance(result, str), "Output should be a string"
    assert len(result) < len(
        input_text
    ), "Summary should be shorter than the input text"
    assert "AI" in result, "Summary should contain key points"
