import random

from faker import Faker

from .model_test import ModelTest


class TestRestaurantRating(ModelTest):
    fake = Faker()

    def setUp(self):
        super(TestRestaurantRating, self).setUp()

        from gooutsafe.models import restaurant_rating
        from gooutsafe.models import customer
        from gooutsafe.models import restaurant

        self.restaurant_rating = restaurant_rating
        self.customer = customer
        self.restaurant = restaurant

    def test_init(self):
        for _ in range(0, 10):
            restaurant_rating, (customer, restaurant, value, review) = TestRestaurantRating.generate_random_rating()

            self.assertEqual(restaurant_rating.review, review)
            self.assertEqual(restaurant_rating.value, value)
            self.assertEqual(restaurant_rating.customer_id, customer.id)
            self.assertEqual(restaurant_rating.restaurant_id, restaurant.id)

    def test_bad_value(self):
        from gooutsafe.models.restaurant_rating import RestaurantRating

        for _ in range(0, 10):
            restaurant_rating, _ = TestRestaurantRating.generate_random_rating()
            with self.assertRaises(ValueError):
                restaurant_rating.set_value(RestaurantRating.MIN_VALUE - random.randint(1, 100))
                restaurant_rating.set_value(RestaurantRating.MAX_VALUE + random.randint(1, 100))

    def test_bad_review(self):
        from gooutsafe.models.restaurant_rating import RestaurantRating

        for _ in range(0, 10):
            restaurant_rating, _ = TestRestaurantRating.generate_random_rating()
            with self.assertRaises(ValueError):
                text = ''.join(['a' for _ in range(0, RestaurantRating.REVIEW_MAX_LENGTH + random.randint(1, 100))])
                restaurant_rating.set_review(text)

    @staticmethod
    def generate_random_rating():
        from .test_customer import TestCustomer
        from .test_restaurant import TestRestaurant
        from gooutsafe.models.restaurant_rating import RestaurantRating

        customer, _ = TestCustomer.generate_random_customer()
        restaurant, _ = TestRestaurant.generate_random_restaurant()

        value = random.randint(RestaurantRating.MIN_VALUE, RestaurantRating.MAX_VALUE)
        review = TestRestaurantRating.fake.text(max_nb_chars=RestaurantRating.REVIEW_MAX_LENGTH)

        restaurant_rating = RestaurantRating(
            customer_id=customer.id,
            restaurant_id=restaurant.id,
            value=value,
            review=review
        )

        return restaurant_rating, (customer, restaurant, value, review)
