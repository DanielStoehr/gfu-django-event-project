import random
from datetime import timedelta

import factory
from django.utils import timezone
from user.factories import UserFactory

from .models import Category, Event, Review

categories = [
    "Sports",
    "Talk",
    "Cooking",
    "Freetime",
    "Hiking",
    "Movies",
    "Travelling",
    "Science",
    "Arts",
    "Pets",
    "Music",
    "Wellness",
]


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Iterator(categories)
    sub_title = factory.Faker("sentence")
    description = factory.Faker("paragraph", nb_sentences=3)


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
    name = factory.Faker("sentence")
    sub_title = factory.Faker("sentence")
    description = factory.Faker("paragraph", nb_sentences=3)
    min_group = factory.LazyAttribute(lambda _: random.choice(list(Event.GroupSize)))
    date = factory.Faker(
        "date_time_between",
        start_date=timezone.now() + timedelta(days=1),
        end_date=timezone.now() + timedelta(days=60),
        tzinfo=timezone.get_current_timezone(),
    )


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review

    event = factory.SubFactory(EventFactory)
    author = factory.SubFactory(UserFactory)
    review = factory.Faker("paragraph", nb_sentences=1)
    rating = factory.LazyAttribute(lambda _: random.choice(list(Review.Rating)))
