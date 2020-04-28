from rethinksmoking.orm.score import Score


class TestScore:
    def test_post_score(self, session):
        expected_quality = 2

        score = Score(quality=expected_quality, scorer_id='AA', message_id=2)
        score.add()

        # Verify only score in database has correct quality
        actual_count = Score.query.count()
        assert actual_count == 1

        actual_score = Score.query.limit(1).first()
        assert actual_score.quality == expected_quality

    def test_post_multiple_scores(self, session):
        expected_quality = 2

        score1 = Score(quality=expected_quality, scorer_id='AA', message_id=2)
        score1.add()

        score2 = Score(quality=expected_quality, scorer_id='BB', message_id=2)
        score2.add()

        # Verify count of scores in database
        actual_count = Score.query.count()
        assert actual_count == 2
