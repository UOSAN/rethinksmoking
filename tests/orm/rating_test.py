from rethinksmoking.orm.rating import Rating


class TestRating:
    def test_post_rating(self, session):
        expected_helpfulness = 2

        rating = Rating(helpfulness=expected_helpfulness, relatability=9, familiarity=11, message_id=2, rater_id=2)
        rating.add()

        # Verify only rating in database has correct value
        actual_count = Rating.query.count()
        assert actual_count == 1

        actual_rating = Rating.query.limit(1).first()
        assert actual_rating.helpfulness == expected_helpfulness

    def test_post_multiple_ratings(self, session):
        expected_helpfulness = 2

        rating1 = Rating(helpfulness=expected_helpfulness, relatability=9, familiarity=11, message_id=2, rater_id=2)
        rating1.add()

        rating2 = Rating(helpfulness=expected_helpfulness, relatability=9, familiarity=11, message_id=2, rater_id=2)
        rating2.add()

        # Verify count of ratings in database
        actual_count = Rating.query.count()
        assert actual_count == 2
