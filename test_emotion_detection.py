from EmotionDetection import emotion_detector

def test_emotion_detector():
    result = emotion_detector("I am very happy today!")
    
    assert result is not None
    assert "joy" in result
    assert result["dominant_emotion"] == "joy"

test_emotion_detector()
print("All tests passed!")